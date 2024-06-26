import logging


def add(a, b):
    logging.info("Adding %s and %s to get %s" % (a, b, a+b))
    return a + b
