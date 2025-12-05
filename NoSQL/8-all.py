#!/bin/bin/env python3
"""
Module that provides a function to list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
    mongo_collection: pymongo collection object

    Returns:
    List of documents (empty list if no document exists)
    """
    document = list(mongo_collection.find())
    return document
