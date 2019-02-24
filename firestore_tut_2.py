# importing the required packages
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import google.cloud.exceptions

# path to secret key
SecretKeyPath = './secret_key/samplepythonservice-firebase-adminsdk-wr5fl-929b1aac66.json'

# use a service account
cred = credentials.Certificate(SecretKeyPath)
firebase_admin.initialize_app(cred)

db = firestore.client()

# read the data from the database
users_ref = db.collection(u'users')


# print out the data
try:
    docs = users_ref.get()
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
except google.cloud.exceptions.NotFound:
    print(u'No such document!') 