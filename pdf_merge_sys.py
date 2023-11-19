import PyPDF2
import sys
# print(PyPDF2.__version__)
# tty: python3 name_of_py.py pdf-1.pdf pdf-2.pdf pdf-n.pdf

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('./files/super.pdf') # i mean, your choice.. duuh


pdf_combiner(inputs)
