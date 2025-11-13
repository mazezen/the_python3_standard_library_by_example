#!/usr/bin/env python3
# encoding: utf-8

import datetime

min6 = datetime.timezone(datetime.timedelta(hours=6))
print(min6)
plus6 = datetime.timezone(datetime.timedelta(hours=6))
print(plus6)
d = datetime.datetime.now(min6)
print(d)

print(min6, ":", d)
print(datetime.timezone.utc, ":", 
      d.astimezone(datetime.timezone.utc))
print(plus6, ":", d.astimezone(plus6))

# Convert to the current system timezone.
d_system = d.astimezone()
print(d_system.tzinfo, '     :', d_system)
