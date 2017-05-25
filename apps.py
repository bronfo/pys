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
        '''
        if self.path == '/reset':
            self.wfile.write("reset ok\n")
            threading.Timer(0.1, shutdown).start()
        else:
            self.wfile.write("hi4\n")
        '''
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

def start():
    global httpd
    SocketServer.TCPServer.allow_reuse_address = True
    Handler = WebRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "serving at port", PORT
    httpd.serve_forever()
