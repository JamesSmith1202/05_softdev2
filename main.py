from pymongo import MongoClient
import pprint

connection = MongoClient('homer.stuy.edu')
db = collection.stan_smith_xus #the database
#populate here
connection.add_one(events)