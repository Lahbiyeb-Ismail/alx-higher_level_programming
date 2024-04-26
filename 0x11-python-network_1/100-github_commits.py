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
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    github_api_url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    req = requests.get(github_api_url)
    res = req.json()

    for i in range(10):
        sha = res[i].get("sha")
        author_name = res[i].get("commit").get("author").get("name")
        print(f"{sha}: {author_name}")
