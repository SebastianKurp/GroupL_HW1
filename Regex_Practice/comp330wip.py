import re
import os


filehandler = open('regexpract.txt', 'r') #read the file
text = filehandler.read() #have file contents inside this var

def run_report(searchParam, nameOfSeach, fileText):
    count = 0
    matches = re.findall(searchParam, fileText)
    for match in matches:
        count += 1
    print(str(count) + " instance(s) of " + nameOfSeach +" were found in the document.")

#method to find desired mentions within text parsed from file

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

directoryPath = '/home/ubuntu/workspace/Regex_Practice/TryToOpen/'
#path to TryToOpen

#below code allows to open 'TryToOpen' folder and opens all files ending with .txt
for file in os.listdir(directoryPath):
    filename = os.fsdecode(file)
    if filename.endswith('.txt'):
        print("Opening and reading: " + filename)
        filePath = os.path.join(directoryPath, filename)
        with open(filePath, 'r') as fileHand:
            docText = fileHand.read()
            for key, value in runnableReports.items():
                run_report(value, key, docText)
        continue
    else:
        continue
