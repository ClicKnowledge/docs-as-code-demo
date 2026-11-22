"""Check published pages against the terminology standard.

Reads standards/terminology.yml and looks for any "avoid" word in the site's
.mdx pages. Code blocks, inline code and the page's front matter are skipped,
as is any text between these two MDX comments:

    {/* terminology-check: off */}
    {/* terminology-check: on */}

Prints one line per problem and exits with status 1 if it finds any, which
makes the GitHub Actions check fail.

Run it from the repository root:  python scripts/check_terminology.py
"""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".github", "node_modules", "templates", "standards", "scripts"}


def load_rules():
    data = yaml.safe_load((ROOT / "standards" / "terminology.yml").read_text(encoding="utf-8"))
    rules = []
    for term in data["terms"]:
        for word in term["avoid"]:
            pattern = re.compile(r"(?<![\w-])" + re.escape(word) + r"(?![\w-])", re.IGNORECASE)
            rules.append((pattern, word, term["use"]))
    return rules


def pages():
    for path in sorted(ROOT.rglob("*.mdx")):
        if not SKIP_DIRS.intersection(path.relative_to(ROOT).parts):
            yield path


def check_page(path, rules):
    problems = []
    in_code = in_front_matter = skipping = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if number == 1 and stripped == "---":
            in_front_matter = True
            continue
        if in_front_matter:
            in_front_matter = stripped != "---"
            continue
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if "terminology-check: off" in stripped:
            skipping = True
            continue
        if "terminology-check: on" in stripped:
            skipping = False
            continue
        if in_code or skipping:
            continue
        text = re.sub(r"`[^`]*`", "", line)  # ignore inline code
        for pattern, word, use in rules:
            if pattern.search(text):
                problems.append(f'{path.relative_to(ROOT)}:{number}: found "{word}". Use "{use}".')
    return problems


def main():
    rules = load_rules()
    problems = [p for page in pages() for p in check_page(page, rules)]
    for problem in problems:
        print(problem)
    if problems:
        print(f"\nTerminology check failed: {len(problems)} problem(s). See standards/terminology.yml.")
        return 1
    print("Terminology check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
