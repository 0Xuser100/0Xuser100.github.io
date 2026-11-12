"""Fail deployment verification if Pages serves anything except the checked site."""
import hashlib
import os
from pathlib import Path
import time
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

DIST = Path(__file__).resolve().parents[1] / 'dist'
BASE = os.environ.get('SITE_URL', 'https://0xuser100.github.io/').rstrip('/') + '/'
TEXT = {'.html', '.js', '.css', '.svg'}


def digest(data, path):
    if path.suffix in TEXT:
        data = data.replace(b'\r\n', b'\n')
    return hashlib.sha256(data).hexdigest()


def verify():
    errors = []
    for path in sorted(DIST.iterdir()):
        if not path.is_file() or path.name.startswith('.'):
            continue
        endpoint = '' if path.name == 'index.html' else quote(path.name)
        query = urlencode({'deployment': os.environ.get('GITHUB_SHA', str(int(time.time())))})
        try:
            request = Request(BASE + endpoint + '?' + query, headers={'Cache-Control': 'no-cache'})
            with urlopen(request, timeout=20) as response:
                actual = response.read()
            if digest(actual, path) != digest(path.read_bytes(), path):
                errors.append(f'{path.name}: published content differs from the repository')
        except Exception as error:
            errors.append(f'{path.name}: {error}')
    return errors


if __name__ == '__main__':
    attempts = int(os.environ.get('VERIFY_ATTEMPTS', '8'))
    for attempt in range(attempts):
        errors = verify()
        if not errors:
            print('Verified: the live homepage, scripts, styles, favicon, and CV match this deployment.')
            break
        print('\n'.join(errors), flush=True)
        if attempt + 1 == attempts:
            raise SystemExit('The live portfolio does not match the deployed files.')
        print('Waiting for the Pages cache to update...', flush=True)
        time.sleep(10)
