#!/usr/bin/bash
# request with a header variable X-School-User-Id with the value 98
curl -sH "X-school-User-Id: 98" "$1"
