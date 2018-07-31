from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):
    def error(self, message):
        pass

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, values) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, values)
                    self.links.add(url)
                    print(url)

    def page_links(self):
        return self.links
