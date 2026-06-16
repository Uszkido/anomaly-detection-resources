# Tools

Helper scripts for maintaining and exploring this resource list.

| Script | Purpose | Requirements |
|---|---|---|
| `arxiv_fetcher.py` | Searches arXiv for recent anomaly detection papers | `requests` |
| `citation_counter.py` | Looks up citation counts for papers via the Semantic Scholar API | `requests` |
| `paper_summarizer.py` | Fetches abstracts for papers listed in the README | `requests` |
| `toolkit_stats.py` | Fetches GitHub stars/forks for the toolboxes listed in the README | `requests` |

## Usage

```bash
pip install requests
python tools/arxiv_fetcher.py
python tools/citation_counter.py
python tools/paper_summarizer.py
python tools/toolkit_stats.py
```

`citation_counter.py` and `paper_summarizer.py` use the Semantic Scholar API, whose anonymous tier has a low shared rate limit. Both scripts retry with backoff automatically; if you still see "not found or rate limited", wait a few minutes and retry, or get a free API key at https://www.semanticscholar.org/product/api for higher limits.

Each script can be run standalone and prints results to stdout. No API keys are required, though Semantic Scholar's optional key speeds things up.
