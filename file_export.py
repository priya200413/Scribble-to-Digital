from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document
import io


def export_txt(text):
    buffer = io.BytesIO()
    buffer.write(text.encode())
    buffer.seek(0)
    return buffer


def export_pdf(text):

    buffer = io.BytesIO()

    c = canvas.Canvas(buffer, pagesize=letter)

    y = 750

    for line in text.split("\n"):
        c.drawString(50, y, line)
        y -= 20

    c.save()

    buffer.seek(0)

    return buffer


def export_docx(text):

    doc = Document()

    for line in text.split("\n"):
        doc.add_paragraph(line)

    buffer = io.BytesIO()
    doc.save(buffer)

    buffer.seek(0)

    return buffer