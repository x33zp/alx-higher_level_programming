#!/usr/bin/python3
"""takes in gihub credentials and displays id
"""
from requests.auth import HTTPBasicAuth
import requests
import sys

if __name__ == '__main__':
    basic_auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get('https://api.github.com/user', auth=basic_auth)

    print(r.json().get('id'))
