#!/usr/bin/python3

"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in
the header of the response.
"""
import urllib.request


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.info().get("X-Request-Id"))
