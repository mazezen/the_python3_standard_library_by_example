#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

from xml.etree import ElementTree

with open('data.xml', 'rt') as f:
    tree = ElementTree.parse(f)

node = tree.find('entity_expansion')
print(node.tag)
print(' in attribute:', node.attrib['attribute'])
print(' in text :', node.text.strip())
