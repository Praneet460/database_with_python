# importing required packages
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

# create a custom class to generate data
class Employee(object):
    def __init__(self, first, last, company, pay, night_shift = False, skills = []):
        self.first = first
        self.last = last
        self.company = company
        self.pay = pay
        self.night_shift = night_shift
        self.skills = skills

    def to_dict(self): # regular method (pass instance as the first argument)
        emp = {
            u'first': self.first,
            u'last': self.last,
            u'company': self.company,
            u'pay': self.pay,
            
        }

        if self.night_shift:
            emp[u'night_shift'] = self.night_shift
        
        if self.skills:
            emp[u'skills'] = self.skills

        return emp

    def __repr__(self): # regular method (pass instance as the first argument)
        return (
            u'Employee(first = {}, last = {}, company = {}, pay = {}, night_shift = {}, skills = {})'
            .format(self.first, self.last, self.company, self.pay, self.night_shift, self.skills)
        )

    

# create instances of the 'Employee' class
emp_1 = Employee(first = 'Praneet', last = 'Nigam', company = 'Google', pay = 50000, night_shift = True, skills = ['Python', 'C', 'R'])
emp_2 = Employee(first = 'Kartik', last = 'Shandilya', company = 'Amazon', pay = 60000, skills = ['Java', 'C'])
emp_3 = Employee(first = 'Mohit', last = 'Dubey', company = 'Internshala', pay = 50000, night_shift = True, skills = ['C'])
emp_4 = Employee(first = 'Kaushal', last = 'Chaudhary', company = 'Amazon', pay = 40000, skills = ['Java', 'C'])
emp_5 = Employee(first = 'Shubham', last = 'Nigam', company = 'Infosys', pay = 50000, night_shift= True, skills = ['C', 'Java'])


# add data to database
def add_emp_data():
    emp_ref = db.collection(u'employees')
    emp_ref.document(u'emp_1').set(emp_1.to_dict())
    emp_ref.document(u'emp_2').set(emp_2.to_dict())
    emp_ref.document(u'emp_3').set(emp_3.to_dict())
    emp_ref.document(u'emp_4').set(emp_4.to_dict())
    emp_ref.document(u'emp_5').set(emp_5.to_dict())

add_emp_data()
print("Sucessfully added to database.")

# query multiple document from the database 
## 'where' parameters -> 'a field', 'a comparision operator', 'a value'
docs = db.collection(u'employees').where(u'night_shift', u'==', True).get()
for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
print('-'*80)

docs = db.collection(u'employees').where(u'pay', u'>', 50000).get()
for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
print('-'*80)

docs = db.collection(u'employees').where(u'skills', u'array_contains', u'Java').get()
for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
print('-'*80)

docs = db.collection(u'employees').where(u'first', u'==', 'Praneet').where(u'pay', u'>', 40000).get()
for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
print('-'*80)

docs = db.collection(u'employees').order_by(u'company').limit(3).get()
for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
print('-'*80)

docs = db.collection(u'employees').order_by(u'company', direction = firestore.Query.DESCENDING).limit(3).get()
for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
print('-'*80)

docs = db.collection(u'employees').where(u'pay', u'<=', 60000).order_by(u'pay').order_by(u'first').limit(2).get()
for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))