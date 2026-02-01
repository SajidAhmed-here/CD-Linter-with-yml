class ManualDetector:
    SMELL = "Manual Job"

    def detect(self, gitlab_yaml):
        results = []

        for job in gitlab_yaml.jobs.values():
            if job.when == "manual":
                results.append({
                    "job": job.name,
                    "smell": self.SMELL
                })

        return results
