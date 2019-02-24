# import required libraries
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

# path to secret key
SecretKeyPath = './secret_key/samplepythonservice-firebase-adminsdk-wr5fl-929b1aac66.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= SecretKeyPath

# use a service account
cred = credentials.Certificate(SecretKeyPath)
firebase_admin.initialize_app(cred)

db = firestore.Client()

# getting the document
doc_ref = db.collection(u'users').get()
for doc in doc_ref:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))

# deleting the document
def delete_doc():
    db.collection(u'users').document(u'aturing').delete()

# delete a specific field from the document
def delete_field():
    user_ref = db.collection(u'users').document(u'alovelace')
    user_ref.update({
        u'born': firestore.DELETE_FIELD
    })
