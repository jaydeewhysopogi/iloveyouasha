"""Optional local static-file server. No backend, database, or dependencies."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from functools import partial
import socket
import webbrowser

PORT = 8000
ROOT = Path(__file__).resolve().parent

if __name__ == '__main__':
    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    with ThreadingHTTPServer(('0.0.0.0', PORT), handler) as server:
        url = f'http://localhost:{PORT}'
        print(f'Your monthsary website is running at {url}')
        lan_ip = socket.gethostbyname(socket.gethostname())
        print(f'On a phone using the same Wi-Fi, open http://{lan_ip}:{PORT}')
        print('Press Ctrl+C to stop.')
        webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print('\nGoodbye ♡')
