#!/usr/bin/python3
"""web scraping - request a URL
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        respo = response.read()
        print("{}".format("Body response:"))
        print("\t- type: {}".format(type(response.read())))
        print("\t- content: {}".format(respo))
        print("\t- utf8 content: {}".format(respo.decode()))
