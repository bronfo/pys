import signal
import apps

if __name__ == "__main__":
    def handle_signal(sig, frame=None):
        apps.stop()
    signal.signal(signal.SIGINT, handle_signal)
    try:
        import win32api
        win32api.SetConsoleCtrlHandler(handle_signal, True)
    except Exception, e:
        pass
    
    while apps.do():
        reload(apps)
