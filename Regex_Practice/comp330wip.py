import re
import os
import locale
import collections
from graphoutline import *

locale.getpreferredencoding()
#get default encoding from local machine
#working on making this run on multiple machines, not just C9

agg_counts = {}
#put aggregate counts into dict

runnableReports = {
     "hash tags" : r"(\#\w+)",
     "dollar signs" : r"(\$\w+)",
     "unique identifiers" : r"(!\w+)",
     "mentions" : r"(\@\w+)",
     "URLS" : r"([http:\/\/|https:\/\/|ftp:\/\/|w{3}].+\.\w{1,4}[\/\w]{0,300})",
     "carots" : r"(\^\w+)"
}

reportChoices = ["hash tags", "dollar signs", "unique identifiers", "mentions", "URLS", "carots", "which notes reference other notes", "done running reports"]

#dictionary to hold the report choices (keys) and the parameters they search (values)

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
    if len(agg_counts[nameOfSeach]) > 0:
        word_array = agg_counts.get(nameOfSeach)
        for i in range(len(word_array)):
            print(word_array[i])
    #given that there are >0 matches it will print those matches for you as they stored in the array that is the value
    #connected to the key (nameOfSearch)


directoryPath = os.path.dirname(os.path.realpath(__file__))
#returns path to directory this .py file is contained in
theOtherDirectory = directoryPath + '/TryToOpen'
#give directory you want to open
notes_dictionary = collections.OrderedDict()
#keep notes in sequential order

def get_notes():
    for file in os.listdir(theOtherDirectory):
        filename = os.fsdecode(file)
        if filename.endswith('.txt'):
            print("Opening and reading: " + filename)
            filePath = os.path.join(theOtherDirectory, filename)
            with open(filePath, 'r') as fileHand:
                docText = fileHand.read()
                notes_dictionary[filename] = docText
                #key is name of note, value is the text of the document



#"unique identifiers" : r"(!\w+)",
#! is a unique identifier. Functionally the title of the note. This is written on the assumption each note can have at most 1
note_identifiers = {}

def parse_notes_for_identifiers():
    for key, val in notes_dictionary.items():
        match = re.search(r"(?<=!)(\w+)", val)
        #re.search only finds first instance
        if match != None:
            match = match.group(0)
            #search returns a object. we only need the string value of the match
            note_identifiers[key] = match
            #name of note is key, !title is the value

connections = {}
#^ are references to other notes which have the unique identifier !
def parse_notes_for_carots():
    for key, val in notes_dictionary.items():
        connections[key] = []
        matches = re.findall(r"(?<=\^)(\w+)", val)
        for match in matches:
            connections[key].append(match)
            #key is file name, append words in matches to array in value

#bang = !
def compare_carot_to_bang():
    for hashtagfilename, hashtag in connections.items():
        for uniquefilename, title in note_identifiers.items():
            if hashtag.count(title) != 0:
                print(hashtagfilename + " contains a reference to " + uniquefilename + " with the title !" + title)

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
            if(nameOfSeach == "which notes reference other notes"):
                get_notes()
                parse_notes_for_identifiers()
                parse_notes_for_carots()
                compare_carot_to_bang()
            else:
                run_keyword_type(nameOfSeach, docText)
        else:
            continue
"""
def main_searches(nameOfSeach):
    for filename, text in notes_dictionary.items():
        #val is text
        if(nameOfSeach == "all reports"):
            for typeOfSearch, searchParam in runnableReports.items():
                run_report(searchParam, typeOfSearch, text)
                fileHand.close()
                #don't hog resouces
                continue
        if(nameOfSeach == "which notes reference other notes"):
            parse_notes_for_identifiers()
            parse_notes_for_carots()
            compare_carot_to_bang()
        else:
            run_keyword_type(nameOfSeach, text)
"""
#the block above is quite broken, but Im working on it

def report_options():
    for i in range(8):
        print("[" + str(i) + "] " + str(reportChoices[i]))
    report_choice = input("What report would you like to run? ")
    try:
        return int(report_choice)
    except:
        print("Invalid choice.")
        report_options()
#prints list of options and returns as int the index to the array which holds the key values which
#can be fed to a search


while True:
    selection = report_options()
    if selection != 7:
        user_choice = reportChoices[selection]
        #feed the int returned from report_options into array reportChoices as the index. This will give back to
        #user_choice the string value from the array which matches the key in the dict runnableReports
        OpenDir(user_choice)
        #opens the directory and does regex search as key is tied to regex parameter as its value
    else:
        print("Exiting report menu. ")
        break
"""
 
get_notes()
parse_notes_for_identifiers()
parse_notes_for_carots()
compare_carot_to_bang()
    

1. Be able to report of all notes containing one or more keywords
-- bool: contains_keywords
2.  able to generate a report of all notes, organized by mention
-- Aggregate count of all keyword types (@, #, !, etc) from all notes
3. Be able to generate a report of all keywords
-- Report count of all individual keywords
4. Be able to generate a report of all notes, organized by keyword
-- Report all notes, organized by agg. counts of keywords
5. Be able to report notes by mention/keywords selectively
-- As above, but with individually chosen keywords
6. Report of all notes in topological order
-- Still unclear what defines order here. First chosen file?
"""