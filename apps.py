import SimpleHTTPServer
import SocketServer
import threading
import app

PORT = 8080
httpd = None

def shutdown():
    httpd.shutdown()
    httpd.server_close()
    app.restart()

class WebRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        if self.path == '/reset':
            threading.Timer(0.1, shutdown).start()
            self.wfile.write("reset ok\n")
        else:
            self.wfile.write("hi\n")

def start():
    global httpd
    SocketServer.TCPServer.allow_reuse_address = True
    Handler = WebRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "serving at port", PORT
    httpd.serve_forever()
