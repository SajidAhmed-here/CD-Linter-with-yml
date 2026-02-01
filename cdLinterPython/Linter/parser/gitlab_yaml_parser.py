import yaml
from Linter.entities.job import Job
from Linter.entities.gitlab_yaml import GitLabYAML
from Linter.entities.retry import Retry


class GitLabYAMLParser:

    def parse_from_string(self, yaml_text: str) -> GitLabYAML:
        raw = yaml.safe_load(yaml_text)
        return self._parse(raw)

    def parse_from_file(self, path: str) -> GitLabYAML:
        with open(path, "r", encoding="utf-8") as f:
            raw = yaml.safe_load(f)
        return self._parse(raw)

    def _parse(self, raw: dict) -> GitLabYAML:
        jobs = {}

        for name, content in raw.items():
            if not isinstance(content, dict):
                continue

            retry_obj = None
            if isinstance(content.get("retry"), dict):
                retry_obj = Retry(
                    max_retries=content["retry"].get("max"),
                    when=content["retry"].get("when", [])
                )

            jobs[name] = Job(
                name=name,
                script=content.get("script"),
                when=content.get("when"),
                retry=retry_obj,
                allow_failure=content.get("allow_failure", False),
                only=content.get("only"),
                except_=content.get("except")
            )

        return GitLabYAML(jobs)
