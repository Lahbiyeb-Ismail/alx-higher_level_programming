#!/usr/bin/python3

"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id

- You must use Basic Authentication with a personal access token as password
to access to your information (only read:user permission is needed)

- The first argument will be your username

- The second argument will be your password (in your case, a personal access
  token as password)

- You must use the package requests and sys

- You are not allowed to import packages other than requests and sys

- You don’t need to check arguments passed to the script (number or type)
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    github_api_url = "https://api.github.com/user"
    github_username = argv[1]
    github_pass = argv[2]

    basic = HTTPBasicAuth(github_username, github_pass)

    req = requests.get(github_api_url, auth=basic)
    user_id = req.json().get("id")

    print(user_id)
