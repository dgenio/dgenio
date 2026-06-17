"""
Consistency checker between README.md and portfolio.yml.

Checks (bidirectional):
1. Every repo link in portfolio.yml appears at least once in README.md.
2. Every GitHub link in README.md (github.com/dgenio/<repo>) is listed in portfolio.yml.
3. Every repo name in portfolio.yml appears at least once in README.md text.

Exit code 0 if consistent, 1 otherwise (prints mismatches).
"""

import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).parent.resolve()
README_PATH = REPO_ROOT / "README.md"
PORTFOLIO_PATH = REPO_ROOT / "portfolio.yml"
LINK_RE = re.compile(r"https://github\.com/dgenio/(\S+)").findall
NAME_RE = re.compile(r"^\s+name:\s+(\S+)", re.MULTILINE).findall
LINES_RE = re.compile(r"^\s+link:\s+(https://github\.com/dgenio/\S+)", re.MULTILINE).findall


def main() -> int:
    errors = []

    readme = README_PATH.read_text(encoding="utf-8")
    portfolio = PORTFOLIO_PATH.read_text(encoding="utf-8")

    portfolio_names = set(NAME_RE(portfolio))
    portfolio_links = set(LINES_RE(portfolio))

    readme_links_raw = LINK_RE(readme)
    # Strip trailing Markdown punctuation so "contextweaver)" -> "contextweaver"
    readme_links = {name.rstrip(")") for name in readme_links_raw}
    readme_link_urls = {f"https://github.com/dgenio/{name}" for name in readme_links}

    # 1. Every portfolio link must appear in README
    missing_in_readme = portfolio_links - readme_link_urls
    if missing_in_readme:
        errors.append(
            f"Links in portfolio.yml but not in README.md: {sorted(missing_in_readme)}"
        )

    # 2. Every README link must be in portfolio
    extra_in_readme = readme_link_urls - portfolio_links
    if extra_in_readme:
        errors.append(
            f"Links in README.md but not in portfolio.yml: {sorted(extra_in_readme)}"
        )

    # 3. Every portfolio name must appear in README text
    for name in portfolio_names:
        if name not in readme:
            errors.append(f"Repo name '{name}' in portfolio.yml but not found in README.md")

    if errors:
        print("Inconsistencies found between README.md and portfolio.yml:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("README.md and portfolio.yml are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
