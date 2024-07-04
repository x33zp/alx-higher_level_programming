#!/bin/bash
# sends a POST req
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
