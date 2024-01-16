#!/usr/bin/env python3

"""
hashes passwords using Bcrypt from github.com/pyca/bcrypt
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password using bcrypt with salt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if the provided password matches the hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)