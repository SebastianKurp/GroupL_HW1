import re
import os
import locale
from graphoutline import *

locale.getpreferredencoding()
#get default encoding from local machine
#working on making this run on multiple machines, not just C9

agg_counts = {}
#put aggregate counts into dict

runnableReports = {
     "all words" : r"([A-Za-z]+)",
     "hash tags" : r"(\#\w+)",
     "dollar signs" : r"(\$\w+)",
     "numbers" : r"(\d+)",
     "unique identifiers" : r"(!\w+)",
     "mentions" : r"(\@\w+)",
     "URLS" : r"((http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?)"
}

reportChoices = ["all words", "hash tags", "dollar signs", "numbers", "unique identifiers", "mentions", "URLS", "all reports"]

#dictionary to hold the report choices (keys) and the parameters they search (values)
#URL regex was found rather than created: @https://stackoverflow.com/questions/6038061/regular-expression-to-find-urls-within-a-string

def run_keyword_type(nameOfSearch, fileText):
    search = nameOfSearch
    text = fileText
    #had to set variables otherwise considered undefined when fed as arugment
    run_report(runnableReports.get(search), search, text)

#method to find desired mentions within text parsed from file
def run_report(searchParam, nameOfSeach, fileText):
    agg_counts[nameOfSeach] = []
    #the individual keywords go into an array
    matches = re.findall(searchParam, fileText)
    for match in matches:
        agg_counts[nameOfSeach].append(match)
    
    print(str(len(agg_counts[nameOfSeach])) + " instance(s) of " + nameOfSeach +" were found in the document.")
    #the length of the array indicates how many of each type of keyword were found

directoryPath = os.path.dirname(os.path.realpath(__file__))
#returns path to directory this .py file is contained in
theOtherDirectory = directoryPath + '/TryToOpen'
#give directory you want to open


noteGraph = Graph()
#create a graph for the notes

#below code allows to open 'TryToOpen' folder and opens all files ending with .txt
def OpenDir(nameOfSeach):
    for file in os.listdir(theOtherDirectory):
        filename = os.fsdecode(file)
        if filename.endswith('.txt'):
            print("Opening and reading: " + filename)
            filePath = os.path.join(theOtherDirectory, filename)
            with open(filePath, 'r') as fileHand:
                docText = fileHand.read()
            if(nameOfSeach == "all reports"):    
                for key, value in runnableReports.items():
                    run_report(value, key, docText)
                    fileHand.close()
                    #don't hog resouces
                    continue
            else:
                run_keyword_type(nameOfSeach, docText)
        else:
            continue
       

def report_options():
    for i in range(8):
        print("[" + str(i) + "] " + str(reportChoices[i]))
    report_choice = input("What report would you like to run? ")
    return int(report_choice)



user_choice = reportChoices[report_options()]    
OpenDir(user_choice)
    
    
    
"""
Be able to report of all notes containing one or more keywords
-- bool: contains_keywords
Be able to generate a report of all notes, organized by mention
-- Aggregate count of all keyword types (@, #, !, etc) from all notes
Be able to generate a report of all keywords
-- Report count of all individual keywords
Be able to generate a report of all notes, organized by keyword
-- Report all notes, organized by agg. counts of keywords
Be able to report notes by mention/keywords selectively
-- As above, but with individually chosen keywords
Report of all notes in topological order
-- Still unclear what defines order here. First chosen file?
"""