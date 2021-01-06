from main import *
from utils import *
import random
from pytest import *
from models.similarity import *

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
    assert captured.out != ""




def testComputeScore_WithNoSimilarities():
    assert compute_score([]) == 0


def testComputeScore_WithSimilaritiesScore_EqualsTo1():        
        assert compute_score([1.0, 1.0, 1.0, 1.0, 1.0]) == 1


def testComputeScore_WithRandomSimilaritiesScore():
        scores = [0.85, 0.48, 0.78, 0.64, 0.25]
        res  = 0
        for s in scores:
            res += s

        assert compute_score(scores) == round(res / len(scores), 2)



def testComputeScore_WithSimilaritiesScore_EqualsTo0():
        assert compute_score([0.0, 0.0, 0.0, 0.0, 0.0]) == 0

def testDisplayScore_WritesRightMsgOnStdout(capsys):
    score = 0.89
    display_score(score)
    captured = capsys.readouterr() 
    assert captured.out == "Similarity score: 0.89\n"
