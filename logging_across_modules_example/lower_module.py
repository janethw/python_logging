import logging


def word_count(my_test_file):

    logging.basicConfig(level=logging.DEBUG,
                        filename="my_log.log",
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    try:
        # Count the number of words in a file and log the result
        with open(my_test_file, 'r') as f:
            file_contents = f.read()
            words = file_contents.split()
            num_words = len(words)
            logger.debug('Number of words: %d', num_words)
            return num_words

    except OSError as e:
        logger.error('Unable to open file: %s', e)

