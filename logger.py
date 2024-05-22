import logging

# Configure the logging module to write logs to 'library.log' file
logging.basicConfig(filename='library.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    
    # Define a static method 'log' that logs the provided message at the INFO level
    @staticmethod
    def log(message):
        logging.info(message)
