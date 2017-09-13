import re
import os

filename = input("Enter file: ")
filehandler = open(filename, 'r') #read the file
text = filehandler.read() #have file contents inside this var

""" MatchObject = re.search(pattern, input_str, flags=0) """
regwordcount = 0;
searchParamRegWords = r"([A-Za-z]+)\s"
regwords = re.findall(searchParamRegWords, text)
for words in regwords:
    regwordcount += 1

print(str(regwordcount) + " instance(s) of unmarked words were found in the document.")


hashcount = 0
searchParamHashtag = r"(\#\w+)" #escape out pound sign
hashtag = re.findall(searchParamHashtag, text)
for hashes in hashtag:
    hashcount += 1

print(str(hashcount) + " instance(s) of hashtags were found in the document.")

dollarcount = 0
searchParamDollars = r"(\$\w+)" #escape out dollar symbol
dollars = re.findall(searchParamDollars, text)
for dollar in dollars:
    dollarcount += 1

print(str(dollarcount) + " instance(s) of $ were found in the document.")

numcount = 0
searchParamNum = r"(\d+)"
nums = re.findall(searchParamNum, text)
for num in nums:
    numcount += 1

print(str(numcount) + " instance(s) of number tags were found in the document.")

num_unique_note_id = 0
searchParamUnique = r"(!\w+)"
uniqueNotes = re.findall(searchParamUnique, text)
for note in uniqueNotes:
    num_unique_note_id += 1

print(str(num_unique_note_id) + " instance(s) of unique note identifiers were found in the document")

#path = os.path.join(os.path.expanduser('~'), 'workspace', 'group_l_hw', 'Regex_Practice', 'TryToOpen', 'openThis.txt')
path = '/home/ubuntu/workspace/Regex_Practice/TryToOpen/openThis.txt'
print(os.path.exists(path))
print(path)
#The above code works on my Ubuntu VM on my laptop, but not on C9
#The below code works on my Windows machine, but also not on C9

with open(path, 'r') as fileHand:
    newText = fileHand.read()
    
lookForSuccess = r"(\w+)"
successNote = re.findall(lookForSuccess, newText)
for note in successNote:
    print(note)