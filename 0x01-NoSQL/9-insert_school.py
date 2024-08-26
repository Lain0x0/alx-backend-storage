#!/usr/bin/env python3
""" Using pymongo to insert document in collection """

def insert_school(mongo_collection, **kwargs):
    """ Inserting based on kwargs """
    return (mongo_collection.insert_one(kwargs).inserted_id)
