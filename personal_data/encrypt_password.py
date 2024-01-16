#!/usr/bin/env python3

"""
hashes passwords using Bcrypt from github.com/pyca/bcrypt
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    hash chosen password with bcrypt *salt*
    """
    sodium_chloride = bcrypt.gensalt()  # salt haha
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), sodium_chloride)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    compare password with newly hashed password [not the same]
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
