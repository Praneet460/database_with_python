# importing the required packages
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# path to secret key
SecretKeyPath = './secret_key/samplepythonservice-firebase-adminsdk-wr5fl-929b1aac66.json'

# use a service account
cred = credentials.Certificate(SecretKeyPath)
firebase_admin.initialize_app(cred)

db = firestore.client()

# create a new collection and document
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
}, merge = True) # merge the data in case document already exist
doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
}, merge = True)

print("Successfully written to database.")