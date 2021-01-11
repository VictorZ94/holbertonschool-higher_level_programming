#!/usr/bin/python3
"""web scraping - request headers = X-Request-Id of a URL
    with requests library
"""
import requests


if __name__ == "__main__":
    _request = requests.get('https://intranet.hbtn.io/status')
    _header = _request.headers['X-Request-Id']
    print("{}".format(_header))
