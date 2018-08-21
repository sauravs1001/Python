import logging
import logging.config


class LoggerConfig:
    def testLogConfig(self):

        logging.config.fileConfig("logging.conf")
        logger = logging.getLogger(LoggerConfig.__name__)

        # Logging messages
        logger.debug("Debug message Example")
        logger.info("Info message example")
        logger.warning("Warning message example")
        logger.error("Error message Example")
        logger.critical("Critical message Example")

obj = LoggerConfig()
obj.testLogConfig()