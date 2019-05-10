import nltk
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
from nltk.tokenize import PunktSentenceTokenizer, sent_tokenize
from database import database
from NLTK_Features.Print_Text import *

from tkinter import *

#Reads from inputted txt file
def read_from_book():
    raw = "is an 1851 novel by American writer Herman Melville. The book is sailor Ishmael's narrative of the obsessive quest of Ahab captain of the whaling ship Pequod for revenge on Moby Dick. the white whale that on the ship's previous voyage bit off Ahab's. leg at the knee. A contribution to the literature of the. American Renaissance. the work's genre classifications range from late Romantic to early Symbolist. Moby-Dick was published to mixed reviews was a commercial. failure and was out of print at the time of the. author's death in 1891. Its reputation as a Great American Novel was established only in the 20th century, after the centennial of its author's birth. William Faulkner confessed he wished he had written the book himself"
    raw2 = sent_tokenize(raw)
    print(raw2)


#Read from local directory
def read_text():
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
    # So maybe in here have a new window that displays file
    # With option of saving it or just viewing it
    import tkinter
    window2= Tk()
    window2.geometry("900x500")
    window2.title("Read Local File")

    Results = Label(window2, text = raw)
    Results.grid(row = 1, column = 1)
    
    #Passing values by references (goes to print sentence) and passes data there
    #print_sentence(raw)
    #print_tokenizer(raw)

    tokens = nltk.word_tokenize(raw)
    print(tokens)   

#Read from an online page    
def read_from_web():
    
    #url= "http://www-personal.umd.umich.edu/~bmaxim/"

    import tkinter
    window3= Tk()
    window3.geometry("900x500")
    window3.title("Read From Web ")

    #Info label
    label = Label(window3, text="Enter URLLL: ")
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
        from bs4 import BeautifulSoup
        raw= BeautifulSoup(html).get_text()
        tokens = word_tokenize(raw)

        #SCROLLTEXT widget
        import tkinter.scrolledtext as tkst
        scrolTxt = tkst.ScrolledText(window3)
        scrolTxt.grid(column=1,row=10)
        scrolTxt.insert(tkinter.INSERT,raw)
        #
    
        #TOKENIZE TEXT
        #Have a second scrollText?? or open in new page?? try new options
        print_tokenizer(raw)

    #Button to perform url retrieval
    option1Button = Button(window3, text= "GET WEB PAGE", bg="light blue", fg="black", command = strip)
    option1Button.grid(column=10, row =0)

    #,width=40,height=10
    
    


