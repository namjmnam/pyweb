import http.server
import socketserver
import os

PORT = 8000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Print the contents of the current directory
        # print("Current directory contents:")
        # for file in os.listdir('.'):
        #     print(file)

        if self.path == '/':
            self.path = 'oil_investment.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Set up the HTTP server
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
