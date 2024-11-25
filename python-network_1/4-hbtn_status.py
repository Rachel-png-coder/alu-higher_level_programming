#!/usr/bin/python3
import requests

def fetch_status():
    response = requests.get('https://alu-intranet.hbtn.io/status')
    body = response.text

    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")

if __name__ == "__main__":
    fetch_status()
