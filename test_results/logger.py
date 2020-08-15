import inspect
import logging
from test_page.testData import testDatafile as TD

def customLogger(logLevel=logging.DEBUG):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)
    automationFile=TD.automationLogPath+TD.automationLogFileName
    fileHandler = logging.FileHandler(automationFile, mode='a')
    fileHandler.setLevel(logLevel)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger






