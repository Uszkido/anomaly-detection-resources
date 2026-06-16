"""Search arXiv for recent anomaly detection papers."""
import requests
import xml.etree.ElementTree as ET

QUERY = 'cat:cs.LG AND abs:"anomaly detection"'
MAX_RESULTS = 10

def fetch_recent_papers(query=QUERY, max_results=MAX_RESULTS):
    url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": max_results,
    }
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(resp.text)
    papers = []
    for entry in root.findall("atom:entry", ns):
        title = entry.find("atom:title", ns).text.strip()
        link = entry.find("atom:id", ns).text.strip()
        published = entry.find("atom:published", ns).text.strip()
        papers.append({"title": title, "link": link, "published": published})
    return papers

if __name__ == "__main__":
    papers = fetch_recent_papers()
    for p in papers:
        print(f"- {p['title']} ({p['published'][:10]})\n  {p['link']}")
