#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

from xml.etree import ElementTree

with open('./podcasts.opml', 'rt') as f:
    tree = ElementTree.parse(f)
print(tree)

