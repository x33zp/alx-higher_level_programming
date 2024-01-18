#!/usr/bin/python3
import sys
argv = sys.argv
argv_len = len(sys.argv) -1

if argv_len == 0:
    print('{} arguments.'.format(argv_len))
elif argv_len == 1:
    print('{} argument:'.format(argv_len))
else:
    print('{} arguments:'.format(argv_len))

for arg in range(argv_len):
    if argv_len > 0:
        print('{}: {}'.format(arg + 1, argv[arg + 1]))
