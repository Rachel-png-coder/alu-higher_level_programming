#!/usr/bin/python3
"""
Python script that takes in URL, sends a request to header of the response.
"""

import urllib.request
import sys


def main():
    """
    Sends a request to a URL and displays the value
    """
    if len(sys.argv) == 2:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            headers = response.info()
            print(headers.get('X-Request-Id'))
    else:
        print("Usage: ./1-hbtn_header.py <URL>")


if __name__ == "__main__":
    main()
