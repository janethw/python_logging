# Reference: https://www.datadoghq.com/blog/python-logging-best-practices/

import logging

# Add filemode="w" to overwrite
logging.basicConfig(filename='sample.log', filemode="w", level=logging.INFO)
log = logging.getLogger("ex")

try:
    raise RuntimeError('There has been a RuntimeError')
except Exception as err:
    log.exception("An exception occurred: %s" % err)


logging.debug('This is a debug message')
logging.info('This is an info message')
logging.error('This is an error message')
logging.warning('This is a warning message')