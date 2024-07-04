#!/bin/bash
# displays only the status code of the response
curl -o /dev/null -s -w "%{http_code}\n" "$1"
