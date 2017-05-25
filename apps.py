import SimpleHTTPServer
import SocketServer

PORT = 8080
httpd = None

def start():
    global httpd
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "serving at port", PORT
    httpd.serve_forever()
