import logging
import sys

ENDPOINT = "https://api.sms.ir"

class BaseRequester:
    def __init__(self) -> None:
        self.endpoint = ENDPOINT
        
        # setup logging
        self.log_level = logging.INFO

        log_format = logging.Formatter("[%(asctime)s] [%(levelname)s] - %(message)s")
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.log_level)

        # writing to stdout
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(self.log_level)
        handler.setFormatter(log_format)
        self.logger.addHandler(handler)
