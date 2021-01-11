#!/usr/bin/python3
"""web scraping - Usign method POST
"""
import requests
import sys


if __name__ == "__main__":
    url = ' http://986b2095742f.7b77981b.hbtn-cod.io:5000/search_user'
    query = ""
    try:
        query = sys.argv[1]
    except:
        pass

    response = requests.post(url, data={'q': query})
    json_response = response.json()
    try:
        if bool(json_response) is False:
            print("{}".format("No result"))
        else:
            dict1 = json_response.values()
            dict1 = list(dict1)
            print("[{}] {}".format(dict1[0], dict1[1]))
    except:
        print("{}".format("Not a valid JSON"))
