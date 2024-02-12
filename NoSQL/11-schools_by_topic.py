#!/usr/bin/env python3
"""Python function that returns the list of school having a specific topic:
    'Prototype: def schools_by_topic(mongo_collection, topic):'
    'mongo_collection' will be the 'pymongo' collection object
    'topic' (string) will be topic searched
"""


def schools_by_topic(mongo_collection, topic):
    """returns a list of schools that have a specific topic
    """
    # find documents where the 'topic' matches up...
    # ...put the name of the schools into list 'schools'
    schools = mongo_collection.find({"topics": topic})

    return schools  # returns the list of school names
