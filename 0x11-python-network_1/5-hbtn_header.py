#!/usr/bin/python3

"""
Python script that fetches https://alx-intranet.hbtn.io/status
using requests package
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)

    XRequestId = req.headers.get("X-Request-Id")
    print(XRequestId)
