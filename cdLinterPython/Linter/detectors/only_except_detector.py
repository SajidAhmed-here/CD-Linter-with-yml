class OnlyExceptDetector:
    SMELL = "Only/Except Usage"

    def detect(self, gitlab_yaml):
        results = []

        for job in gitlab_yaml.jobs.values():
            if job.only is not None or job.except_ is not None:
                results.append({
                    "job": job.name,
                    "smell": self.SMELL
                })

        return results
