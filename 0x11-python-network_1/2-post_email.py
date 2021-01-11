#!/usr/bin/python3
"""web scraping - Using method post and requested
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        get_val = response.read()
        print(get_val.decode('utf-8'))
