from pypdf import PdfWriter
import os

merger = PdfWriter()

pdfs = list(filter(lambda x: x.endswith(".pdf"), os.listdir()))
pdfs.sort()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
