import http.server
import socketserver
import os

os.chdir('/Users/colinvanostern/Desktop/Iceland')

PORT = 8742

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
