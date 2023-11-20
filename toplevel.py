import logging

logger = logging.getLogger(__name__)
logger.info(f"Imported {__name__}")


class TopLevelLogger:
    def __init__(self, master):
        self.master = master
        logger.info("Logger works here now")
