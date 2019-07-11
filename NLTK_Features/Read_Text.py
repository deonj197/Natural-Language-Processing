from database import database
import nltk
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
from nltk.tokenize import PunktSentenceTokenizer, sent_tokenize
from NLTK_Features.Print_Text import *
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText 
from nltk.corpus import PlaintextCorpusReader  
# Open From File GUI
from tkinter.filedialog import askopenfilename
import tkinter.scrolledtext as tkst
from tkinter import *
import tkinter

#Reads from inputted txt file
def read_from_book():
    raw = "is an 1851 novel by American writer Herman Melville. The book is sailor Ishmael's narrative of the obsessive quest of Ahab captain of the whaling ship Pequod for revenge on Moby Dick. the white whale that on the ship's previous voyage bit off Ahab's. leg at the knee. A contribution to the literature of the. American Renaissance. the work's genre classifications range from late Romantic to early Symbolist. Moby-Dick was published to mixed reviews was a commercial. failure and was out of print at the time of the. author's death in 1891. Its reputation as a Great American Novel was established only in the 20th century, after the centennial of its author's birth. William Faulkner confessed he wished he had written the book himself"
    raw2 = sent_tokenize(raw)
    print(raw2)


#****************************** READ FROM LOCAL FILE **************************************
#Read from local directory
def read_text():
    #just have a function that can remember the name of the file, instead of always
    #opening the file
    window= Tk()
    window.geometry("900x500")
    window.title("WORDS TAGGING FUNCTION")

    nb = ttk.Notebook(window)

    page1 = ttk.Frame(nb)
    page2 = ttk.Frame(nb)
    page3 = ttk.Frame(nb)
    #page4 = ttk.Frame(nb)
    
    nb.add(page1, text = 'Sentence tokenization')
    nb.add(page2, text= 'Word tokenization')
    nb.add(page3, text='WORDS TAGGING')
    #nb.add(page4, test='Names')

    nb.pack(expand=1, fill="both")
   
    monty = ttk.LabelFrame(page1, text=' ORIGINAL SENTENCE ')
    monty.grid(column=0, row=0, padx=8, pady=4)

    monty2 = ttk.LabelFrame(page2, text=' WORD　TOKENIZATION')
    monty2.grid(column=0, row=0, padx=8, pady=4)

    monty3 = ttk.LabelFrame(page3, text=' WORDS TAGGING')
    monty3.grid(column=0, row=0, padx=8, pady=4)

    #monty4 = ttk.LabelFrame(page3, text=' NAMES ')
    #monty4.grid(column=0, row=0, padx=8, pady=4)

    # This will hide the tk window and exit out of it once program is terminated
    root = Tk()
    root.withdraw()

    # Opens windows explorer
    file_name = askopenfilename()
    f = open(file_name)
    
    # Read from file
    raw=f.read()
    
    sentences = nltk.sent_tokenize(raw)
     #ORIGINAL TEXT
    totL = ("TOTAL WORDS COUNTS =", len([word for s in sentences for word in s]), "\n")
    scrolTxt2 = tkst.ScrolledText(monty, width=100, height=30, wrap=tk.WORD)
    #scrolTxt.grid(column=0, row=3, sticky='WE', columnspan=3)
    scrolTxt2.grid(column=1,row=3)
    scrolTxt2.insert(tkinter.INSERT,totL)
    scrolTxt2.insert(tkinter.INSERT,sentences)

    #WORD TOKENIZED VERESION
    # print ("TOTAL # OF WORDS =", len([word for s in filtered_sent for word in s]))
    #print("FILETERED  Sentence:",filtered_sent)
    wordTokenized = [nltk.word_tokenize(sent) for sent in sentences]
    totL3=("WORDS TOKENIZED =", len([word for s in wordTokenized for word in s]), "\n") 
    scrolTxt3 = tkst.ScrolledText(monty2, width=100, height=30, wrap=tk.WORD)
    scrolTxt3.grid(column=1,row=3)
    scrolTxt3.insert(tkinter.INSERT,totL3, '\n')
    scrolTxt3.insert(tkinter.INSERT,wordTokenized)
    
    wordTag = [nltk.pos_tag(sent) for sent in wordTokenized]
    totL3=("WORDS TAGGING =", len([word for s in wordTag  for word in s]), "\n") 
    scrolTxt3 = tkst.ScrolledText(monty3, width=100, height=30, wrap=tk.WORD)
    scrolTxt3.grid(column=1,row=3)
    scrolTxt3.insert(tkinter.INSERT,totL3)
    scrolTxt3.insert(tkinter.INSERT,wordTag )
    tokens = nltk.word_tokenize(raw)
   #print(tokens)   
    storeData(tokens)

#***************************** END OF READ FROM LOCAL ********************************

    
#***************************** READ FROM WEB *****************************************
#Read from an online page    
def read_from_web():
    
    #url= "http://www-personal.umd.umich.edu/~bmaxim/"
    window3= Tk()
    window3.geometry("900x500")
    window3.title("Read From Web ")

    # This will hide the tk window and exit out of it once program is terminated
    root = Tk()
    root.withdraw()

    #Info label
    label = Label(window3, text="Enter Web Page URL: ")
    label.grid(column = 0, row = 0)

    #User Input
    txt = Entry(window3,width=50)
    txt.grid(column = 1, row =0)
    txt.focus()

    def strip():
        #url_name=input('Enter the web URL: ')
        url_name = txt.get()
        response= request.urlopen(url_name)

        # Open the website and read the content inside the html page
        html = request.urlopen(url_name).read().decode('utf8')
        raw= response.read().decode('utf8')

        #STRIP OUT HTML
        raw= BeautifulSoup(html).get_text()
        tokens = word_tokenize(raw)

        #SCROLLTEXT widget
        scrolTxt = tkst.ScrolledText(window3)
        #scrolTxt.grid(column=1,row=10)
        #scrolTxt.insert(tkinter.INSERT,raw)
  
        #TOKENIZE TEXT
        #Have a second scrollText?? or open in new page?? try new options
        #print_tokenizer(raw)
    
        print("\n----------------WORDS + TAG-----------------------------------\n")
        sentences = nltk.sent_tokenize(raw)
        wordTokenized = [nltk.word_tokenize(sent) for sent in sentences]
        wordTag = [nltk.pos_tag(sent) for sent in wordTokenized]
        print(wordTag )
        totL3=("WORDS TAGGING =", len([word for s in wordTag  for word in s]), "\n") 
        #scrolTxt = tkst.ScrolledText(monty3, width=100, height=30, wrap=tk.WORD)
        scrolTxt.grid(column=1,row=3)
        scrolTxt.insert(tkinter.INSERT,totL3)
        scrolTxt.insert(tkinter.INSERT,wordTag )
        

    #Button to perform url retrieval
    option1Button = Button(window3, text= "GET WEB PAGE", bg="light blue", fg="black", command = strip)
    option1Button.config(height = 1, width = 20)
    option1Button.grid(column=10, row =0)

    print_tokenizer(raw)
    tokens = nltk.word_tokenize(raw)   
    storeData(tokens)
#*******************=************** END OF READ FROM WEB **************************************
    
