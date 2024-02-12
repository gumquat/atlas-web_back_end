#!/usr/bin/env python3
"""Python function that returns the list of school having a specific topic:
    'Prototype: def schools_by_topic(mongo_collection, topic):'
    'mongo_collection' will be the 'pymongo' collection object
    'topic' (string) will be topic searched
"""


def schools_by_topic(mongo_collection, topic):
    """returns a list of schools that have a specific topic
    """
    # finds documents where the 'topic' matches
    cursor = mongo_collection.find({"topics": topic})
    # extract the school names and put it in list 'schools'
    schools = [document["name"] for document in cursor]

    return schools  # returns the list of school names
