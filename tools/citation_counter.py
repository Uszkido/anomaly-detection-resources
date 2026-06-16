"""Look up citation counts for papers via the Semantic Scholar API."""
import requests
import time

def get_citation_count(title, max_retries=3):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {"query": title, "fields": "title,citationCount,url", "limit": 1}
    for attempt in range(max_retries):
        resp = requests.get(url, params=params, timeout=15)
        if resp.status_code == 429:
            wait = 5 * (attempt + 1)
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
        "Deep Learning for Anomaly Detection: A Survey",
    ]
    for title in sample_titles:
        result = get_citation_count(title)
        if result:
            print(f"{result['title']}: {result['citationCount']} citations")
            print(f"  {result['url']}")
        else:
            print(f"{title}: not found or rate limited")
        time.sleep(3)
