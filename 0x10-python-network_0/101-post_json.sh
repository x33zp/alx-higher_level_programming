#!/bin/bash
# sends a JSON POST request
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
