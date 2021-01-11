#!/usr/bin/python3
"""web scraping - doing request an URL with requests method
"""
import requests


if __name__ == "__main__":
    _request = requests.get('https://intranet.hbtn.io/status')
    respon = str(_request)
    print("{}".format("Body response:"))
    print("\t- type: {}".format(type(respon)))
    print("\t- content: {}".format(_request.text))
