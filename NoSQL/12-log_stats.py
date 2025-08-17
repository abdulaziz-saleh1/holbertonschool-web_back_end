#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

if __name__ == "__main__":

    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_db = client.logs
    collection = logs_db.nginx

    total = collection.count_documents({})
    print("{} logs".format(total))

    print("Methods:")
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method_name in http_methods:
        method_count = collection.count_documents({"method": method_name})
        print("\tmethod {}: {}".format(method_name, method_count))

    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_count))
