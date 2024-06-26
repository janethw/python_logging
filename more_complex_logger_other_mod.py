import logging

module_logger = logging.getLogger("exampleApp.more_complex_logger_other_mod")


def add(a, b):
    logger = logging.getLogger("exampleApp.more_complex_logger_other_mod.add")
    logger.info("Adding %s and %s to get %s" % (a, b, a+b))
    return a+b
