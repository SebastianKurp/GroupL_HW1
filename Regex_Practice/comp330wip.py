import re

filename = input("Enter file: ")
filehandler = open(filename, 'r') #read the file
text = filehandler.read() #have file contents inside this var

""" MatchObject = re.search(pattern, input_str, flags=0) """
regwordcount = 0;
searchParamRegWords = r"([A-Za-z]+)\s"
regwords = re.findall(searchParamRegWords, text)
for words in regwords:
    print(words)
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
