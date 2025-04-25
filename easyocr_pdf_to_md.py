import os
import sys
import subprocess
from pathlib import Path
from pdf2image import convert_from_path
import easyocr
import numpy as np

def run_cmd(cmd):
    print(f"\n👉 执行命令：{' '.join(cmd)}")
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("❌ 错误信息：", result.stderr.decode(errors='ignore'))
    return result

def convert_docx(file_path):
    output = file_path.with_suffix('.md')
    run_cmd(['pandoc', str(file_path), '-f', 'docx', '-t', 'markdown', '-o', str(output)])
    print(f"✅ Word 转换完成: {output}")

def convert_pdf_text(file_path):
    txt_path = file_path.with_suffix('.txt')
    md_path = file_path.with_suffix('.md')
    run_cmd(['pdftotext', str(file_path), str(txt_path)])
    run_cmd(['pandoc', str(txt_path), '-f', 'markdown', '-t', 'markdown', '-o', str(md_path)])
    print(f"✅ 文本型 PDF 转换完成: {md_path}")
    txt_path.unlink(missing_ok=True)

def convert_pdf_image(file_path):
    print(f"🧠 使用 EasyOCR 处理图片型 PDF: {file_path.name}")
    images = convert_from_path(str(file_path), dpi=300)
    reader = easyocr.Reader(['ch_sim', 'en'])
    all_text = []
    for img in images:
        result = reader.readtext(np.array(img), detail=0)
        all_text.extend(result)
    md_path = file_path.with_suffix('.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(all_text))
    print(f"✅ 图片型 PDF（OCR）转换完成: {md_path}")

def is_pdf_textual(file_path):
    result = subprocess.run(['pdffonts', str(file_path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return len(result.stdout.decode(errors='ignore').strip().split('\n')) > 2

def process_file(file_path):
    if file_path.suffix.lower() == '.doc':
        print(f"📎 正在将 .doc 转换为 .docx: {file_path.name}")
        new_docx = file_path.with_suffix('.docx')
        run_cmd(['soffice', '--headless', '--convert-to', 'docx', str(file_path), '--outdir', str(file_path.parent)])
        convert_docx(new_docx)
    elif file_path.suffix.lower() == '.docx':
        convert_docx(file_path)
    elif file_path.suffix.lower() == '.pdf':
        if is_pdf_textual(file_path):
            convert_pdf_text(file_path)
        else:
            convert_pdf_image(file_path)

def main(path_str):
    path = Path(path_str)
    if not path.exists():
        print("❌ 路径不存在")
        return
    if path.is_file():
        process_file(path)
    elif path.is_dir():
        print(f"📂 正在扫描目录：{path}")
        for file in path.rglob("*"):
            if file.suffix.lower() in ['.pdf', '.docx', '.doc']:
                print(f"\n--- 处理文件：{file} ---")
                process_file(file)

if __name__ == '__main__':
    main(sys.argv[1])