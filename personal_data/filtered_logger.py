#!/usr/bin/env python3

"""filtered logger module that obfuscates data in log messages"""
import logging
import re
from typing import List


def replace_field(match, redaction):
    """to appease pycodestyle"""
    return match.group(1) + '=' + redaction


def filter_datum(
                fields: List[str], redaction: str, message: str, separator: str
                ) -> str:
    """obfuscate fields in log messages

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
    pattern = (
        '(' + '|'.join(fields) +
        r')=[^' + re.escape(separator) + r']*'
    )
    return re.sub(
        pattern,
        lambda match: replace_field(match, redaction),
        message
    )

def get_logger() -> logging.Logger:
    """
    Logger 'user_data'
    """
    """Logger named 'user_data'."""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """description text"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format a log by obfuscating certain fields"""
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR
            )
        return super().format(record)
