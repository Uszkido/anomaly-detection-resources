# Automation Workflows

This directory contains GitHub Actions workflows that keep the repository healthy automatically.

| Workflow | Schedule | Purpose |
|---|---|---|
| `link-checker.yml` | Every Monday | Scans all URLs in README and opens an issue if any are broken |
| `arxiv-watcher.yml` | Every Wednesday | Searches arXiv for new anomaly detection papers and opens a curated issue |
| `stale.yml` | Daily | Labels issues/PRs inactive after 60 days, closes after 7 more |

No configuration needed — workflows run automatically once the PR is merged.
