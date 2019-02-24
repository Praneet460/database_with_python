# importing required packages
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1beta1 import ArrayRemove, ArrayUnion


# path to secret key
SecretKeyPath = './secret_key/samplepythonservice-firebase-adminsdk-wr5fl-929b1aac66.json'

# use a service account
cred = credentials.Certificate(SecretKeyPath)
firebase_admin.initialize_app(cred)

db = firestore.Client()

# create a new collection and document

## create a custom class
class City(object):
    def __init__(self, name, state, country, capital=False, population=0,
                 regions=[]):
        self.name = name
        self.state = state
        self.country = country
        self.capital = capital
        self.population = population
        self.regions = regions

    @staticmethod
    def from_dict(source):
        # [START_EXCLUDE]
        city = City(source[u'name'], source[u'state'], source[u'country'])

        if u'capital' in source:
            city.capital = source[u'capital']

        if u'population' in source:
            city.population = source[u'population']

        if u'regions' in source:
            city.regions = source[u'regions']

        return city
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {
            u'name': self.name,
            u'state': self.state,
            u'country': self.country
        }

        if self.capital:
            dest[u'capital'] = self.capital

        if self.population:
            dest[u'population'] = self.population

        if self.regions:
            dest[u'regions'] = self.regions

        return dest
        # [END_EXCLUDE]

    def __repr__(self):
        return(
            u'City(name={}, country={}, population={}, capital={}, regions={})'
            .format(self.name, self.country, self.population, self.capital,
                    self.regions))

## create an instnace of a class
city = City(u'New Delhi', u'Delhi', u'India')
print(city.to_dict())

## creating a collection and add data to document
doc_ref = db.collection(u'cities').document(u'new-delhi')
doc_ref.set(city.to_dict(), merge = True)

# update the data
doc_ref.update({
    u'capital': True, 
    u'timestamp': firestore.SERVER_TIMESTAMP,
    u'regions': ['old_delhi', 'new_delhi', 'karol_bag', 'sarojni']
    })

## update the array -> add and remove
doc_ref.update({
    u'regions': ArrayUnion([u'hauz_khas'])
})

doc_ref.update({
    u'regions': ArrayRemove([u'new_delhi'])
})

# verify data added
print("Sucessfully added to database.")