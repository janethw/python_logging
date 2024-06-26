# From tutorial at: https://www.datadoghq.com/blog/python-logging-best-practices/


import logging

# The logging library's built-in getLogger() method dynamically sets the logger name
# to match the name of your module (file).
logger = logging.getLogger(__name__)

