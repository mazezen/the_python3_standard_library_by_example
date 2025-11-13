#!/usr/bin/env python3
# encoding: utf-8


import calendar

c = calendar.LocaleTextCalendar(locale='en_US')
c.prmonth(2025, 11)

print()

c = calendar.LocaleTextCalendar(locale='fr_FR')
c.prmonth(2025, 11)

c = calendar.LocaleTextCalendar(locale='zh_CN')
c.prmonth(2025, 11)
