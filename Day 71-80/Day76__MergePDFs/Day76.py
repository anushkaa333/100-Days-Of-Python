#Ex. 8
# Merge all pdfs in current directory


from PyPDF2 import PdfWriter  #ModuleNotFoundError: No module named 'pypdf2' <== Will throw this error becoz its case sensitive
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close() 




