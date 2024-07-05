#!/usr/bin/python3
"""takes a url and email, sends POST request with an
email param and displays a body of the response
"""
if __name__ == "__main__":
    import urllib.request as req
    import urllib.parse as ps
    import sys

    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    url_values = ps.urlencode(data).encode("ascii")

    request = req.Request(url, data)

    with req.urlopen(request) as response:
        print(response.read().decode("utf-8"))
