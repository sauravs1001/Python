import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt="%d/%m/%Y %I:%M:%S %p", level=logging.DEBUG)
logging.warning("Warning message ---")
logging.info("Info message ")
logging.error("Errorr ++++")