#!/usr/bin/python3
""" Time for an interview!
"""
from sys import argv
import requests


if __name__ == "__main__":
    comit = requests.get(
        f'https://api.github.com/repos/{argv[1]}/{argv[2]}/commits').json()
    for commit in comit[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
