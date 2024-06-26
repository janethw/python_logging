import logging


def main():

    def word_count(my_test_file):
        logging.basicConfig(level=logging.DEBUG,
                            filename='data_dog_app.log',
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logging.debug("This is a test message")
        try:
            # Count the number of words in a file and log the result
            with open(my_test_file, 'r') as f:
                file_contents = f.read()
                words = file_contents.split()
                num_words = len(words)
                logging.debug('Number of words: %d', num_words)
                return num_words

        except OSError as e:
            logging.error('Unable to open file: %s', e)

    word_count('my_test_file.txt')
    word_count('my_non_existent_file.txt')


if __name__ == '__main__':
    main()
