from threading import Thread

def run_in_thread(fn, *args, **kwargs):
    thread = Thread(target=fn, args=args, kwargs=kwargs)
    thread.daemon = True
    thread.start()
    return thread
