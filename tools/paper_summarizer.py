"""Fetch abstracts for papers by title using the Semantic Scholar API."""
import requests
import time

def get_abstract(title, max_retries=5):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {"query": title, "fields": "title,abstract,url", "limit": 1}
    for attempt in range(max_retries):
        resp = requests.get(url, params=params, timeout=15)
        if resp.status_code == 429:
            wait = 10 * (attempt + 1)
            print(f"  Rate limited, waiting {wait}s...")
            time.sleep(wait)
            continue
        resp.raise_for_status()
        data = resp.json()
        if data.get("data"):
            return data["data"][0]
        return None
    return None

if __name__ == "__main__":
    sample_titles = [
        "Anomaly Detection: A Survey",
    ]
    for title in sample_titles:
        result = get_abstract(title)
        if result:
            print(f"Title: {result['title']}")
            abstract = result.get("abstract") or "No abstract available."
            print(f"Abstract: {abstract[:300]}...")
            print(f"URL: {result['url']}\n")
        else:
            print(f"{title}: not found or rate limited\n")
        time.sleep(3)
