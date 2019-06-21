# -*- coding: utf-8 -*-

"""
    tokenize.py: provides Tokenizer class and related functions

    TODO: Deal with line continuations...
"""

# Use this to add our SPACE token
from .fix_token import token

from itertools import chain, count
from typing import List



# This class is a hack to add space tokens to the tokenized lines
class Tokenizer(object):
    def __init__(self, file_):
        self._tokens = token.tokenize(file_)
        self._cur_line = None
        self._line_toks = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._line_toks) > 0:
            ret = self._line_toks.pop(0)
            print(ret)
            return ret

        ret = next(self._tokens)
        self._cur_line = ret.start[0] # Start is (line, col)

        while ret.start[0] == self._cur_line:
            self._line_toks.append(ret)
            ret = next(self._tokens)

        # Put back first item of next line, make function if 
        # needed again
        self._tokens = chain([ret], self._tokens)

        if len(self._line_toks) > 0:
            self._add_spaces(self._line_toks[0].line)

        return next(self)

    def _add_spaces(self, line_str: str):
        started = False
        for ind in count():
            if ind >= len(self._line_toks):
                return

            tok = self._line_toks[ind]

            if tok.type == token.COMMENT:
                return
            elif tok.type in (token.INDENT, token.DEDENT):
                continue
            elif not started:
                started = True
                continue

            lt = self._line_toks[ind - 1]
            if lt.end[1] < tok.start[1]:
                newtok = token.TokenInfo(
                        token.SPACE, ' ', (lt.end[0], lt.end[1]),
                        (tok.start[0], lt.end[1]+1), tok.line)
                self._line_toks.insert(ind, newtok)


class IOFile(object):
    def __init__(self, file_name):
        self._file = open(file_name, 'r')

    def __call__(self):
        return bytes(self._file.readline(), 'utf-8')

    def __del__(self):
        self._file.close()

def tokenize(read_file: str) -> Tokenizer:
    return Tokenizer(IOFile(read_file))

