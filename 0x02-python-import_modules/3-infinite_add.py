#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    argv_len = len(sys.argv)

    for arg in range(1, argv_len):
        sum += int(sys.argv[arg])
    print('{}'.format(sum))
