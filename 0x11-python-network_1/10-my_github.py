#!/usr/bin/python3
"""web scraping - get URL github API
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    login = requests.get('https://api.github.com/user', auth=(username, token))
    try:
        print(login.json().get("id"))
    except:
        print("None")
