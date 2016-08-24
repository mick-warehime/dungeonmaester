import datetime
import logging
import os


# get the global logger
def getLogger(module_name):
    return logging.getLogger(module_name)


def logging_filepath_from_date():
    """
    creates a path to a log file based on the current time
    this will create a 'logs' folder if one doesn't exist already

    :rtype: string
    """

    d = datetime.datetime.now()
    log_filename = d.strftime('runtimelog_%b_%d_%Y_%H_%M_%S.log')

    LOGGING_DIRECTORY = '../logs'
    if not os.path.isdir(LOGGING_DIRECTORY):
        os.makedirs(LOGGING_DIRECTORY)

    return os.path.join(LOGGING_DIRECTORY, log_filename)

LOGFILE = logging_filepath_from_date()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-20s %(name)-20s %(levelname)-10s %(message)s',
                    datefmt='%m-%d-%Y %H:%M',
                    filename=LOGFILE,
                    filemode='w')
# create file handler which logs even debug messages
fh = logging.FileHandler(LOGFILE)
fh.setLevel(logging.INFO)
# define a Handler which writes ERROR messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logger = logging.getLogger('')
logger.addHandler(console)
logger.info('BEGIN RUNTIME LOG')

