#!/usr/bin/env python3
# Web scraping by Avinash on Udemy

import re
import urllib.request

try:
    url = "http://dictionary.reference.com/browse/"
    
    word = input("Enter your word: ")# enter a word that needs to be defined
    
    url = url + word# updating url
    
    data = urllib.request.urlopen(url).read()
    data1 = data.decode("utf-8")
    
    m = re.search('meta name="description" content="', data1)
    start = m.end()
    end = start + 300
    
    newString = data1[start: end]
    
    m = re.search("See more.", newString)
    end = m.start() - 1
    
    definition = newString[0:end]
    
    print(definition)
    
except:
    print("I'm sorry, your word is not in the dictionary.")