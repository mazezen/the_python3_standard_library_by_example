#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import random
import os
import pickle

if os.path.exists('state.dat'):
    # Restore the previously saved stated.
    print('Found state.dat, initizlizing random module')
    with open('state.dat', 'rb') as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    # Use a well-known start state.
    print('No state.dat, sedding')
    random.seed(1)

# Produce random values.
for i in range(3):
    print('{:04.3f}'.format(random.random()), end=' ')
print()

# Save state for next time
with open('state.dat', 'wb') as f:
    pickle.dump(random.getstate(), f)

# Product mode random values:
print('\nAfter saveing state:')
for i in range(3):
    print('{:04.3f}'.format(random.random()), end=' ')
print()
