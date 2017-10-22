import signal
import os
import logging
import apps

logger = logging.getLogger(os.path.basename(__file__))

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(filename)s %(lineno)s: %(message)s')
    logger.setLevel(logging.DEBUG)
    logger.debug('main enter')
    def handle_signal(sig, frame=None):
        apps.stop()
    signal.signal(signal.SIGINT, handle_signal)
    
    '''
    try:
        import win32api
        win32api.SetConsoleCtrlHandler(handle_signal, True)
    except Exception, e:
        pass
    '''

    while apps.do():
        logger.debug('reload...')
        reload(apps)
