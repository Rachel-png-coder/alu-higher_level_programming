#!/usr/bin/python3
"""
A Python script that takes in a URL
"""

import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
