#!/usr/bin/python3

"""
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

- The letter must be sent in the variable q
- If no argument is given, set q=""
- If the response body is properly JSON formatted and not empty,
  display the id and name like this: [<id>] <name>

- Otherwise:
  _ Display Not a valid JSON if the JSON is invalid
  _ Display No result if the JSON is empty

- You must use the package requests and sys
- You are not allowed to import packages other than requests and sys
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if not argv[1]:
        param = ""
    else:
        param = argv[1]

    payload = {"q": param}

    req = requests.post(url, data=payload)

    try:
        res = req.json()
        if res == {}:
            print("No result")
        else:
            id = res.get("id")
            name = res.get("name")
            print(f"[{id}] {name}")
    except ValueError:
        print("Not a valid JSON")
