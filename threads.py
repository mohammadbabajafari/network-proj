import threading

from servant import main


class ServantThread(threading.Thread):
    def run(self):
        main()
