from IA.check_plagiarism import *
from main import *
from utils import *
from pytest import *

def testDisplayHelpMessage_WritesOnStdout(capsys):
    display_help_message()
    captured = capsys.readouterr() 
    assert len(captured.out) > 0

def testHandleUnknownArgProvided_WritesOnStdoutAndStdErr(capsys):
    handle_unknown_arg_provided()
    captured = capsys.readouterr()
    assert len(captured.out) > 0
    assert len(captured.err) > 0


def testHandleUnknownArgProvided_WritesRightMessageOnStdErr(capsys):
    handle_unknown_arg_provided()
    captured = capsys.readouterr()
    assert captured.err == "Unknown args have been provided\n"   


def testDisplayHelpMessage_WritesCorrectMsgOnStdout(capsys):
    display_help_message()
    captured = capsys.readouterr() 
    help_sentences = [seq for seq in captured.out.splitlines() if len(seq) > 0]
    assert "usage: CheckSimilarities [-t] [-h] fname fname2" == help_sentences[0]
    assert "compute and display sentence similarities between text files" == help_sentences[1]
    assert "positional arguments:" == help_sentences[2]
    assert "fname        path to the first file to compare" == help_sentences[3]
    assert "fname2       path to the second file to compare" == help_sentences[4]
    assert "optional arguments:" == help_sentences[5]
    assert "-h, --help   Show this help message " == help_sentences[6]
    assert "-t, --tests  Run the testsuite over the progam and exit" == help_sentences[7]
    
