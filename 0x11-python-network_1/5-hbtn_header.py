#!/usr/bin/python3
"""fetches a url and displays the value of
'X-Request-Id' variable in the header
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])

    print(r.headers.get('X-Request-Id'))
