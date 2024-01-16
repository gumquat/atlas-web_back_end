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

# Problem 2 - Create Logger
### Implement a get_logger function that takes no arguments and returns a logging.Logger object
* The logger should be named "user_data" and only log up to logging.INFO level. It should not propagate messages to other loggers. It should have a StreamHandler with RedactingFormatter as formatter.
    - Create a tuple PII_FIELDS constant at the root of the module containing the fields from user_data.csv that are considered PII. 
    - PII_FIELDS can contain only 5 fields - choose the right list of fields that can are considered as “important” PIIs or information that you must hide in your logs.
    - Use it to parameterize the formatter.

# Problem 3 - Connect to secure database
### Connect to a secure holberton database to read a users table
Database credentials should NEVER be stored in code or checked into version control. One secure option is to store them as environment variable on the application server.
* In this task, you will connect to a secure holberton database to read a users table. The database is protected by a username and password that are set as environment variables on the server named PERSONAL_DATA_DB_USERNAME (set the default as “root”), PERSONAL_DATA_DB_PASSWORD (set the default as an empty string) and PERSONAL_DATA_DB_HOST (set the default as “localhost”).
* The database name is stored in PERSONAL_DATA_DB_NAME.
* Implement a get_db function that returns a connector to the database (mysql.connector.connection.MySQLConnection object).
    - Use the os module to obtain credentials from the environment
    - Use the module mysql-connector-python to connect to the MySQL database (pip3 install mysql-connector-python)

# Problem 4 - Read and Filter Data
### Implement a 'main function'
The 'Main' function will obtain a database connection using get_db and retrieve all rows in the users table and display each row under a filtered format like this:
```
[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=e848:e856:4e0b:a056:54ad:1e98:8110:ce1b; last_login=2019-11-14T06:16:24; user_agent=Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN);
```
Filtered Fields:
    - name
    - email
    - phone
    - ssn
    - password
* ONLY your main function should run when the module is executed.

# Problem 5 - Encrypting Passwords
### Implement a hash_password function that expects one string argument name password and returns a salted, hashed password, which is a byte string
* Use the bcrypt package to perform the hashing (with hashpw)

# Problem 6 - Check Valid Password
### Implement an is_valid function that expects 2 arguments and returns a boolean
* Arguments:
    - hashed_password: bytes type
    - password: string type
Use bcrypt to validate that the provided password matches the hashed password.