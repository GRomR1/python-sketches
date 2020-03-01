import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG) # logging.INFO


if __name__ == "__main__":
    logger.debug("The script %s was started", __name__)
