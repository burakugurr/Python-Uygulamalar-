from pdf2docx import Converter

pdf_file = 'imzalancaklar.pdf'
docx_file = 'cv.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()
