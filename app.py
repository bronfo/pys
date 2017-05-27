import threading
import signal
import apps

done_event = None

def handle_signal(sig, frame):
    print 'ctrl c', done_event
    threading.Timer(0.1, apps.shutdown, (done_event,)).start()

if __name__ == "__main__":
    signal.signal(signal.SIGUSR1, handle_signal)
    done_event = threading.Event()
    while True:
        apps.do(done_event)
        print 'done'
        done_event.wait()
        done_event.clear()
        print 'restarting...'
        reload(apps)
