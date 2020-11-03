#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
__version__     =   "0.0.1"
__author__      =   "@lantip"
__date__        =   "2020/11/03"
__description__ =   "Kitinyi Giniritir"
"""

import sys
import argparse
from itertools import cycle
import json


case = cycle(["lower", "upper"])

def bikin(text):    
    generated = ""
    for char in text:
        generated += getattr(char, next(case))()

    vow_num = {'a': 4, 'A': 4, 'e': 3, 'E': 3, 'i': 1, 'I': 1, 'o': 0, 'O': 0, 'u': 7, 'U': 7}
    replaced = ""
    for i in range(len(generated)):
        letter = generated[i]
        if letter in vow_num:
            letter = vow_num[letter]
        replaced += str(letter)

    vow_i = {'a': 'i', 'A': 'I', 'e': 'i', 'E': 'I', 'i': 'i', 'I': 'I', 'o': 'i', 'O': 'I', 'u': 'i', 'U': 'I'}
    nyinyir = ""
    for i in range(len(generated)):
        letter = generated[i]
        if letter in vow_i:
            letter = vow_i[letter]
        nyinyir += str(letter)

    kipitil = ""

    for i in range(len(nyinyir)):
        letter = nyinyir[i]
        if letter in vow_num:
            letter = vow_num[letter]
        kipitil += str(letter)
    

    return {
        'tiren': generated,
        'alay': replaced,
        'nyinyir': nyinyir.lower(),
        'kipitil': kipitil
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.MetavarTypeHelpFormatter, description='''Kitinyi Giniritir''')

    parser.add_argument('-t', '--text', type=str, help="Text yang ingin diubah", required=True)

    args = parser.parse_args()
    text = args.text
    ubah = bikin(text)
    print(json.dumps(ubah, indent=4))
