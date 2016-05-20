#!/usr/bin/env python
# encoding: utf-8

def normalize(name):
    return name.capitalize()
L1 = ['a','b','c']
L2 = list(map(normalize,L1))
print(L2)
