#!/usr/bin/env python3
"""
Module that provides a function to list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.
    """
    document = list(mongo_collection.find())
    return document
