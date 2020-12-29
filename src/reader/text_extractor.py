
import os
import sys


def extract_text_from_file(path):
    name, extension = os.path.splitext(path)
    try:
        with open(path) as f:
            if(extension == 'pdf'):
                print("pdf")
            elif (extension == 'docx'):
                print("docx")
            else:
                return " ".join(f.readlines())
    except:
        print("No such file: " + path, file=sys.stderr)
        return None

def extract_from_pdf():
    pass


def extract_from_docx():
    pass