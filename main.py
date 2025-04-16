from pdf2docx import Converter

pdf_path = "sample.pdf" #pdf dosyası burada olduğu direk yazabiliriz.Olmasaydı tek tek yolu yazmalıyız.
docx_path = "sample.docx"

cv = Converter(pdf_file=pdf_path) #pdf_file, python'da parametrenin adıdır.cv oluşturulan dosyanın adıdır.
cv.convert(docx_filename=docx_path)
cv.close()