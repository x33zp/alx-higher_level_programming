#!/usr/bin/python3
"""send a post req with email as param
"""

if __name__ == "__main__":

    import urllib.request as req
    import urllib.parse as ps
    import sys

    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = ps.urlencode(values)
    data = data.encode('ascii')
    request = req.Request(url, data)
    with req.urlopen(request) as response:
        print(response.read().decode('utf-8'))
