class RetryDetector:
    SMELL = "Retry Job"

    def detect(self, gitlab_yaml):
        results = []

        for job in gitlab_yaml.jobs.values():
            if job.retry and job.retry.max_retries:
                results.append({
                    "job": job.name,
                    "smell": self.SMELL,
                    "retries": job.retry.max_retries
                })

        return results
