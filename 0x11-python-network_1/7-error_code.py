#!/usr/bin/python3
"""web scraping - take a URL, sends a request to the URL and
   displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    _request = requests.get(url)
    if _request.status_code == 200:
        print(_request.text)
    else:
        print("Error code: {}".format(_request.status_code))
