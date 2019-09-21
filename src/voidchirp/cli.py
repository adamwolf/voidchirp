import logging


def configure_logging(verbosity=None):
    # Don't show anything but the message
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if verbosity is None:
        logger.setLevel("INFO")
    elif verbosity == "quiet":
        logging.disabled = True
    elif verbosity == "verbose":
        logger.setLevel("DEBUG")
