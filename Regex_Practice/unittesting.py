import unittest

##PLEASE LOOK AT THIS...
##DO I HAVE TO IMPORT REGEX like in py., I'm guessing I have to because it wouldn't make sense otherwise...
#The baisc sudo code is 
#def test_something(self)
# make test_note="to what you're using regex for"
#self.assertEqual("to what you sent test_note")
class TestRegex(unittest.TestCase):
##These test regex
    def test_grab@(self):
        test_note = "@iliketocode"
        
        searchMentions = r"(\@\w+)"
        mentions=  re.findall(searchMentions,test_note)
        
        self.assertEquals("@iliketocode")
    
     def test_grab!(self):
        test_note = "!wowsounique"
        
        searchUniqueId =  r"(!\w+)"
        unique = re.findall(searchUniqueId, test_note)
        
        self.assertEquals("!wowsounique")
    
     def test_grabhashtag(self):
        test_note = "#Piegonshavefeelings"
        
        searchhashtags = r"(\#\w+)"
        hashtag = re.findall(searchhashtags,test_note)
        
        self.assertEquals("#Piegonshavefeelings")
    
     def test_grab$(self):
        test_note = "All I see is $signs"
        
        searchDollarSigns = r"(\$\w+)"
        doll = re.findall(searchDollarSigns,test_note)
        
        self.assertEquals("$signs")

     def test_graburls(self):
        test_note = "https://stackoverflow.com/questions/22818948/testing-regexes-in-python-using-py-test"
        
        searchurls = r"((http|https|ftp|www).+\.\w{1,4}[\/\w]{0,300}))" 
        urls = re.findall(searchParamurls,test_note)
        
        self.assertEquals("https://stackoverflow.com/questions/22818948/testing-regexes-in-python-using-py-test")

class TestOpenNotes(unittest.TestCase):
##this will test if the code can open text