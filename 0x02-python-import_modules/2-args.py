#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    args = len(argv) - 1

    if args == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(args, "s" if args > 1 else ""))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
