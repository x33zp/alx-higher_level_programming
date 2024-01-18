#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for names in hidden_4:
        if names[:2] != '__':
            print(dir(hidden_4))
