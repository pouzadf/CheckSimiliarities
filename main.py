from IA.check_plagiarism import find_similarities
import pytest
import argparse
import sys


def test():
    text_1 = "Null Island\n\
\
Null Island is a name for the area around the point where the prime meridian and the equator cross, located in international waters in the Gulf of Guinea (Atlantic Ocean) off the west African coast.[1] In the WGS84 datum, this is at zero degrees latitude and longitude (0°N 0°E), and is the location of a buoy. The name 'Null Island' serves as both a joke based around the suppositional existence of an island there, and also as a name to which coordinates erroneously set to 0,0 are assigned in placenames databases in order to more easily find and fix them."

    text_2 = "Presentation of Null Island.\n\
\
It's the name of a location close to the intersection of the prime meridian and the equator. It's located in international waters in the Atlantic Ocean of the Gulf of Guinea, off the west African coast. It corresponds to the coordinates (0, 0) in the WGS84 datum. At this locztion ther is a buoy. The name is both a joke and based on the hypothesis existence of an island at this point. As well, it's link to databases placenames to ease finding them."
    find_similarities(text_1, text_2)


def init_parser():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-t", "--tests", help="Run the testsuite",
                        action="store_true")
    parser.add_argument("-h", "--help",
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


def process_cmdline_args(args):
    if(args.help):
        display_help_message()  
    elif(args.tests):
        pytest.main(["-x", "tests/"])


def handle_unknown_arg_provided():
    print("Unknown args have been provided", file=sys.stderr)
    display_help_message()



if __name__ == "__main__":
    print("")
    parser = init_parser()    
    while True:
        astr = input('CheckSimilarities ')
        if('exit' in astr):
                exit()        
        ns, unknown_args = parser.parse_known_args(astr.split())        
        if unknown_args != []:
            handle_unknown_arg_provided()
        else:            
            process_cmdline_args(ns)
