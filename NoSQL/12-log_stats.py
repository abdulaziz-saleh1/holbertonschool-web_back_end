#!/usr/bin/env python3
"""
12-log_stats.py
Provides stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    col = client.logs.nginx

    # total documents
    total = col.count_documents({})
    print("{} logs".format(total))

    print("Methods:")
    for m in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        cnt = col.count_documents({"method": m})
        # EXACTLY four spaces before 'method'
        print("    method {}: {}".format(m, cnt))

    # status check: method GET and path /status
    status_cnt = col.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_cnt))
