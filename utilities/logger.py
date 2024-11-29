import logging


def setup_logger(name):
    """
    Sets up a logger with the specified name and formats it for console output.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)  # Set the log level

    # Check if the logger already has handlers (prevents duplicate messages)
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
