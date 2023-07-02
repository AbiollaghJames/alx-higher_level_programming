#!/usr/bin/python3
"""
  a Python script that fetches https://alx-intranet.hbtn.io/status
    - You must use the package requests
"""


import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
