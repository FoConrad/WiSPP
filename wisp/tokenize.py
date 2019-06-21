# -*- coding: utf-8 -*-

"""
    tokenize.py: provides Tokenizer class and related functions
"""

import tokenize as py_tok

from typing import List

class Tokenizer(object):
    def __init__(self, file_):
        self._tokens = py_tok.tokenize(file_)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._tokens)

class IOFile(object):
    def __init__(self, file_name):
        self._file = open(file_name, 'r')

    def __call__(self):
        return bytes(self._file.readline(), 'utf-8')

    def __del__(self):
        self._file.close()

def tokenize(read_file: str) -> Tokenizer:
    return Tokenizer(IOFile(read_file))

def untokenize(tokens: List[py_tok.TokenInfo]) -> bytes:
    return py_tok.untokenize(tokens)
