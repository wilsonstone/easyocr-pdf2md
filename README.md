# 🧠 EasyOCR 中文 PDF/Word 批量识别工具

支持将 `.pdf` 和 `.docx` 批量转换为 Markdown 格式文本，支持中文 OCR。

## 📦 安装依赖（macOS/Linux）

```bash
brew install poppler pandoc  # macOS
sudo apt install poppler-utils pandoc -y  # Linux
pip install -r requirements.txt
```

## 📝 支持的文件格式

- `.docx`（Word 现代格式）
- `.doc`（Word 老格式，会自动转换为 .docx）
- `.pdf`（文本型和图片型）

## 🚀 使用方式

```bash
python easyocr_pdf_to_md.py /path/to/pdf_or_directory/
```

支持：

- 📄 Word (`.docx`)
- 🧾 文本型 PDF（`pdftotext` 提取）
- 📷 图片型 PDF（`EasyOCR` OCR）

## ✨ 输出格式

每个文件生成 `.md` 文件，保存在原目录中。