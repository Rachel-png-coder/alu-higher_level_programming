#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get("https://api.github.com/user", auth=(username, password))
    json_res = r.json()
    print(json_res.get("id"))
