from IA.check_plagiarism import find_similarities
import pytest
import argparse


def test():
    text_1 = "Null Island\n\
\
Null Island is a name for the area around the point where the prime meridian and the equator cross, located in international waters in the Gulf of Guinea (Atlantic Ocean) off the west African coast.[1] In the WGS84 datum, this is at zero degrees latitude and longitude (0°N 0°E), and is the location of a buoy. The name 'Null Island' serves as both a joke based around the suppositional existence of an island there, and also as a name to which coordinates erroneously set to 0,0 are assigned in placenames databases in order to more easily find and fix them."

    text_2 = "Presentation of Null Island.\n\
\
It's the name of a location close to the intersection of the prime meridian and the equator. It's located in international waters in the Atlantic Ocean of the Gulf of Guinea, off the west African coast. It corresponds to the coordinates (0, 0) in the WGS84 datum. At this locztion ther is a buoy. The name is both a joke and based on the hypothesis existence of an island at this point. As well, it's link to databases placenames to ease finding them."
    find_similarities(text_1, text_2)


def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tests", help="Run the testsuite",
                        action="store_true")
    return parser


def parse_cmdline_args():
        
    args = parser.parse_args()
    return args

def process_cmdline_args(args):
    if(args.tests):
        pytest.main(["-x", "tests/"])
        exit()
    



if __name__ == "__main__":
    parser = init_parser()
    while True:
        astr = input('$: ') 
        try:
            args = parser.parse_args(astr.split())
            if('exit' in args):
                exit()
            process_cmdline_args()
        except SystemExit:
            # trap argparse error message
            print('error')
            continue



