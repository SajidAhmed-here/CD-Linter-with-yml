import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Linter.api import lint_from_file

results = lint_from_file("test_files\Test1.yaml")

print("Detected smells:")
for r in results:
    print(r)
