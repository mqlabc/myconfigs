#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyperclip import copy
from os import popen

text = popen('ssh -p6001 u0_a112@127.0.0.1' + ' termux-clipboard-get').read()
copy(text)
