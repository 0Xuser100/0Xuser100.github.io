"""Check the portable, buildless website before publishing to GitHub Pages."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
ORIGIN = 'https://0xuser100.github.io/'


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.canonical = []
        self.og_url = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])
        if 'data-en' in attrs and 'data-ar' not in attrs:
            self.errors.append(f'Missing Arabic text on <{tag}>')
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical.append(attrs.get('href'))
        if tag == 'meta' and attrs.get('property') == 'og:url':
            self.og_url.append(attrs.get('content'))


def main():
    errors = []
    html = (DIST / 'index.html').read_text(encoding='utf-8')
    parser = SiteParser()
    parser.feed(html)
    errors.extend(parser.errors)
    errors.extend(f'Duplicate ID: {key}' for key, count in Counter(parser.ids).items() if count > 1)
    for link in parser.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        if url.path:
            path = (DIST / unquote(url.path).lstrip('/')).resolve()
            if not path.is_relative_to(DIST) or not path.is_file():
                errors.append(f'Missing local asset: {link}')
        elif url.fragment and url.fragment not in parser.ids:
            errors.append(f'Missing anchor: {link}')
    if parser.canonical != [ORIGIN] or parser.og_url != [ORIGIN]:
        errors.append('Canonical and Open Graph URLs must match the GitHub Pages URL')
    if (DIST / 'Mahmoud_Abdulhamid.pdf').read_bytes()[:4] != b'%PDF':
        errors.append('CV file is not a valid PDF')
    if not (DIST / '.nojekyll').exists():
        errors.append('Missing .nojekyll marker')
    for css in DIST.glob('*.css'):
        for match in re.finditer(r'url\([\s\"\']*([^\)\"\']+)', css.read_text(encoding='utf-8')):
            value = match.group(1).strip()
            if not urlsplit(value).scheme and not value.startswith(('#', '//')):
                if not (css.parent / value).is_file():
                    errors.append(f'Missing CSS asset: {value}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print('Passed: local assets, anchor links, bilingual text, CV, and GitHub Pages metadata.')


if __name__ == '__main__':
    main()
