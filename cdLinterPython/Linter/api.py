from Linter.parser.gitlab_yaml_parser import GitLabYAMLParser
from Linter.engine import LintEngine


_parser = GitLabYAMLParser()
_engine = LintEngine()

def lint_from_string(yaml_text: str):
    model = _parser.parse_from_string(yaml_text)
    return _engine.run(model)

def lint_from_file(path: str):
    model = _parser.parse_from_file(path)
    return _engine.run(model)
