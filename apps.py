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
        if self.path == '/reset':
            threading.Timer(0.1, shutdown).start()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("reset ok\n")
            self.wfile.flush()
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

def start():
    global httpd
    SocketServer.TCPServer.allow_reuse_address = True
    Handler = WebRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "serving at port", PORT
    httpd.serve_forever()
