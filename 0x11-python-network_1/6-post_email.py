#!/usr/bin/python3
"""web scraping - Usign method POST
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = requests.post(url, data=email)
    print("{}".format(data.text))
