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
        similarities = []
        for i in range(10):
            similarities.append(Similarity(1,create_random_sentence(), create_random_sentence()))
        assert compute_score(similarities) == 1


def testComputeScore_WithRandomSimilaritiesScore():
        similarities = []
        score = 0
        for i in range(10):
            curr = random.uniform(0,1)
            score += curr
            similarities.append(Similarity(curr,create_random_sentence(), create_random_sentence()))
        assert compute_score(similarities) == round(score // len(   similarities), 2)



def testComputeScore_WithSimilaritiesScore_EqualsTo0():
        similarities = []
        for i in range(10):
            similarities.append(Similarity(0,create_random_sentence(), create_random_sentence()))
        assert compute_score(similarities) == 0

def testDisplayScore_WritesRightMsgOnStdout(capsys):
    score = 0.89
    display_score(score)
    captured = capsys.readouterr() 
    assert captured.out == "Similarity score: 0.89\n"
