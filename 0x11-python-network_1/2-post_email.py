#!/usr/bin/python3

""""""

import urllib.parse
import urllib.request

if __name__ == "__main__":
    from sys import argv

    url = argv[1]
    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode("utf-8"))
