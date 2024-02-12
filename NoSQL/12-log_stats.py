#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB:
Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the...
...method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
one line with the number of documents with:
method=GET
path=/status
"""

import pymongo
from pymongo imoprt MongoClient


def statLog():
    # bruh