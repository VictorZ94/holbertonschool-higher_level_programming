#!/usr/bin/python3
"""web scraping - take a URL, sends a request to the URL and
   displays the body of the response
"""
import urllib.request
import sys


if __name__ == "__main__":
    args = sys.argv[1]
    try:
        with urllib.request.urlopen(args) as response:
            value = response.read()
            print("{}".format(value.decode('utf-8')))

    except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.getcode()))
