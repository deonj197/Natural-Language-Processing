import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
from nltk.tokenize import PunktSentenceTokenizer, sent_tokenize
from database import database
from nltk.corpus import gutenberg
import os
from tkinter import *
from nltk.probability import FreqDist
from NLTK_Features.Read_Text import *
from NLTK_Features.Print_Text import *


def sentece_word_tag():

    import nltk
    from nltk.corpus import PlaintextCorpusReader

    # Open From File GUI
    from tkinter.filedialog import askopenfilename

    # This will hide the tk window and exit out of it once program is terminated
    root = Tk()
    root.withdraw()

    # Opens windows explorer
    file_name = askopenfilename()
    f = open(file_name)
    
    # Read from file
    raw=f.read()

    print("-----------------Sentence tokenization------------------- \n")
    sentences = nltk.sent_tokenize(raw)
    print(sentences)
    print("\n-----------------Word tokenization----------------------------------\n")
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    print(sentences)
    print("\n----------------WORDS + TAG-----------------------------------\n")
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    print(sentences)   

    Stats_Menu()

def Stats_Menu():
    print("-------------------------------------------------------- -")
    print("                       ANALYTICS                          ")
    print("----------------------------------------------------- ----")
    print("1. FREQUENCY DISTRIBUTION                                 ")
    print("2. STOP WORDS                                             ")
    print("3. STEMMING                                               ")
    
    print("0. EXIT")
    print("----------------------------------------------------------")
    user_choice= input("Enter choice: ")

    if(user_choice== "1"):
        freq_Dist()
       
        #if(freq_Dist()=="0"):
           #print("SUCCESS!")
    if(user_choice=="2"):
        stop_words()
    if(user_choice=="3"):
        stemming()
        
    else:
        #this will be the code if user enters invalid answer, it will take them to main menu
        return "111"
#Stemming reduces a word to its simpleset form
#for example driving, drove, would reduce to drive   
def stemming():
    
    from nltk.stem import PorterStemmer
    from nltk.tokenize import sent_tokenize, word_tokenize

    #Open file
    from nltk.corpus import PlaintextCorpusReader

    # Open From File GUI
    from tkinter.filedialog import askopenfilename

    # This will hide the tk window and exit out of it once program is terminated
    root = Tk()
    root.withdraw()

    # Opens windows explorer
    file_name = askopenfilename()
    f = open(file_name)
    
    # Read from file
    raw=f.read()
    
    sentences = nltk.word_tokenize(raw)
    ps = PorterStemmer()
    stemmed_words=[]
    for w in sentences:
        
        stemmed_words.append(ps.stem(w))
                             
    print("ORGINAL Sentencs:",sentences)
    print("Stemmed Sentence:",stemmed_words)

#Remove stop words (in english stop words, are words that connect words,
#but alone give no significant meaning to a sentece
def stop_words():
                             
    #jsut have a function that can remember the name of the file, instead of always
    #opening the file
    print("LIST OF STOP WORDS\n")
    from nltk.corpus import stopwords
    stop_words=set(stopwords.words("english"))
    print(stop_words)
    print("REMOVING STOP WORDS FROM THE TEXT\n")

    #Open file
    from nltk.corpus import PlaintextCorpusReader

    # Open From File GUI
    from tkinter.filedialog import askopenfilename

    # This will hide the tk window and exit out of it once program is terminated
    root = Tk()
    root.withdraw()

    # Opens windows explorer
    file_name = askopenfilename()
    f = open(file_name)
    
    # Read from file
    raw=f.read()
    
    sentences = nltk.word_tokenize(raw)

    missing_words =[]
    unfiltered = []
    for w in sentences:
        unfiltered.append(w)
    
    filtered_sent=[]
    for w in sentences:
        if w not in stop_words:
            filtered_sent.append(w)


    #ORIGINAL TEXT
    print ("TOTAL # OF WORDS =", len([word for s in sentences for word in s]))
    print("ORIGINAL Tokenized Sentence:",sentences)

    #FILTERED VERESION
    print ("TOTAL # OF WORDS =", len([word for s in filtered_sent for word in s]))
    print("FILETERED  Sentence:",filtered_sent)
    

    #CHECK WHAT WORDS HAVE BEEN 
    print("UNFILTERED: ", unfiltered)

    for w in unfiltered:
        if w not in filtered_sent:
            missing_words.append(w)
    print("MIssing words", missing_words)
            
   
#Will check the word distribution, how often does a particular word occur
def freq_Dist():

    import nltk
    from nltk.corpus import PlaintextCorpusReader

    # Open From File GUI
    from tkinter.filedialog import askopenfilename

    # This will hide the tk window and exit out of it once program is terminated
    root = Tk()
    root.withdraw()

    # Opens windows explorer
    file_name = askopenfilename()
    f = open(file_name)
    
    # Read from file
    raw=f.read()
    #tokenized_text=sent_tokenize(raw)
    tokenized_word=word_tokenize(raw)
    fdist = FreqDist(tokenized_word)
    #print(fdist)
    #fdist.most_common(2)
    
   #import matplotlib.pyplot as plt
    fdist.plot(30,cumulative=False)
    plt.show()    
    
