import spacy
from sentence_transformers import SentenceTransformer
from sentence import Sentence
from similarity import Similarity
import scipy

BIAS = 0.7

def window_tokenizer(text, window_size=10, strides=4):
    """
    :param text: String. Text to tokenize.
    :param window_size: int. Nb of words in a sequences.
    :param strides: int. Nb of words to shift over to create a new sequence.
    """
    sequences = []
    sentence_tokenizer = spacy.load("en_core_web_sm")
    tok_doc = sentence_tokenizer(text)
    sentences = [sent.string for sent in tok_doc.sents]
    for sent in sentences:
        word_sent = sent.split()
        start = 0
        end = window_size
        len_sent = len(word_sent)
        while end - start == window_size:
            seq = word_sent[start:end]
            sequences.append(seq)
            start += strides
            tmp_end = end + strides
            end = tmp_end if tmp_end <= len_sent else end
    sequences = [ " ".join(seq) for seq in sequences]
    return build_sentences(sentences, sequences)


def build_sentences(sentences, sequences)   :
    text = " ".join(seq for seq in sentences)     
    sentences = []        
    for seq in sequences:              
        try:                          
            index = text.index(seq)    
            indexEnd = index + len(seq)              
            sentences.append(Sentence(seq, index, indexEnd))
        except:
            print("error")                      
    return sentences

def get_distances(emb_model, tokenizer, doc1, doc2):
    docs_emb = []
    docs_sentences = []
    for text in [doc1, doc2]:        
        sentences = tokenizer(text)    
        sentencesContent = [seq.text for seq in sentences]            
        docs_sentences.append(sentences)                                           
        sentences_embeddings = emb_model.encode(sentencesContent)
        docs_emb.append(sentences_embeddings)    
    distance_matrix = scipy.spatial.distance.cdist(docs_emb[0], docs_emb[1], "cosine")
    #results = zip(range(len(distances)), distances)
    #results = sorted(results, key=lambda x: x[1])
    return docs_sentences, distance_matrix



def find_similarities(text_1, text_2):
    model = SentenceTransformer("distilbert-base-nli-stsb-mean-tokens")
    #sequences: resultats de la tokenization
    #distances: matrices avec une distance de 0 à 1. similarity = 1 - distance
    # distances à l'index (i, j): distance entre la sequence i et la sequence j
    # => matrice symetrique 
    sequences, distances = get_distances(model, window_tokenizer, text_1, text_2)
    similarities = []
    for i, qi in enumerate(sequences[0]):        
        for j, qj in enumerate(sequences[1]):
            distanceNormalized = 1 - distances[i][j]            
            if(distanceNormalized > BIAS):
                    similarities.append(Similarity(distanceNormalized, qi, qj))
    return similarities
       

