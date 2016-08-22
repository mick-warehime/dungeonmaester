import datetime
import logging
import os

LOGGING_DIRECTORY = '../logs'

def logging_filepath_from_date():
    """
    creates a path to a log file based on the current time
    this will create a 'logs' folder if one doesn't exist already

    :rtype: string
    """

    d = datetime.datetime.now()
    log_filename = d.strftime('runtimelog_%b_%d_%Y_%H_%M_%S.log')

    if not os.path.isdir(LOGGING_DIRECTORY):
        os.makedirs(LOGGING_DIRECTORY)

    return os.path.join(LOGGING_DIRECTORY, log_filename)


# create logger with 'spam_application'
logger = logging.getLogger('DungeonMaester')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
log_filepath = logging_filepath_from_date()
fh = logging.FileHandler(log_filepath)
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info("Begin Runtime Log")
