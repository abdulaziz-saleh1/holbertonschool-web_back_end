#!/usr/bin/env python3
"""
Module 10-update_topics
Contains a function to update topics of a school by name
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: pymongo collection object
        name (str): school name to update
        topics (list of str): list of topics

    Returns:
        None
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
