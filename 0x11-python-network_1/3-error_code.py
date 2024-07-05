#!/usr/bin/python3
"""send a request and displays the body decoded in utf-8
"""

if __name__ == "__main__":
    import urllib.error as error
    import urllib.request as req
    from sys import argv

    url = argv[1]

    request = req.Request(url)

    try:
        with req.urlopen(request) as res:
            print(res.read().decode('ascii'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
