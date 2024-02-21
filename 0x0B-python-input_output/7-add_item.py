#!/usr/bin/python3
"""
Script to add command-line arguments to a Python list
and save them to a JSON file.

This script imports the `sys` module to access command-line
arguments and imports the `save_to_json_file()` and
`load_from_json_file()` functions from respective Python files.

It attempts to read existing items from the file `add_item.json`.
If the file exists, the items are loaded from the file using the
`load_from_json_file()` function. If the file doesn't exist, an
empty list is used.

New items are added to the list `items` from the command-line
arguments (excluding the script name itself).

Finally, the updated list `items` is saved to the file `add_item.json`
using the `save_to_json_file()` function. If the file doesn't exist, it
will be created. If it exists, its content will be overwritten.

Usage:
    $ python script.py arg1 arg2 ...
"""
import sys

save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

try:
    items = load_from_json(file)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])

save_to_json(items, file)
