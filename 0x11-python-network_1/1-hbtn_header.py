#!/usr/bin/python3
"""web scraping - request headers = X-Request-Id of a URL
"""
import urllib.request
import sys


if __name__ == "__main__":
    args = sys.argv[1]
    with urllib.request.urlopen(args) as response:
        header = response.getheader('X-Request-Id')
        print("{}".format(header))
