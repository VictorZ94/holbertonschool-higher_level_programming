#!/usr/bin/python3
"""web scraping - request headers = X-Request-Id of a URL
    with requests library
"""
import requests
import sys


url = sys.argv[1]
_request = requests.get(url)
my_header = _request.headers['X-Request-Id']
print("{}".format(my_header))
