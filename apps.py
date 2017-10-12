#coding:utf-8

import os
import logging

from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler, RequestHandler, stream_request_body
from tornado.websocket import WebSocketHandler

logger = logging.getLogger(os.path.basename(__file__))
PORT = 8080
g_ioloop = None

#@stream_request_body
class WebHandler(RequestHandler):
    def get(self):
        logger.debug("do get")
        self.write('get ok')

class WsHandler(WebSocketHandler):
    def open(self):
        logger.debug("new ws")
    def on_message(self, message):
        self.write_message(u"You said: " + message)
    def on_close(self):
        logger.debug("close ws")

def do():
    logging.basicConfig(format='%(asctime)s %(lineno)s: %(message)s')
    logger.setLevel(logging.DEBUG)
    logger.debug("doing...")
    
    global g_ioloop
    g_ioloop = IOLoop()
    g_ioloop.make_current()
    
    application = Application([
        (r"/ws", WsHandler),
        (r"/static/(.*)", web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "static")}),
        (r".*", WebHandler),
    ])
    application.listen(PORT)
    
    g_ioloop.start()
    g_ioloop.close(all_fds=True)
    logger.debug("stopped")
    return True

def stop():
    logger.debug("stopping...")
    g_ioloop.add_callback_from_signal(g_ioloop.stop)
