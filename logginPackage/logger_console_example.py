import logging

class LoggerConsole:
    def testLog(self):
        # Create Logger
        logger = logging.getLogger(LoggerConsole.__name__)
        logger.setLevel(logging.INFO)

        # Create console handler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        # Create Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt="%d/%m/%Y %I:%M:%S %p")

        # Add Formatter to console Handler -> ch
        chandler.setFormatter(formatter)

        # Add console handler to logger
        logger.addHandler(chandler)

        # Logging messages
        logger.debug("Debug message Example")
        logger.info("Info message example")
        logger.warning("Warning message example")
        logger.error("Error message Example")
        logger.critical("Critical message Example")

obj = LoggerConsole()
obj.testLog()




