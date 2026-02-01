class AllowFailureDetector:
    SMELL = "Allow Failure"

    def detect(self, gitlab_yaml):
        results = []

        for job in gitlab_yaml.jobs.values():
            if job.allow_failure is True:
                results.append({
                    "job": job.name,
                    "smell": self.SMELL
                })

        return results
