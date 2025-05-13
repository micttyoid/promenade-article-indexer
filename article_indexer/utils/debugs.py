from article_indexer.config import config
from typing import Any


class PrintDebug:
    def __init__(self):
        self._debug_enabled = config.DEBUG
        config.subscribe(self._handle_config_change)

    def _handle_config_change(self, key: str, old_value: bool, new_value: bool):
        if key == "DEBUG":
            self._debug_enabled = new_value

    def __call__(self, *messages):
        if self._debug_enabled:
            print("[DEBUG]", *messages)

    def __del__(self):
        config.unsubscribe(self._handle_config_change)


print_debug = PrintDebug()
