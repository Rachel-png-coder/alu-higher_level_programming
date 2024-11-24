#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    # Get the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the POST data
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    # Send the POST request
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode("utf-8"))
