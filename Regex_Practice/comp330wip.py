import re

filename = input("Enter file: ")
filehandler = open(filename, 'r') #read the file
text = filehandler.read() #have file contents inside this var

""" MatchObject = re.search(pattern, input_str, flags=0) """
searchParamJabberwocky = r"(J\w+)\s"
jabs = re.search(searchParamJabberwocky, text)
print(jabs.group(0))

searchParamHashtag = r"(\#\w+)" #escape out pound sign
hashtag = re.search(searchParamHashtag, text)
print(hashtag.group(0))

searchParamDollars = r"(\$\w+)" #escape out dollar symbol
dollars = re.search(searchParamDollars, text)
print(dollars.group(0))

searchParamNum = r"(\d+)"
nums = re.search(searchParamNum, text)
print(nums.group(0))
