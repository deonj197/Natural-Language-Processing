import nltk
from nltk import word_tokenize
from bs4 import BeautifulSoup
from nltk.tokenize import PunktSentenceTokenizer, sent_tokenize
from database import *
from tkinter import *

def print_tokenizer(raw):
    # Using the tokenizer library and assigning it to a variable
    # This is where the text is converted and assigned to a token
    custom_sent_tokenizer = PunktSentenceTokenizer(raw)
    tokenized = custom_sent_tokenizer.tokenize(raw)
          
#******************* THIS WILL NEED TO BE MODIFIED ***********************
    # Creates an empty file
    new_file = open("myfile.txt", "w+")
    
    try:
        # For loop that will take each word and tokenize it
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            new_file.write(str(tagged)) # This will write contents to the file
            print(tagged)
            store(raw, tagged)
    
    except Exception as e:
        print(str(e))

    new_file.close()
    print(sent_tokenize(raw))
#**************************************************************************

