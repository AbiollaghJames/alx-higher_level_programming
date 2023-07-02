#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""


from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        file_content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(file_content)))
        print("\t- content: {}".format(file_content))
        print("\t- utf8 content: {}".format(file_content.decode('utf-8')))
