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


def testBuildSentence_returnsNotEmptyList():
    text_1 = "Null Island\n\
\
Null Island is a name for the area around the point where the prime meridian and the equator cross, located in international waters in the Gulf of Guinea (Atlantic Ocean) off the west African coast.[1] In the WGS84 datum, this is at zero degrees latitude and longitude (0°N 0°E), and is the location of a buoy. The name 'Null Island' serves as both a joke based around the suppositional existence of an island there, and also as a name to which coordinates erroneously set to 0,0 are assigned in placenames databases in order to more easily find and fix them."
    sequences = window_tokenizer(text_1)    
    assert len(build_sentences(text_1, sequences)) > 0     


def testBuildSentence_returnsSentences_WithRightIndex():
    text_1 = "Null Island\n\
\
Null Island is a name for the area around the point where the prime meridian and the equator cross, located in international waters in the Gulf of Guinea (Atlantic Ocean) off the west African coast.[1] In the WGS84 datum, this is at zero degrees latitude and longitude (0°N 0°E), and is the location of a buoy. The name 'Null Island' serves as both a joke based around the suppositional existence of an island there, and also as a name to which coordinates erroneously set to 0,0 are assigned in placenames databases in order to more easily find and fix them."
    sequences = window_tokenizer(text_1)
    sentences = build_sentences(text_1, sequences)
    for s in sentences:
        assert s.text == text_1[s.start:s.end]


def testBuildSentence_returnsSentences_WithRightIndex2():
  text_1 = "The mysterious diary records the voice.\n Three years later, the coffin was still full of Jello.\n His ultimate dream fantasy consisted of being content and sleeping eight hours in a row. Sometimes I stare at a door or a wall and I wonder what is this reality, why am I alive, and what is this all about?\nThe lyrics of the song sounded like fingernails on a chalkboard."
  sequences = window_tokenizer(text_1)
  sentences = build_sentences(text_1, sequences)
  for s in sentences:
    assert s.text == text_1[s.start:s.end]




def testBuildSentence_returnsSentences_WithRightIndex3():
  text_1 = "Courage and stupidity were all he had.\n It was the best sandcastle he had ever seen. David subscribes to the stuff your tent into the bag strategy over nicely folding it.\n He knew it was going to be a bad day when he saw mountain lions roaming the streets. \nTruth in advertising and dinosaurs with skateboards have much in common."
  sequences = window_tokenizer(text_1)
  sentences = build_sentences(text_1, sequences)
  for s in sentences:
    assert s.text == text_1[s.start:s.end]