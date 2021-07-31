import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb

URL = 'http://mateo:couchdb@localhost:5984'
print(URL)

try:
    response = requests.get(URL)
    if response.status_code == 200:
        print('CouchDB connection: Success')
    if response.status_code == 401:
        print('CouchDB connection: failed', response.json())
except requests.ConnectionError as e:
    raise e

server=couchdb.Server(URL)
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

db_client = MongoClient('mongodb://localhost:27017')

try:
    db_client.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

db = server['tokyo2021-locations']
my_db = db_client.tokyo2021.couch1

for element in db.view('_all_docs'):
    try:
        id=element['id']
        data=db[id]
        print(data)
        my_db.insert_one(data)
    
    except Exception as e:    
        print("post not saved:" + str(e))
        
db2 = server['tokyo2021-track']
my_db2 = db_client.tokyo2021.couch2

for element in db2.view('_all_docs'):
    try:
        id=element['id']
        data=db[id]
        print(data)
        my_db2.insert_one(data)
    
    except Exception as e:    
        print("post not saved:" + str(e))
