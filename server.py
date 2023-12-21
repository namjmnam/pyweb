import http.server
import socketserver
import os

PORT = 80
DIRECTORY = "./sharedfiles"

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Serve the main investment page
            self.path = 'oil_investment.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

        elif self.path == '/files':
            # Serve the file listing page
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            html = '<html><head><title>File Downloads</title></head><body>'
            html += '<h1>Available Files</h1><ul>'
            for filename in os.listdir(DIRECTORY):
                html += f'<li><a href="{DIRECTORY}/{filename}" download>{filename}</a></li>'
            html += '</ul></body></html>'

            self.wfile.write(html.encode('utf-8'))

        else:
            # Handle other requests normally
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Set the directory to serve
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Set up the HTTP server
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
