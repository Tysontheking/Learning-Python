from PyPDF2 import PdfWriter

marger = PdfWriter()

pdfs = []

pdfMerge = int(input("How many pdf do you merge : "))

for i in range(0,pdfMerge):
    pdf_name = input(f"Enter pdf name {i+1} : ")
    pdfs.append(pdf_name)

for pdf in pdfs:
    marger.append(pdf,import_outline=False)

marger.write("Merge_pdf.pdf")
marger.close()