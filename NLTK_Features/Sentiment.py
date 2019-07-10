from database import database
import nltk
from nltk import word_tokenize
from bs4 import BeautifulSoup
from nltk.tokenize import PunktSentenceTokenizer, sent_tokenize
#from database import database
from NLTK_Features.Read_Text import *
from NLTK_Features.Print_Text import *
from NLTK_Features.Analytics import *
from tkinter import *

#SENTIMENT ANALYSIS DONE WITH TEXTBLOB (in order for this to run on your machine)
    #run on CMD the following command
    #                                 pip install -U textblob  
def sentiment_analysis():
    window5= Tk()
    window5.geometry("900x500")
    window5.title("Sentiment Analysis")

    nb = ttk.Notebook(window5)
    page1 = ttk.Frame(nb)

    nb.add(page1, text='Sentiments')
    nb.pack(expand=1, fill="both")

    monty = ttk.LabelFrame(page1, text='Sentiments')
    monty.grid(column=0, row=0, padx=8, pady=4)

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

# Set up the scroll text
    from tkinter.scrolledtext import ScrolledText
    scrolTxt = tkst.ScrolledText(monty, width=100, height=30)
    scrolTxt.grid(column=1,row=3)
    
#STEP 3: DETERMINE WHEATHER THE SENTENCE IS POSITIVE OR NEGATIVE
    num=1
    for sentence in s.sentences:
        print(num, " ", sentence)
        step1 = (num, " ", sentence)
        scrolTxt.insert(tkinter.INSERT,step1)
        
        print(sentence.sentiment)
        step2 = ('\n', "Sentiment", sentence.sentiment)
        scrolTxt.insert(tkinter.INSERT, step2)
        
#STEP 4: PRINT SENTENCE + SCORE
        if(sentence.sentiment.polarity>0):
            print ('Score: positive')
            step3 = ('\nScore: positive\n')
            scrolTxt.insert(tkinter.INSERT,step3)
        elif(sentence.sentiment.polarity==0):
                  print('Score: neutral')
                  step4 = ('\nScore: neutral\n')
                  scrolTxt.insert(tkinter.INSERT,step4)
        elif(sentence.sentiment.polarity<0):
                        print('Score: negative!')
                        step5 = ('\nScore: negative!\n')
                        scrolTxt.insert(tkinter.INSERT,step5)
        
        print(" ")
        step6 = ("\n")
        scrolTxt.insert(tkinter.INSERT,step6)
        num=num+1

    window5.mainloop()
