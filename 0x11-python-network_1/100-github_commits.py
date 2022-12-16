#!/usr/bin/python3
""" Time for an interview!
"""
from sys import argv
import requests


if __name__ == "__main__":
    commit = requests.get(
        f'https://api.github.com/repos/{argv[1]}/{argv[2]}/commits').json()
    for i in range(10):
        print("{}: {}".format(
            commit[i].get("sha"),
            commit[i].get("commit").get("author").get("name")))
