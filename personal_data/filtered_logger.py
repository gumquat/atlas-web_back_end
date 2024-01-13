#!/usr/bin/env python3

"""filtered logger module that obfuscates data in log messages"""
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
    return re.sub(fr'(?<={separator}|^)({"|".join(fields)})={redaction}(?={separator}|$)', f'{fields[0]}={redaction}', message)
