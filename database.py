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
conn = pyodbc.connect ('Driver={ODBC Driver 11 for SQL Server};'
                       'Server=40.76.203.241;'
                       'Database=PODS_DB_1;'
                       'UID=deon;'
                       'PWD=project2019.;')

#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=40.76.203.241;PORT=3389;DATABASE=PODS_DB_1;UID=deon;PWD=project2019.')
cursor = conn.cursor()

'------------------Insert Into SQL Server-------------------'
text = ['If you need to add items of a list to the another list (rather than the list itself), extend() method is used']

#example of inserting to sql server
for i in text:
    word = []
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)
    word= tagged
    for i in word:
        #print(i)
        if(i[1] == 'NN' or i[1] =='NNS' or
            i[1] == 'NNP' or i[1] == 'NNPS'):
             temp = i[0]
             print(i)

             
             insertValue = (temp,0,0,0)
             cursor.execute('''
    INSERT INTO PODS_DB_1.dbo.Noun (NounDesc, Pronoun, Synonym, Language)
    VALUES(?,?,?,?)    ''' , insertValue)
             conn.commit()

cursor.execute('SELECT * FROM PODS_DB_1.dbo.Noun')

for row in cursor:
    print(row)
"""    
           
for i in text:
    if(i == 'that'):
        temp = i

        insertValue = (temp,0,0,0)
        cursor.execute('''
    INSERT INTO PODS_DB_1.dbo.Noun (NounDesc, Pronoun, Synonym, Language)
    VALUES(?,?,?,?)    ''' , insertValue)
        conn.commit()

cursor.execute('SELECT * FROM PODS_DB_1.dbo.Noun')

for row in cursor:
    print(row)
"""
