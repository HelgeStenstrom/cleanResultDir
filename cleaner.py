#! /usr/bin/env python3

# A little program to clean among the result files that OneTE creates.

import argparse
import sys


def parse_args(args):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('resultRoot', help='The result directory that is configured in CONF GUI of OneTE.')
    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])
    rr = args.resultRoot
    print("Main called. This file was called directly")
    print("args = ", args)
    print("resultRoot = ", rr)

if __name__ == '__main__':
    main()
