#!/usr/bin/python3
"""
A Python script that takes in a URL
"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
