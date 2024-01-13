# LOGGING
Logging in Python refers to the process of recording events that occur during the execution of a software program. It's a crucial aspect of software development, debugging, and operation. Logging helps developers understand the flow of a program and identify scenarios that might not have been considered during development. It can provide valuable information, such as which user or IP accessed the application, and offer insightful details in case of an error.

Python's built-in logging module provides a flexible framework for emitting log messages from Python programs. It is thread-safe, allowing it to handle multi-threaded applications efficiently. The logging module provides a way for applications to configure different log handlers, filters, and formatters, and to set the level of detail for each handler.

### Logging Example
```
import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

```
* In this example, the logging.basicConfig() function sets up the root logger with a filename, encoding, and level. 
* The logging.debug(), logging.info(), logging.warning(), and logging.error() functions are then used to log messages at different levels of severity.

Logging can be configured in various ways, including using dictionaries, JSON files, or YAML files, depending on the complexity of the application and the developer's preferences. The logging module also supports logging from multiple modules, allowing for a unified log across an entire application.

# Problem 0 - Regex-ing
### Write a function called filter_datum that returns the log message obfuscated
   * Arguments:
        - fields: a list of strings representing all fields to obfuscate
        - redaction: a string representing by what the field will be obfuscated
        - message: a string representing the log line
        - separator: a string representing by which character is separating all fields in the log line (message)

The function should use a regex to replace occurrences of certain field values.
filter_datum should be less than 5 lines long and use re.sub to perform the substitution with a single regex.

# Problem 1 - Log Formatter
### Update the class to accept a list of strings fields constructor argument
First, add the following code
```
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
```
* Implement the format method to filter values in incoming log records using filter_datum. Values for fields in fields should be filtered.
* DO NOT extrapolate FORMAT manually. The format method should be less than 5 lines long.