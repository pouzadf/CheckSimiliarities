from reader.text_extractor import *
from pytest import *

def testExtractFile_WrongPath(capsys):
    extract_text_from_file('filename')
    captured = capsys.readouterr() 
    assert captured.err == 'No such file: filename\n'

def testExtractFile_NoExtensions():
    pass