#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import pathlib

p = pathlib.Path('touched')

p.touch()

print('exists before removing:', p.exists())

p.unlink()

print('exists after removing:', p.exists())
