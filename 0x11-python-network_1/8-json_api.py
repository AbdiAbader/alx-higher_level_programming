#!/usr/bin/python3
"""ython script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""


import requests
import sys

if __name__ == "__main__":
    quest = ""
    url = 'http://0.0.0.0:5000/search_user'
    if sys.argv[1]:
        quest = sys.argv[1]
    values = {"q": quest}
    r = requests.post(url, data=values)
    if r.json():
        print(f'[{r.json().get("id")}] {r.json().get("name")}')
    elif len(r.json() == 0):
        print("No result")
    else:
        print("Not a valid JSON")
