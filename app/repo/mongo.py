import os
from pymongo import MongoClient

COLLECTION_NAME = 'transactions'

class MongoRepository(object):
 def __init__(self):
   mongo_url = os.environ.get('MONGO_URL')
   self.db = MongoClient(mongo_url).transactions

 def find_all(self, selector):
   return self.db.transactions.find(selector)

 def find_services(self):
    return [self.db.transactions.count_documents({'service':i}) for i in range(4)]

 def find(self, selector):
   return self.db.transactions.find_one(selector)

 def create(self, transactions):
   return self.db.transactions.insert_many(transactions)
