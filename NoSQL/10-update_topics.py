#!/usr/bin/env python3
"""
Module that updates the topics of a school document in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the list of topics for a school based on its name.
    Args:
        mongo_collection: The pymongo collection object.
        name (str): The name of the school to update.
        topics (list): The list of topics to set for the school.
    Returns:
        None
    """

    mongo_collection.update_many(
        {"name": name},
        {'$set': {"topics": topics}}
    )
