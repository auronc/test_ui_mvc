from PyQt5 import QtCore
from WorkerThread import WorkerThread


class TestAllThread(QtCore.QThread):

    def __init__(self, model):
        QtCore.QThread.__init__(self)
        self.model = model

    def run(self):
        for i in range(1, 7):
            self.worker = WorkerThread(self.model, 'test{}'.format(i))
            self.worker.start()
            self.worker.wait()
