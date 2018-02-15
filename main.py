#http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=en

from pymongo import MongoClient
import pprint

connection = MongoClient('homer.stuy.edu')
db = collection.stan_smith_xus #the database
#populate here
connection.add_one(events)
