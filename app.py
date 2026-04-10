from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

server = HTTPServer(('0.0.0.0', PORT), SimpleHTTPRequestHandler)

print(f"Server running on port {PORT}")
server.serve_forever()
