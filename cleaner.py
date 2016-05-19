#! /usr/bin/env python3

# A little program to clean among the result files that OneTE creates.

import argparse
import sys
import os.path

def parse_args(args):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('resultRoot', help='The result directory that is configured in CONF GUI of OneTE.')
    return parser.parse_args(args)


def checkIsRoot(path):

    if not os.path.isdir(path):
        raise NotADirectoryError


def hasFilesOnly(path):
    return False

def main():
    args = parse_args(sys.argv[1:])
    rr = args.resultRoot
    print("Main called. This file was called directly")
    print("args = ", args)
    print("resultRoot = ", rr)

if __name__ == '__main__':
    main()
