# from http.server import HTTPServer, BaseHTTPRequestHandler
# import socket
# import socketserver
# import http

# HOST = socket.gethostname()
# IPAddr = socket.gethostbyname(HOST)
# PORT = 4000
# print(IPAddr)

# Handler = BaseHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print(f"Running on {IPAddr}:{PORT}")
#     httpd.serve_forever()
from flask import Flask
app = Flask(__name__)


if __name__ == '__main__':
    app.debug = True
    app.run()
