import unittest
import argparse
import sys
from comp330wip import *


class TestReportFunctionality(unittest.TestCase):
    def test_report_options(self):
        self.assertEqual(report_options(), "all words")
        #this is wrong
        #https://stackoverflow.com/questions/1029891/python-unittest-is-there-a-way-to-pass-command-line-options-to-the-app
        #not familiar with python unit testing
        #but this is actually running the program somehow when it should only be returning a string
        #it's also checking my command line entry for the equality instead of the returned value of report_options()
        
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='My Input')
    parser.add_argument('filename', default='some_file.txt')
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()

    # Now set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
    sys.argv[1:] = args.unittest_args
    unittest.main()
    
#I have no idea why this is looping
#to run: python3 testing.py TestReportFunctionality.test_report_options