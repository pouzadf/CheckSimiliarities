from IA.check_plagiarism import *
from utils import *


def testSequenceListSize_whenTokenized_withOddStrideSize():
    sentence = create_random_sentence()
    sequences = window_tokenizer(sentence, window_size = 2, strides = 2)
    assert len(sequences) == 5


def testSequenceListSize_whenTokenized_withNotOddStrideSize():
    sentence = create_random_sentence()
    sequences = window_tokenizer(sentence, window_size = 2, strides = 3)   
    [print(seq.text) for seq in sequences]
    assert len(sequences) == 3


def testSequenceSize_whenTokenized_withOddWindowSize():
    sentence = create_random_sentence()    
    sequences = window_tokenizer(sentence, window_size = 5, strides = 5)    
    for seq in sequences:        
        assert len(seq.text.split()) == 5