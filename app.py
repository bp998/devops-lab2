from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Hello world.".encode('utf-8'))

if __name__ == "__main__":
    print("Serwer rusza na porcie 8080...")
HTTPServer(('0.0.0.0', 8080), MyHandler).serve_forever()