from WorkerThread import WorkerThread
from TestAllThread import TestAllThread


class MainController(object):

    def __init__(self, model):
        self.model = model

    def run_test(self, test_name):
        if test_name == 'testAll':
            self.model.prepare_test(6) # 6 means a total of six tests will be run.
            self.test_all = TestAllThread(self.model)
            self.test_all.start()
        else:
            self.model.prepare_test(1)
            self.worker = WorkerThread(self.model, test_name)
            self.worker.start()
