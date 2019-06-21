# -*- coding: utf-8 -*-

"""
    syn_tree.py: provides AST generation from tokens
"""

import ast
from typing import List


from .fix_token import token

def untokenize(tokens: List[token.TokenInfo]) -> bytes:
    return token.untokenize(tokens)

def token_parse(tokens: List[token.TokenInfo]) -> bytes:
    return ast.parse(untokenize(tokens))
