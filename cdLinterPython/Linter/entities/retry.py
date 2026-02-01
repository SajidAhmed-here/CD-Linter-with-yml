class Retry:
    def __init__(self, max_retries=None, when=None):
        self.max_retries = max_retries
        self.when = when or []
