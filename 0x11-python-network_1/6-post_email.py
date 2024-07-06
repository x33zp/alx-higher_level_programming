#!/usr/bin/python3
"""takes a url and email address, sends a post request and displays a response
"""
import requests
import sys

r = requests.post(sys.argv[1], data={'email': sys.argv[2]})

print(r.text)
