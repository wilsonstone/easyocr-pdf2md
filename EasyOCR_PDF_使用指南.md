# 📘 中文 PDF/Word 批量转换说明

支持将目录中所有 PDF 和 Word 文件转换为 Markdown：

- `Word (.docx)` → Markdown（`pandoc`）
- `文本型 PDF` → Markdown（`pdftotext + pandoc`）
- `扫描型 PDF` → Markdown（`pdf2image + EasyOCR`）

## 🛠 安装依赖

```bash
brew install poppler pandoc  # macOS
sudo apt install poppler-utils pandoc -y  # Linux
pip install easyocr pdf2image numpy
```

## 支持的文件格式

- `.docx`：Word（现代格式）
- `.doc`：Word（老版格式，将自动使用 LibreOffice 转换为 `.docx`）
- `.pdf`：自动判断是否为图片型（OCR）或文本型

## 📂 使用方式

```bash
python easyocr_pdf_to_md.py /你的/目录路径/
```

---

可扩展输出格式为 HTML/JSON，如需请联系开发者。