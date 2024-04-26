#!/usr/bin/python3

"""
Python script that takes in a URL, sends a request to
the URL and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
