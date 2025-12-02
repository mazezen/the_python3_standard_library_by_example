#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import cgi
from http.server import BaseHTTPRequestHandler
import io

class PostHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Parse the form data posted.
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONNECT_TYPE': self.headers['Content-Type'],
            }
        )

        # Begin the response.
        self.send_response(200)
        self.send_header('Content-Type',
                        'text/plain;charset=utf-8')
        self.end_headers()

        out = io.TextIOWrapper(
            self.wfile,
            encoding='utf-8',
            line_buffering=False,
            write_through=True,
        )

        out.write('Client: {}\n'.format(self.client_address))
        out.write('User-agent: {}\n'.format(
            self.headers['use_agent']
        ))
        out.write('Path: {}\n'.format(self.path))
        out.write('From data:\n')

        # Echo back information about what was posted in the form.
        for filed in form.keys():
            filed_item = form[filed]
            if filed_item.filename:
                # The field contains an uploaded file.
                file_data = filed_item.file.read()
                file_len = len(file_data)
                del file_data
                out.write(
                    '\tUploaded {} as {!r} ({}) bytes)\n'.format(
                        filed, filed_item.filename, file_len
                ))

            else:
                # Regular form value
                out.write('\t{}={}\n'.format(
                    filed, form[filed].value
                ))
        out.detach()

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), PostHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()