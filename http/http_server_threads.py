#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; chatset=utf08')
        self.end_headers()
        message = threading.currentThread().getName()
        self.wfile.write(message.encode('utf-8'))
        self.wfile.write(b'\n')

class TheadedHTTPServer(ThreadingMixIn, HTTPServer):
        """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = TheadedHTTPServer(('localhost', 8080), Handler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()