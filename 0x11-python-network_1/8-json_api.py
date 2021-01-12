#!/usr/bin/python3
"""web scraping - Usign method POST
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    query = ""
    if len(sys.argv) > 1:
        query = sys.argv[1]

    letter = {'q': query}
    response = requests.post(url, data=letter)
    json_response = response.json()
    try:
        if json_response:
            dict1 = json_response.values()
            dict1 = list(dict1)
            print("[{}] {}".format(dict1[0], dict1[1]))
        else:
            print("{}".format("No result"))
    except:
        print("Not a valid JSON")
