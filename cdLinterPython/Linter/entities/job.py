class Job:
    def __init__(
        self,
        name: str,
        script=None,
        when=None,
        retry=None,
        allow_failure=False,
        only=None,
        except_=None,
        lines=None
    ):
        self.name = name
        self.script = script
        self.when = when
        self.retry = retry
        self.allow_failure = allow_failure
        self.only = only
        self.except_ = except_
        self.lines = lines or {}
