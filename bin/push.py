#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyperclip import paste
from os import system

text = r"'" + paste() + "'"
system('ssh -p6001 u0_a112@127.0.0.1' + ' "termux-clipboard-set ' + text+'"')
print('content of your clipboard:')
print('ssh -p8022 handsome@x.x.x.x' + ' termux-clipboard-set ' + text)
