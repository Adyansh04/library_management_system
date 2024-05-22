import logging

logging.basicConfig(filename='library.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    @staticmethod
    def log(message):
        logging.info(message)
