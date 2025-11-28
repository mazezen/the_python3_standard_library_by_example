#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import asyncio
import logging
import sys


SERVER_ADDRESS = ('localhost', 10000)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=sys.stderr,
)

log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()