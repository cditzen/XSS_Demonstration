#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from FakeDatabase import FakeDatabase


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    database = FakeDatabase()

    # Handle HTTP GET requests
    def do_GET(self):
        self.send_response(200)
        self.sendHeaders()

        route = self.path[1:]

        if route == "posts":
            self.getPosts()

        return

    # Handle HTTP POST requests
    def do_POST(self):
        self.send_response(200)
        self.sendHeaders()

        route = self.path[1:]

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len).decode("utf-8")

        if route == "submit-post":
            self.submitPost(post_body)
        elif route == "clear-database":
            self.clearDatabase()

        return

    def sendHeaders(self):
        self.send_header('Content-type', 'text/html')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        return


    def getPosts(self):
        message = json.dumps(self.database.getPosts())

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    def submitPost(self, post):
        self.database.addPost(post)
        return

    def clearDatabase(self):
        self.database.deletePosts()
        return

def run():
    print('starting server...')

    # Server settings
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

run()