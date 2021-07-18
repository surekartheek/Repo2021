import logging


def customLogger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s - %(funcName)s - '
                                                   '%(levelname)s --> %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logging
