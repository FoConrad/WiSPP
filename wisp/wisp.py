# -*- coding: utf-8 -*-

"""
    wisp.py: provides entry point into program, and all else currently.
"""
__version__ = "0.0.1"

import sys
import ast

from .tokenize import tokenize, untokenize


def run(file_name: str) -> None:
    tokker = tokenize(file_name)
    tree = ast.parse(untokenize(list(tokker)))
    eval(compile(tree, '<tree>', mode='exec'))

def usage():
    print('python -m wisp file.py')
    sys.exit(0)

def main():
    if len(sys.argv) < 2:
        usage()
    run(sys.argv[1])
