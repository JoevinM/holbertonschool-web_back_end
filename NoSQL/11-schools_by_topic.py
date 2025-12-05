#!/usr/bin/env python3
"""
Module that provides a function to find schools by topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return a list of schools that include a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        A list of documents matching the topic.
    """
    result = list(mongo_collection.find({"topics": topic}))
    return result
