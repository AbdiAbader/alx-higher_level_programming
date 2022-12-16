#!/usr/bin/python3
""" HTTPError Handling python script
"""

import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code == 200:
        print(r.text)
    else:
        print(f'Error code: {e.status_code}')
