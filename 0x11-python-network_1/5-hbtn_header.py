#!/usr/bin/python3
"""fetches a url and displays the value of 'X-Request-Id' variable in the header
"""
import requests
from sys import argv

r = requests.get(argv[1])

print(r.headers.get('X-Request-Id'))
