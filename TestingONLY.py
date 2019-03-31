import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
from nltk.tokenize import PunktSentenceTokenizer
from tkinter import *
from database import database
import os
from sentence import Sentence


#Menu to help user navigate through program.
def Main_Menu():
    print("---------------------------------------------------------")
    print("              Weclome to UMD ANALYTICS                   ")
    print("---------------------------------------------------------")
    print("1. Access Corpora")
    print("0. EXIT")
    print("---------------------------------------------------------")


#sub menu for user to choose (loca/web access)
def minor_menu():
    user_choice= ""
    #while loop
    print("1. Access local")
    print("2. Access Web")
    
    user_choice= input("Enter choice: ")

    if(user_choice== "1"): 
        if(read_text()=="1"):
           print("SUCCESS!")
        
    elif(user_choice=="2"):
        if(read_from_web()=="1"):
            print("SUCCESSS!")
        
    else:
        #this will be the code if user enters invalid answer, it will take them to main menu
        return "000"

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
    #Add the text sentence to the database collection
    text = Sentence(raw)
    ref = database.collection(u'sentences').add(text.to_dict())
    

    #Passing value by reference
    print_tokenizer(raw)

#Read from an online page    
def read_from_web():   
    #url= "http://www-personal.umd.umich.edu/~bmaxim/"
    url_name=input('Enter the web URL: ')
    response= request.urlopen(url_name)

    # Open the website and read the content inside the html page
    html = request.urlopen(url_name).read().decode('utf8')
    raw= response.read().decode('utf8')

    #STRIP OUT HTML
    from bs4 import BeautifulSoup
    raw= BeautifulSoup(html).get_text()
    tokens = word_tokenize(raw)

    database.collection("sentences").document(ref).collection("words").document(tokens)
    
    #Pass a variable by reference
    print_tokenizer(raw)

#Lexical diversity of text, not used yet   
def lexical_diversity(my_text_data):
    word_count = len(my_text_data)
    vocab_size = len(set(my_text_data))
    diversity_score = vocab_size / word_count
    return diversity_score

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
    
    except Exception as e:
        print(str(e))
    
    new_file.close()
#**************************************************************************


def main():
    
    #Run this to test your database connection.
    
   # test = database.collection(u'sentences').get()
    #for doc in test:
     #   print(u'{} => {}'.format(doc.id, doc.to_dict()))
    
    #This is somewhat our "main", call menu, and await for input
    user_input= ""
    while (user_input!="0"):
        Main_Menu()
        user_input=input("Select an option: ")
        if(user_input == "1"):
            if(minor_menu()=="000"):
                print("Wrong Choice!")
               # break

        elif(user_input == "0"):
            print("THANK YOU FOR USING UMD ANALYTICS")
        else:
           # print("Wrong input,please select a valid choice!")
            Main_Menu()
            user_input=input("Select an option: ")

if __name__ == "__main__":
    main()
