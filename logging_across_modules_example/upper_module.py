import logging
import lower_module


logging.basicConfig(level=logging.DEBUG, filename="my_log.log", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def main():

    def record_word_count(my_file):
        logger.info("Starting the record_word_count function")
        try:
            word_count = lower_module.word_count(my_file)
            with open("word_count_archive.csv", 'a') as f:
                row = str(my_file) + "," + str(word_count)
                f.write(row + "\n")
        except:
            logger.warning("Could not write file %s to destination", my_file)
        finally:
            logger.debug("Ending the record_word_count function for the file %s", my_file)


    record_word_count('../my_test_file.txt')
    record_word_count('my_non_existent_file.txt')


if __name__ == '__main__':
    main()
