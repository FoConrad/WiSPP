# -*- coding: utf-8 -*-

"""
    fix_token.py: Fixes issues with missing tokens across python version

"""

import tokenize as token

token.SPACE = 67 # Check Lib/token.py for free numbers
token.tok_name[67] = 'SPACE'

token.EXACT_TOKEN_TYPES[' '] = token.SPACE

__all__ = ["token"]
