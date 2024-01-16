#!/usr/bin/env python3

"""filtered logger module that obfuscates data in log messages"""
from typing import List
import logging
import re
import os
import datetime
import mysql.connector

PII_FIELDS = ("name", "email", "password", "phone", "ssn")


# THIS CLASS HAS TO BE AT THE TOP OF THE FILE
class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter Class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """description text"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        format a log by obfuscating certain fields
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR
            )
        return super().format(record)


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
    logger = logging.getLogger('user_data')  # create logger named user_data
    logger.setLevel(logging.INFO)  # set level to info
    logger.propagate = False  # prevent duplicate logs

    stream_handler = logging.StreamHandler()  # add stream handler
    formatter = RedactingFormatter(fields = PII_FIELDS)
    stream_handler.setLevel(logging.INFO)  # set level to info
    stream_handler.setFormatter(formatter)  # add formatter to handler

    logger.addHandler(stream_handler)  # add handler to logger
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    connects to ATLAS MYsql DB
    """
    user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    pword = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db = os.getenv('PERSONAL_DATA_DB_NAME', 'my_db')  # 'my_db' from intranet

    db = mysql.connector.connect(  # this connects to the db
        user=user,
        password=pword,
        host=host,
        database=db
    )

    return db


def main():
    """
    no arguments & no returns
    retrieve every row in the "users table"
    display every row in a 'filtered format' [see README]
    """
    db = get_db()
    logger = get_logger()
    cursor = db.cursor()  # allows interaction with the db [queries, fetches]

    cursor.execute("SELECT * FROM users;")  # retrieve every row in users table
    rows = cursor.fetchall()

    for row in rows:  # display every row in the 'filtered format'
        filtered_row = filter_datum(
            PII_FIELDS, RedactingFormatter.REDACTION, str(row), ";"
            )
        logger.info(
            "[HOLBERTON] user_data INFO %s: %s;",
            str(datetime.datetime.now()), filtered_row
            )

    logger.info(  # display the filtered fields
        "Filtered fields:\n%s", "\n".join(PII_FIELDS)
        )

    # dont forget to close everything on your way out!
    cursor.close()
    db.close()
