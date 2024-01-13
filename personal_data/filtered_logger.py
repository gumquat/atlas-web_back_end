#!/usr/bin/env python3

"""description text goes here"""
import logging
import re


def filter_datum(fields, redaction, message, separator):
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
    pattern = f"({separator})(?:{separator}.*{separator}|$)".join(fields)
    obfuscated_message = re.sub(pattern, redaction, message)
    return obfuscated_message
