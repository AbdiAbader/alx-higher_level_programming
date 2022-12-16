#!/usr/bin/python3
""" HTTPError Handling python script
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        if response.code == 200:
            print(response.read().decode("utf-8"))
        else:
            print("Error code: {}".format(response.code))
