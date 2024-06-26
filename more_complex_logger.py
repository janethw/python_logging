import logging
import more_complex_logger_other_mod as mc_logger


def main():
    # create a logger instance named "exampleApp"
    logger = logging.getLogger('exampleApp')
    logger.setLevel(logging.INFO)

    # Create the logging file handler object
    fh = logging.FileHandler('new_snake.log')

    # "asctime", "name", "levelhame" and "message" are LogRecord attributes
    # A full list of attributes at: https://docs.python.org/3/library/logging.html#logrecord-attributes
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # The file handler sets the formatter object as its formatter
    fh.setFormatter(formatter)

    # Add the file handler to the logger instance
    logger.addHandler(fh)

    logger.info("Program started")
    mc_logger.add(7, 8)
    logger.info("Program finished")


if __name__ == '__main__':
    main()