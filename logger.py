import logging

# Configure the logger
logging.basicConfig(
    level=logging.INFO,     # Set the logging level to DEBUG
    format='%(asctime)s [%(name)s] [%(levelname)s]: %(message)s'  # Include logger name
)


def get_logger(name: str):
    return logging.getLogger(name)
