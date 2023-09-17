import requests
import xml.etree.ElementTree as ET

class RSSFeedReader:
    def __init__(self):
        self.feeds = []

    def add_feed(self, url):
        self.feeds.append(url)

    def fetch_rss_feed(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to fetch feed from {url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error fetching feed from {url}: {str(e)}")
        return None

    def parse_rss(self, xml_data):
        try:
            root = ET.fromstring(xml_data)
            items = root.findall(".//item")
            for item in items:
                title = item.find("title").text
                description = item.find("description").text
                link = item.find("link").text

                print(f"Title: {title}")
                print(f"Description: {description}")
                print(f"Link: {link}")
                print("\n")
        except Exception as e:
            print(f"Error parsing RSS feed: {str(e)}")

if __name__ == "__main__":
    feed_reader = RSSFeedReader()

    # Add RSS feed URLs
    while True:
        user_url = input("Enter an RSS feed URL (or press Enter to quit): ")
        if not user_url:
            break
        feed_reader.add_feed(user_url)

    for feed_url in feed_reader.feeds:
        xml_data = feed_reader.fetch_rss_feed(feed_url)
        if xml_data:
            feed_reader.parse_rss(xml_data)