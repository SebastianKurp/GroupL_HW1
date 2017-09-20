import re
import os
import locale
import collections
import itertools
from collections import OrderedDict
from graphoutline import *

locale.getpreferredencoding()
#get default encoding from local machine
#working on making this run on multiple machines, not just C9

agg_counts = {}
#put aggregate counts into dict -- this holds the counts for #, !, ^, @, $, and URLs

#! is a unique identifier. Functionally the title of the note. The method is written on the assumption each note can have at most 1
note_identifiers = {}

connections = {}
#^ are references to other notes which have the unique identifier !

directoryPath = os.path.dirname(os.path.realpath(__file__))
#returns path to directory this .py file is contained in

theOtherDirectory = directoryPath + '/TryToOpen'
#assuming you cloned this, your notes should be in the TryToOpen directory

notes_dictionary = collections.OrderedDict()
#keep notes in sequential order

frequent_words = {}
#this keeps a running tally of each unique word (any old word, not just !words)

runnableReports = {
     "hash tags" : r"(\#\w+)",
     "dollar signs" : r"(\$\w+)",
     "unique identifiers" : r"(!\w+)",
     "mentions" : r"(\@\w+)",
     "URLS" : r"((http|https|ftp|www).+\.\w{1,4}[\/\w]{0,300})",
     "carots" : r"(\^\w+)",
     "most frequently used words" : r"(\w+)"
}
#((http|https|ftp|www).+\.\w{1,4}[\/\w]{0,300}) is partially working, just need to write method to merge the subgroups I thinkpython3
#This dictionary has the names of the searches which the user sees in the menu as well as the regex search parameters that the methods use

reportChoices = ["hash tags",
"dollar signs",
"unique identifiers",
"mentions",
"URLS",
"carots",
"which notes reference other notes",
"most frequently used words",
"search a specific mention, keyword, or general word",
"done running reports"]

#dictionary to hold the report choices (keys) and the parameters they search (values)

def run_keyword_type(nameOfSearch, fileText, documentName):
    search = nameOfSearch
    text = fileText
    docName = documentName
    #had to set variables otherwise considered undefined when fed as arugment
    run_report(runnableReports.get(search), search, text, docName)

#method to find desired mentions within text parsed from file
def run_report(searchParam, nameOfSeach, fileText, documentName):
    agg_counts[nameOfSeach] = []
    #the individual keywords go into an array
    matches = re.findall(searchParam, fileText)
    for match in matches:
        agg_counts[nameOfSeach].append(match)
    
    print(str(len(agg_counts[nameOfSeach])) + " instance(s) of " + nameOfSeach +" were found in " + str(documentName) + ".")
    #the length of the array indicates how many of each type of keyword were found
    if len(agg_counts[nameOfSeach]) > 0:
        word_array = agg_counts.get(nameOfSeach)
        for i in range(len(word_array)):
            print(word_array[i])
    #given that there are >0 matches it will print those matches for you as they stored in the array that is the value
    #connected to the key (nameOfSearch)

def get_notes():
    for file in os.listdir(theOtherDirectory):
        filename = os.fsdecode(file)
        if filename.endswith('.txt'):
            #print("Opening and reading: " + filename)
            #removed because looks cluttered
            filePath = os.path.join(theOtherDirectory, filename)
            with open(filePath, 'r') as fileHand:
                docText = fileHand.read()
                notes_dictionary[filename] = docText
                #key is name of note, value is the text of the document
#allows to open 'TryToOpen' folder and opens all files ending with .txt

def parse_notes_for_identifiers():
    for key, val in notes_dictionary.items():
        match = re.search(r"(?<=!)(\w+)", val)
        #re.search only finds first instance
        if match != None:
            match = match.group(0)
            #search returns a object. we only need the string value of the match
            note_identifiers[key] = match
            #name of note is key, !title is the value

def parse_notes_for_carots():
    for key, val in notes_dictionary.items():
        connections[key] = []
        matches = re.findall(r"(?<=\^)(\w+)", val)
        for match in matches:
            connections[key].append(match)
            #key is file name, append words in matches to array in value

