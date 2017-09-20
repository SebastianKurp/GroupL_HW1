import unittest
import re

##PLEASE LOOK AT THIS...
##DO I HAVE TO IMPORT REGEX like in py., I'm guessing I have to because it wouldn't make sense otherwise...
#The baisc sudo code is 
#def test_something(self)
# make test_note="to what you're using regex for"
#self.assertEqual("to what you sent test_note")
class TestRegex(unittest.TestCase):
##These test regex
    def test_grabat(self):
        test_note = "@iliketocode"
        
        searchMentions = r"(\@\w+)"
        mentions=  re.search(searchMentions,test_note)
        
        self.assertRegex(test_note,searchMentions,msg="woot woot")
        
    def test_grabid(self):
        test_note = "!wowsounique"
        
        searchUniqueId =  r"(!\w+)"
        unique = re.findall(searchUniqueId, test_note)
        
        self.assertRegex(test_note,searchUniqueId,msg="Passed")

    
    def test_grabhashtag(self):
        test_note = "#Piegonshavefeelings"
        
        searchhashtags = r"(\#\w+)"
        hashtag = re.findall(searchhashtags,test_note)
        
        self.assertRegex(test_note,searchhashtags,msg="Passed")
    
    def test_grabdollarsign(self):
        test_note = "All I see is $signs"
        
        searchDollarSigns = r"(\$\w+)"
        doll = re.findall(searchDollarSigns,test_note)
        
        self.assertRegex(test_note,searchDollarSigns,msg="Passed")

    def test_graburls(self):
        test_note = "https://stackoverflow.com/questions/22818948/testing-regexes-in-python-using-py-test"
        bad_note = "h1m.bad/link#"
        
        searchurls = r"((http|https|ftp|www).+\.\w{1,4}[\/\w]{0,300})" 
        urls = re.findall(searchurls,test_note)
        
        self.assertRegex(test_note,searchurls,msg="error")
        self.assertNotRegex(bad_note,searchurls,msg="error")

if __name__ == '__main__':
    unittest.main()