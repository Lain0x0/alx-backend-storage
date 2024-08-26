#!/usr/bin/env python3
""" Updating all with pymongo """


def update_topics(mongo_collection, name, topics):
    """ Set up variables to use with pymongo functions """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
