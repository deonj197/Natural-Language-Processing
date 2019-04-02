import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
from nltk.tokenize import PunktSentenceTokenizer, sent_tokenize
from database import database
from nltk.corpus import gutenberg
from NLTK_Features.Read_Text import *
from NLTK_Features.Print_Text import *
from NLTK_Features.Analytics import *
from NLTK_Features.Sentiment import *
import os
from tkinter import *
from nltk.probability import FreqDist

#Menu to help user navigate through program.
def Main_Menu():
    print("---------------------------------------------------------")
    print("              Weclome to UMD ANALYTICS                   ")
    print("---------------------------------------------------------")
    print("1. Access Corpora")
    print("0. EXIT")
    print("---------------------------------------------------------")


#sub menu for user to choose (local/web access)
def minor_menu():
    user_choice= ""
    #while loop
    print("1. Access local")
    print("2. Access Web")
    print("3. From String")
    print("4. Sentence/WORD/TAG")
    
    user_choice= input("Enter choice: ")

    if(user_choice== "1"): 
        if(read_text()=="1"):
           print("SUCCESS!")
        
    elif(user_choice=="2"):
        if(read_from_web()=="1"):
            print("SUCCESSS!")

    elif(user_choice=="3"):
        if(read_from_book() == "3"):
            print("SUCCESS!")

    elif(user_choice =="4"):
        sentece_word_tag()
        
    else:
        #this will be the code if user enters invalid answer, it will take them to main menu
        return "000"
   
#Lexical diversity of text, not used yet   
##def lexical_diversity(my_text_data):
##    word_count = len(my_text_data)
##    vocab_size = len(set(my_text_data))
##    diversity_score = vocab_size / word_count
##    return diversity_score

def main():
    """
    Run this to test your database connection.
    
    test = database.collection(u'sentences').get()
    for doc in test:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
    """
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
