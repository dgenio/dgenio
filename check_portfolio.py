"""
Consistency checker between README.md and portfolio.yml.

Checks (bidirectional):
1. Every repo link in portfolio.yml appears at least once in README.md.
2. Every GitHub link in README.md (github.com/dgenio/<repo>) is listed in portfolio.yml.
3. Every repo name in portfolio.yml appears at least once in README.md.

Exit code 0 if consistent, 1 otherwise (prints mismatches).
"""

import pathlib
import re
import sys

try:
    import yaml
except ImportError:
    yaml = None


REPO_ROOT = pathlib.Path(__file__).parent.resolve()
README_PATH = REPO_ROOT / "README.md"
PORTFOLIO_PATH = REPO_ROOT / "portfolio.yml"
LINK_RE = re.compile(r"https://github\.com/dgenio/([^\s/)\]]+)")


def _parse_portfolio_native(path: pathlib.Path):
    """Parse the subset of YAML we actually use, without requiring PyYAML."""
    text = path.read_text(encoding="utf-8")
    repos = []
    current = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if line.startswith("  - name: "):
            current = {"name": line.split("name: ", 1)[1].strip()}
        elif line.startswith("    link: ") and current is not None:
            current["link"] = line.split("link: ", 1)[1].strip()
        elif line.startswith("    related_to:") and current is not None:
            current["related_to"] = []
        elif line.startswith("    composes_with:") and current is not None:
            current["composes_with"] = []
        elif line.startswith("    ") and current is not None and (line.strip().startswith("- ")):
            val = line.strip().lstrip("- ").strip()
            if "related_to" in current and current.get("related_to") is not None:
                current["related_to"].append(val)
            elif "composes_with" in current and current.get("composes_with") is not None:
                current["composes_with"].append(val)
        elif line.startswith("  - ") and current is not None:
            # new entry
            repos.append(current)
            current = {"name": line.split("name: ", 1)[1].strip()}
    if current is not None:
        repos.append(current)
    return repos


def parse_portfolio(path: pathlib.Path):
    if yaml is not None:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        return [
            {"name": item["name"], "link": item["link"]}
            for item in data.get("ecosystem", [])
        ]
    return _parse_portfolio_native(path)


def main() -> int:
    errors = []

    readme = README_PATH.read_text(encoding="utf-8")
    portfolio = parse_portfolio(PORTFOLIO_PATH)

    portfolio_names = {entry["name"] for entry in portfolio}
    portfolio_links = {entry["link"] for entry in portfolio}

    readme_links = set(LINK_RE.findall(readme))
    # Reconstruct full URLs for comparison
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
