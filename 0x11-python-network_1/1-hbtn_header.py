#!/usr/bin/python3
"""a py script that send request to a URL
"""

import urllib.request as req
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = req.Request(url)

    with req.urlopen(request) as response:
        print(response.headers.get("X-Request-Id"))
