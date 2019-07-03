import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from Data_Models.word import Word
from Data_Models.sentence import Sentence
import pyodbc
import nltk
"""
In order for this to work you must install firebase_admin. Use the following command to install...

pip install --upgrade firebase-admin
"""
cred = credentials.Certificate("firebaseServiceAccountKey.json")
firebase_admin.initialize_app(cred)

database = firestore.client()

def store(raw, tagged):
    words = []
    for pair in tagged:
        word = Word(pair[0], pair[1])
        word_dict = word.to_dict()
        words.append(word_dict)

    text = Sentence(raw, words=words)
    database.collection(u'sentences').add(text.to_dict())


#https://www.microsoft.com/en-us/download/details.aspx?id=36434
conn = pyodbc.connect ('Driver={SQL Server};'
                       'Server=35.239.55.42;'
                       'Database=PODS_DB_1;'
                       'UID=analytics-admin;'
                       'PWD=project2019.;')

#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=40.76.203.241;PORT=3389;DATABASE=PODS_DB_1;UID=deon;PWD=project2019.')
cursor = conn.cursor()

'------------------Insert Into SQL Server-------------------'
#Will be called in read_text.py
def storeData(raw):
    for i in raw:
        tagWord = []
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        tagWord = tagged
        for pair in tagWord:
            if(pair[1] == 'NN' or pair[1] =='NNS' or pair[1] == 'NNP' or pair[1] == 'NNPS'):
                 tempNoun = pair[0]
                 #print(pair)
                
                 insertNoun = (tempNoun,0,0,1)
                 cursor.execute('''
        INSERT INTO PODS_DB_1.dbo.Noun (NounDesc, Pronoun, Synonym, Language)
        VALUES(?,?,?,?)    ''' , insertNoun)
                 conn.commit()

            elif(pair[1] == 'VB' or pair[1] =='VBD' or pair[1] == 'VBG' or pair[1] == 'VBN'or pair[1] == 'VBP' or pair[1] == 'VBZ'):
                 tempVerb = pair[0]
                # print(pair)
                 insertVerb = (tempVerb,0,1)
                 cursor.execute('''
        INSERT INTO PODS_DB_1.dbo.Verb (VerbDesc, Synonym, Language)
        VALUES(?,?,?)   ''' , insertVerb)
                 conn.commit()
