import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
import os

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
   # corpus_root= '/Users/user/desktop/test'
    file_name= input('Enter the directory of file: ')
    corpus_root = file_name
    tokenizer = nltk.RegexpTokenizer('[^.!?]+')
    object = nltk.corpus.PlaintextCorpusReader(corpus_root, '.*\.txt', sent_tokenizer=tokenizer)
    text = object.words()
    print(text)
    return "1"

#Read from an online page    
def read_from_web():   
    #url= "http://www-personal.umd.umich.edu/~bmaxim/"
    url_name=input('Enter the web URL: ')
    response= request.urlopen(url_name)
    html = request.urlopen(url_name).read().decode('utf8')
    raw= response.read().decode('utf8')

    #STRIP OUT HTML
    from bs4 import BeautifulSoup
    raw= BeautifulSoup(html).get_text()
    tokens = word_tokenize(raw)
    
    #print(tokens)
    text= raw[:len(raw)]
    print(text)
    return "1"

#Lexical diversity of text, not used yet   
def lexical_diversity(my_text_data):
    word_count = len(my_text_data)
    vocab_size = len(set(my_text_data))
    diversity_score = vocab_size / word_count
    return diversity_score


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
    
















