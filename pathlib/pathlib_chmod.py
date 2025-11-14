#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import os
import pathlib
import stat

# Create a fresh test file.
f = pathlib.Path('pathlib_chmod_example.txt')
if f.exists():
    f.unlink()
f.write_text('contents')

# Determine which permissions are already set using stat.
existing_permissions = stat.S_IMODE(f.stat().st_mode)
print('Before: {:o}'.format(existing_permissions))

# Decide which way to toggle them.
if not (existing_permissions & os.X_OK):
    print('Adding execute permission')
    new_perssions = existing_permissions | stat.S_IXUSR
else:
    print('Removing execute permission')
    # Use xor to remove the user execute permission.
    new_perssions = existing_permissions ^ stat.S_IXUSR

# Make the change and show the new value.
f.chmod(new_perssions)
after_permissions = stat.S_IMODE(f.stat().st_mode)
print('After: {:0}'.format(after_permissions))
