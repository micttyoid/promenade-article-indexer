import os
from typing import List, Optional, Union

# TODO: maybe intialize without OS


# A singleton import-around for configuration
class Config:
    def __init__(self):
        # hmm...
        self.NAME: str = os.getenv("NAME", "article-indexer")

        self.DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

        # ex. Validators keep going with warnings without termination
        self.LENIENT: bool = os.getenv("LENIENT", "False").lower() == "true"

    def show_config(self) -> dict:
        return {
            "NAME": self.NAME,
            "DEBUG": self.DEBUG,
            "ENVIRONMENT": self.ENVIRONMENT,
        }


# this
config = Config()
