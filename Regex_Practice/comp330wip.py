import re
import os
import locale
from graphoutline import *

locale.getpreferredencoding()
#get default encoding from local machine
#working on making this run on multiple machines, not just C9

agg_counts = {}
#put aggregate counts into dict

filehandler = open('regexpract.txt', 'r') #read the file
text = filehandler.read() #have file contents inside this var

#method to find desired mentions within text parsed from file
def run_report(searchParam, nameOfSeach, fileText):
    agg_counts[nameOfSeach] = []
    #the individual keywords go into an array
    matches = re.findall(searchParam, fileText)
    for match in matches:
        agg_counts[nameOfSeach].append(match)
    
    print(str(len(agg_counts[nameOfSeach])) + " instance(s) of " + nameOfSeach +" were found in the document.")
    #the length of the array indicates how many of each type of keyword were found


runnableReports = {
     "all words" : r"([A-Za-z]+)",
     "hash tags" : r"(\#\w+)",
     "dollar signs" : r"(\$\w+)",
     "numbers" : r"(\d+)",
     "unique identifiers" : r"(!\w+)",
     "mentions" : r"(\@\w+)",
     "URLS" : r"((http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?)"
}

#dictionary to hold the report choices (keys) and the parameters they search (values)

for key, value in runnableReports.items():
    run_report(value,key,text)

#URL regex was found rather than created: @https://stackoverflow.com/questions/6038061/regular-expression-to-find-urls-within-a-string

directoryPath = os.path.dirname(os.path.realpath(__file__))
#returns path to directory this .py file is contained in
theOtherDirectory = directoryPath + '/TryToOpen'
#give directory you want to open


noteGraph = Graph()
#create a graph for the notes

#below code allows to open 'TryToOpen' folder and opens all files ending with .txt
for file in os.listdir(theOtherDirectory):
    filename = os.fsdecode(file)
    if filename.endswith('.txt'):
        #noteGraph.addVertex(filename)
        print("Opening and reading: " + filename)
        filePath = os.path.join(theOtherDirectory, filename)
        with open(filePath, 'r') as fileHand:
            docText = fileHand.read()
            for key, value in runnableReports.items():
                run_report(value, key, docText)
            fileHand.close()
            #close the file when done with it, save resources, etc etc
        continue
    else:
        continue

    
    
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