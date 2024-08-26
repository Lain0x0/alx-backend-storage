#!/usr/bin/env python3
""" Srting student by theer marks using pymongo """
from pymongo import MongoClient


def top_students(mongo_collection):
    """ Sorting student by marks """
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "total_score": {"$sum": "$topics.score"},
            "total_topics": {"$sum": 1}
        }},
        {"$addFields": {
            "averageScore": {"$divide": ["$total_score", "$total_topics"]}
        }},
        {"$sort": {"averageScore": -1}}
    ]

    top_ones = list(mongo_collection.aggregate(pipeline))
    return (top_ones)
