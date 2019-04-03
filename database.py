import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from Data_Models.word import Word
from Data_Models.sentence import Sentence

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

