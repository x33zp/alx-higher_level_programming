#!/usr/bin/python3
"""takes in a letter and sends a post req to the url,
with the letter as a parameter
"""
import requests
import sys

if __name__ == '__main__':
    q = "" if len(sys.argv) == 1 else sys.argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        res = r.json()
        if res == {}:
            print('No result')
        else:
            print('[{}] {}'.format(res.get('id'), res.get('name')))
    except ValueError:
        print('Not a valid JSON')