#bang = !
def compare_carot_to_bang():
    for uniquefilename, title in note_identifiers.items():
        #for each title check to see if it exists in the list of hashtags
        for hashtagfilename, hashtag in connections.items():
            if hashtag.count(title) != 0:
                print(hashtagfilename + " contains a reference to " + uniquefilename + " with the title !" + title)
#this method looks at the results of parse_notes_for_identifiers and parse_notes_for_carots and prints the links between them

def most_frequent_words():
    for filename, text in notes_dictionary.items():
        matches = re.findall(r"(\w+)", text)
        for match in matches:
            if match in frequent_words:
                frequent_words[match] += 1
            else:
                frequent_words[match] = 1
    #sort the dictionary
    print("The top most commonly used words in all the notes are: ")
    sortedByNumHits = OrderedDict(sorted(frequent_words.items(), key=lambda t: t[1], reverse=True))
    topTenKeywords = itertools.islice(sortedByNumHits.items(), 0, 10)
    count = 1
    for word, numHits in topTenKeywords:
        print(str(count) + ". '" + str(word) + "'" + " with " + str(numHits) + " uses")
        count += 1
#this method gets ALL words and reverse sorts the OrderedDict based on number of times the word (key) was seen. It then prints the top 10.

def find_specific_word():
    basic_regex_end = ")"

    choice = input("Were you looking for a [1] mention, [2] keyword, or [3] any word? ")
    print(choice)
    if choice == "1":
        mention_regex_start = "(\@"
        mention = input("Please input the mention you are looking for (do not include the @): ")
        search_param = mention_regex_start + str(mention) + basic_regex_end
        print(search_param)
    elif choice == "2":
        hash_regex_start = "(\#"
        keyword = input("Please input the keyword you are looking for (do not include the #): ")
        search_param = hash_regex_start + str(keyword) + basic_regex_end
    elif choice == "3":
        word_start = "("
        #this is wrong, but something isn't working with re.findall when the parameter is given as a string
        word = input("Please input the word you are looking for: ")
        search_param = word_start + word + basic_regex_end
        #run_report(searchParam, nameOfSeach, fileText, documentName):
    else:
        print("Invalid choice")
        find_specific_word()
    for filename, text in notes_dictionary.items():
        re.compile(search_param)
        #make it readable for re
        matches = re.findall(search_param, text)
        for match in matches:
           print(str(match) + " was found in " + str(filename))

def main_searches(nameOfSeach):
    if(nameOfSeach == "which notes reference other notes"):
            parse_notes_for_identifiers()
            parse_notes_for_carots()
            compare_carot_to_bang()
    elif(nameOfSeach == "most frequently used words"):
            most_frequent_words()
    elif(nameOfSeach == "search a specific mention, keyword, or general word"):
        find_specific_word()
    else:
        for filename, text in notes_dictionary.items():
            #val is text
            if(nameOfSeach == "all reports"):
                for typeOfSearch, searchParam in runnableReports.items():
                    run_report(searchParam, typeOfSearch, text, filename)
                    continue
            else:
                run_keyword_type(nameOfSeach, text, filename)
    


def report_options():
    for i in range(10):
        print("[" + str(i) + "] " + str(reportChoices[i]))
    report_choice = input("What report would you like to run? ")
    try:
        return int(report_choice)
    except:
        print("Invalid choice.")
        report_options()
#prints list of options and returns as int the index to the array which holds the key values which
#can be fed to a search

get_notes()

while True:
    selection = report_options()
    if selection != 9:
        user_choice = reportChoices[selection]
        #feed the int returned from report_options into array reportChoices as the index. This will give back to
        #user_choice the string value from the array which matches the key in the dict runnableReports
        main_searches(user_choice)
        #opens the directory and does regex search as key is tied to regex parameter as its value
    else:
        print("Exiting report menu. ")
        break

"""
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