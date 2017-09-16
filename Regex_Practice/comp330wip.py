import re
import os


filehandler = open('regexpract.txt', 'r') #read the file
text = filehandler.read() #have file contents inside this var
print(text)

""" MatchObject = re.search(pattern, input_str, flags=0) """
regwordcount = 0;
searchParamRegWords = r"([A-Za-z]+)\s"
regwords = re.findall(searchParamRegWords, text)
for words in regwords:
    print(words)
    regwordcount += 1

print(str(regwordcount) + " instance(s) of all words were found in the document.")

#Finds the amount of hashtags in the text
hashcount = 0
searchParamHashtag = r"(\#\w+)" #escape out pound sign
hashtag = re.findall(searchParamHashtag, text)
for hashes in hashtag:
    hashcount += 1

print(str(hashcount) + " instance(s) of hashtags were found in the document.")

#Finds the amount of dollar signs in the text
dollarcount = 0
searchParamDollars = r"(\$\w+)" #escape out dollar symbol
dollars = re.findall(searchParamDollars, text)
for dollar in dollars:
    dollarcount += 1

print(str(dollarcount) + " instance(s) of $ were found in the document.")

#Finds and prints the number of numbers in the text
numcount = 0
searchParamNum = r"(\d+)"
nums = re.findall(searchParamNum, text)
for num in nums:
    numcount += 1

print(str(numcount) + " instance(s) of number tags were found in the document.")

#Finds number of unique identifiers in the text 
num_unique_note_id = 0
searchParamUnique = r"(!\w+)"
uniqueNotes = re.findall(searchParamUnique, text)
for note in uniqueNotes:
    num_unique_note_id += 1

print(str(num_unique_note_id) + " instance(s) of unique note identifiers were found in the document")

#Finds number of mentions in the text
num_mentions= 0
searchParamMent = r"(^@\w+)"
ment = re.findall(searchParamMent, text)
for note in ment:
    print (note)
    num_mentions += 1

print(str(num_mentions)+ " instance(s) of mentions were found in the document")

path = '/home/ubuntu/workspace/Regex_Practice/TryToOpen/openThis.txt'
print(os.path.exists(path))
print(path)

with open(path, 'r') as fileHand:
    newText = fileHand.read()

print(newText)