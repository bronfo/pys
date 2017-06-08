#coding:utf-8

import os
import logging

from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, stream_request_body

logger = logging.getLogger(os.path.basename(__file__))
PORT = 8080
g_ioloop = None

#@stream_request_body
class PostHandler(RequestHandler):
    def get(self):
        self.write('get ok')

def do():
    logging.basicConfig(format='%(asctime)s %(lineno)s: %(message)s')
    logger.setLevel(logging.DEBUG)
    logger.debug("doing...")
    
    global g_ioloop
    g_ioloop = IOLoop()
    g_ioloop.make_current()
    
    application = Application([
        (r".*", PostHandler),
    ])
    application.listen(PORT)
    
    g_ioloop.start()
    g_ioloop.close(all_fds=True)
    logger.debug("stopped")
    return True

def stop():
    logger.debug("stopping...")
    g_ioloop.add_callback_from_signal(g_ioloop.stop)
