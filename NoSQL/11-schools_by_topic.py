#!/usr/bin/env python3
"""
Module 11-schools_by_topic
Contains a function that finds schools by a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools that have a specific topic.

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic searched

    Returns:
        List of documents that match
    """
    return list(mongo_collection.find({ "topics": topic }))
