import SimpleHTTPServer
import SocketServer
import threading

PORT = 8080
httpd = None
done_event = None

def shutdown(evt):
    httpd.shutdown()
    httpd.server_close()
    evt.set()

class WebRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        if self.path == '/reset':
            threading.Timer(0.1, shutdown, (done_event,)).start()
            self.wfile.write("reset ok\n")
        else:
            self.wfile.write("hi5\n")

def do(evt):
    global httpd
    global done_event
    done_event = evt
    SocketServer.TCPServer.allow_reuse_address = True
    Handler = WebRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "serving at port", PORT
    httpd.serve_forever()
