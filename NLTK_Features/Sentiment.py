import nltk
from nltk import word_tokenize
from bs4 import BeautifulSoup
from nltk.tokenize import PunktSentenceTokenizer, sent_tokenize
from database import database
from NLTK_Features.Read_Text import *
from NLTK_Features.Print_Text import *
from NLTK_Features.Analytics import *
from tkinter import *
from nltk.probability import FreqDist

#SENTIMENT ANALYSIS DONE WITH TEXTBLOB (in order for this to run on your machine)
    #run on CMD the following command
    #                                 pip install -U textblob  
def sentiment_analysis():
#STEP 1: READ FILE    
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
    
#STEP 2: DIVIDE TEXT INTO SENTENCES
    from textblob import TextBlob
    s = TextBlob(raw)
    
#STEP 3: DETERMINE WHEATHER THE SENTENCE IS POSITIVE OR NEGATIVE
    num=1
    for sentence in s.sentences:
        print(num, " ", sentence)
        print(sentence.sentiment)
#STEP 4: PRINT SENTENCE + SCORE
        if(sentence.sentiment.polarity>0):
            print ('Score: positive')
        elif(sentence.sentiment.polarity==0):
                  print('Score: neutral')
        elif(sentence.sentiment.polarity<0):
                        print('Score: negative!')
        
        print(" ")
        num=num+1
