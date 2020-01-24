import threading

from servant import main


class ServantThread(threading.Thread):
    def run(self):
        main()


class UICallThread(threading.Thread):
    func = None
    args = None
    kwargs = None

    def set_function(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.func(*self.args, **self.kwargs)


def run_func_async(func, *args, **kwargs):
    thread = UICallThread()
    thread.set_function(func, *args, **kwargs)
    thread.start()
