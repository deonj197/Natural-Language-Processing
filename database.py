import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

"""
In order for this to work you must install firebase_admin. Use the following command to install...

pip install --upgrade firebase-admin
"""

cred = credentials.Certificate("firebaseServiceAccountKey.json")
firebase_admin.initialize_app(cred)

database = firestore.client()

