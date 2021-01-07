from IA.check_plagiarism import find_similarities, merge_similarities
from reader.text_extractor import extract_text_from_file
import pytest
import argparse
import sys
import textract

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tests", help="Run the testsuite",
                         action="store_true")
    parser.add_argument("filename")
    parser.add_argument("filename2")
    parser.add_argument("--score",
                        action="store_true")
    return parser

def display_help_message():
    print("usage: CheckSimilarities [-t] [-h] fname fname2\n")
    print("compute and display sentence similarities between text files\n")
    print("positional arguments:")
    print("fname        path to the first file to compare")
    print("fname2       path to the second file to compare")
    print("")
    print("optional arguments:")
    print("-h, --help   Show this help message ")
    print("-t, --tests  Run the testsuite over the progam and exit")
    print("")

def display_similarities(sims_intervals, text):
    index = 0
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    for interval in sims_intervals:
        print(text[index:interval[0]], end="")
        print(FAIL + text[interval[0]:interval[1]] + ENDC, end="")
        index = interval[1]
    if(index != len(text) - 1):
        print(text[index:len(text)], end="")
    print()



def compute_score(scoreList):    
    result = 0
    if(len(scoreList) == 0):
        return 0

    for score in scoreList:        
        result += score
            
    return round(result / len(scoreList), 2)

def display_score(score):
    print("Similarity score: " + str(score))


def process_cmdline_args(args):
    try:    
        text = textract.process(args.filename, encoding='ascii').decode("utf-8")         
        text2 = textract.process(args.filename2, encoding='ascii').decode("utf-8")
    except Exception as e:
        print(e, file=sys.stderr)
        return
    
    sims, scores = find_similarities(text, text2)    
    sims_intervals = merge_similarities(sims)

    BOLD = '\033[1m'
    ENDC = '\033[0m'
    print(BOLD + "First File:" + ENDC)
    display_similarities(sims_intervals[0], text2)
    
    print(BOLD + "\nSecond File:" + ENDC)
    display_similarities(sims_intervals[1], text)

    if(args.score):
        score = compute_score(scores)
        display_score(score)        


def handle_unknown_arg_provided():
    print("Unknown args have been provided", file=sys.stderr)
    display_help_message()

if __name__ == "__main__":    
    parser = init_parser()    
    while True:
        astr = input('main.py ')
        if('exit' in astr):
                exit()        
        ns, unknown_args = parser.parse_known_args(astr.split())        
        if unknown_args != []:
            handle_unknown_arg_provided()
        else:            
            process_cmdline_args(ns)
