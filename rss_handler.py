import feedparser
import requests

class RSSHandler:
    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        response.raise_for_status()
        self.feed = feedparser.parse(response.content)
        self.entries = self.feed.entries

    def __len__(self):
        return len(self.entries)

    def __iter__(self):
        yield from ((entry.title, entry.summary, entry.description) for entry in self.entries)