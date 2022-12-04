#!/usr/bin/env python
import sys

with open('words.txt') as file:
    for line in file.readlines():
        if len(line.strip()) == int(sys.argv[1]):
            print(line.strip())
