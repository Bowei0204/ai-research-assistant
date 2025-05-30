# paper_helper/arxiv_fetcher.py
import feedparser
import re

def extract_arxiv_id(url_or_id):
    match = re.search(r"\d{4}\.\d{5}(v\d+)?", url_or_id)
    return match.group(0) if match else url_or_id.strip()

def fetch_arxiv_metadata(arxiv_url_or_id):
    arxiv_id = extract_arxiv_id(arxiv_url_or_id)
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    feed = feedparser.parse(url)

    if feed.entries:
        entry = feed.entries[0]
        return {
            "title": entry.title,
            "authors": ", ".join(author.name for author in entry.authors),
            "published": entry.published.split("T")[0],
            "abstract": entry.summary.replace("\n", " ").strip()
        }
    return None
