"""Fetch GitHub stars/forks for anomaly detection toolboxes."""
import requests

REPOS = [
    "yzhao062/pyod",
    "TimeEval/TimeEval",
    "open-edge-platform/anomalib",
    "salesforce/Merlion",
]

def get_repo_stats(repo):
    url = f"https://api.github.com/repos/{repo}"
    resp = requests.get(url, timeout=15)
    if resp.status_code != 200:
        return None
    data = resp.json()
    return {
        "name": data["full_name"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
    }

if __name__ == "__main__":
    for repo in REPOS:
        stats = get_repo_stats(repo)
        if stats:
            print(f"{stats['name']}: {stats['stars']} stars, {stats['forks']} forks")
        else:
            print(f"{repo}: could not fetch (may not exist or rate limited)")
