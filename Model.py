
class Model(object):

    def __init__(self):
        self._update_funcs = []
        self.message = ''

        # self.status_testing = False
        self._number_of_tests = 0

    def get_message(self):
        msg = self.message
        self.message = ''
        return msg

    def set_message(self, msg):
        self.message = msg
        self.announce_update()

    def prepare_test(self, number_of_test):
        self._number_of_tests = number_of_test
        self.announce_update()

    def done_one_test(self):
        if self._number_of_tests > 0:
            self._number_of_tests = self._number_of_tests - 1
        else:
            print('Program flow error!')

        self.announce_update()

    def is_testing(self):
        return self._number_of_tests > 0

    def subscribe_update_func(self, func):
        if func not in self._update_funcs:
            self._update_funcs.append(func)

    def unsubscribe_update_func(self, func):
        if func in self._update_funcs:
            self._update_funcs.remove(func)

    def announce_update(self):
        for func in self._update_funcs:
            func()
