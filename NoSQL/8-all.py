#!/usr/bin/env python3
"""
Module 8-all
Contains a function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list of documents, or an empty list if none.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
