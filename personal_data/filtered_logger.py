#!/usr/bin/env python3

"""filtered logger module that obfuscates data in log messages"""
import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """_summary_

    Args:
        fields (_type_): list of strings representing all 
            fields to obfuscate
        redaction (_type_): string representing by what the 
            field will be obfuscated
        message (_type_): string representing the log line
            separator (_type_): string representing by which character 
            is separating all fields in the log line
    Returns:
        _type_: the log message of obfuscated data
    """
    regex = '(' + '|'.join(fields) + r')=[^' + re.escape(separator) + r']*'
    obfuscated_message = lambda match: match.group(1) + '=' + redaction
    return re.sub(regex, obfuscated_message, message)
