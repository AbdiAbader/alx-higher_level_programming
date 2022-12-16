#!/usr/bin/python3
""" HTTPError Handling python script
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as res:
        print("Error code: {}".format(res.code))
