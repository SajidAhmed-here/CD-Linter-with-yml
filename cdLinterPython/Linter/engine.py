from Linter.detectors.manual_detector import ManualDetector
from Linter.detectors.allow_failure_detector import AllowFailureDetector
from Linter.detectors.retry_detector import RetryDetector
from Linter.detectors.only_except_detector import OnlyExceptDetector


class LintEngine:
    def __init__(self):
        self.detectors = [
            ManualDetector(),
            AllowFailureDetector(),
            RetryDetector(),
            OnlyExceptDetector()
        ]

    def run(self, gitlab_yaml):
        findings = []

        for detector in self.detectors:
            findings.extend(detector.detect(gitlab_yaml))

        return findings
