#!/usr/bin/env python3
"""
Module that inserts a document into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on kwargs.
    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Fields of the document to insert.
    Returns:
        The _id of the inserted document.
    """

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
