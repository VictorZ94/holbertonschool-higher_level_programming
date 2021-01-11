#!/usr/bin/python3
"""web scraping - request headers = X-Request-Id of a URL
    with requests library
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    _request = requests.get(url)
    _header = _request.headers.get('X-Request-Id')
    print("{}".format(_header))
