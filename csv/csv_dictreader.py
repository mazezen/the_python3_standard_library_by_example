#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import csv
import sys

with open(sys.argv[1], 'rt') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
