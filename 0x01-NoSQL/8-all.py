#!/usr/bin/env python3
""" Using pymongo to list all document in collection """


def list_all(mongo_collection):
    """ Returning a list if list in empty """
    return [docs for docs in mongo_collection.find()]
