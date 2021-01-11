#!/usr/bin/python3
"""web scraping - request a URL
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        respo = response.read()
        print("{}".format("Body response:"))
        print("\ttype: {}".format(type(response.read())))
        print("\tcontent: {}".format(respo))
        print("\tutf8 content: {}".format(respo.decode()))
