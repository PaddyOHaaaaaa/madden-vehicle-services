"""Local preview server that mimics Cloudflare Pages: clean URLs and 404.html."""
import http.server
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def send_head(self):
        path = self.path.split("?", 1)[0].split("#", 1)[0]
        if path.endswith(".html"):
            clean = "/" if path == "/index.html" else path[:-5]
            self.send_response(308)
            self.send_header("Location", clean)
            self.end_headers()
            return None
        local = os.path.join(ROOT, path.lstrip("/"))
        if path != "/" and not os.path.exists(local) and os.path.exists(local + ".html"):
            self.path = path + ".html"
        elif path != "/" and not os.path.exists(local):
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            return open(os.path.join(ROOT, "404.html"), "rb")
        return super().send_head()


http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
