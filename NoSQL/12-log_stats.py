#!/usr/bin/env python3
"""
12-log_stats.py
Provides stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Total logs
    logs_count = collection.count_documents({})
    print(f"{logs_count} logs")

    # Methods count
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check count
    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")
