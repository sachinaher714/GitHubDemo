import logging

class BaseClass:
    def getlogger(self):

        logger=logging.getLogger(__name__)

        fileHandler=logging.FileHandler('logfile.log') #where to print logs

        formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        logger.setLevel(logging.info)