from PyQt5 import QtCore
import time


class WorkerThread(QtCore.QThread):

    def __init__(self, model, name):
        QtCore.QThread.__init__(self)
        self.name = name
        self.model = model

    def msg(self, text):
        self.model.set_message(text)

    def run(self):
        self.msg('RUN(' + self.name + ')')
        time.sleep(5)
        self.msg('STOP(' + self.name + ')')

        self.model.done_one_test()
