import logging
import mySnake_other_mod


def main():
    logging.basicConfig(filename='mySnake.log', filemode="w", level=logging.INFO)
    logging.info('Program started')
    mySnake_other_mod.add(8, 9)
    logging.info('Program finished')


if __name__ == '__main__':
    main()