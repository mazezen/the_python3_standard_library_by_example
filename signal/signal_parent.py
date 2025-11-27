#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import os
import signal
import subprocess
import time 
import sys

proc = subprocess.Popen(['python3', 'signal_child.py'])
print('PARENT  : Pausing before sending signal...')
sys.stdout.flush()
time.sleep(1)
print('PAREBT  : Signaling child')
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)
