#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

res = os.popen('ifconfig')
ip = re.search(
    r'inet (192.168.\d{1,3}.\d{1,3})  netmask 255.255.255.0  broadcast 192.168.1.255', res.read()).group(1)
# sock = 'http://' + ip + ':8000'

# os.system('export LS='+sock)
print(ip)
