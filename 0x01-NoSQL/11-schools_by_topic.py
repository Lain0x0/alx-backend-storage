#!/usr/bin/env python3
""" Using mongo to return a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ Returning the list of school topics """
    return (list(mongo_collection.find({'topics': topics})))
