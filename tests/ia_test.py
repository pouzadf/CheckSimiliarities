from IA.check_plagiarism import *


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
        

