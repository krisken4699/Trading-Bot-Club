from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import socketserver
import http

HOST = socket.gethostname()
IPAddr = socket.gethostbyname(HOST)
PORT = 4040

# Handler = BaseHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print(f"Running on {IPAddr}:{PORT}")
#     httpd.serve_forever()
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host=HOST, port=PORT)
