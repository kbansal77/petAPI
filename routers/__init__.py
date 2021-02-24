import firebase_admin
from firebase_admin import auth, credentials, firestore

cred = credentials.Certificate("./pet-api-791ec-firebase-adminsdk-wm1z3-52a0dc81fa.json")
firebase_admin.initialize_app(cred)

db = firestore.client()