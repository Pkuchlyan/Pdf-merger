import PyPDF2

pdffiles = ["sample.pdf" , "s2.pdf"]
marger =  PyPDF2.PdfMerger()
for file in pdffiles:
    pdffile = open(file , 'rb')
    pdfreader = PyPDF2.PdfReader(pdffile)
    marger.append(pdfreader)
pdffile.close()
marger.write('new.pdf')