#!/usr/bin/env python3
from pymongo import MongoClient

"""script that lists all databases in MongoDB
"""


# connect to MongoDB
# assuming MongoDB is running locally on the default port
client = MongoClient('localhost', 27017)


# get the list of databases
database_names = client.list_database_names()

# print the list of databases
for db_name in database_names:
    print(db_name)

# close the connection
client.close()
