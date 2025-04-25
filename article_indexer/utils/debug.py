from article_indexer.config import config


class PrintDebug:
    def __init__(self, debug=False):
        self.debug = debug

    def __call__(self, *args):
        if self.debug:
            print("DEBUG:", *args)


print_debug = PrintDebug(config.DEBUG)
