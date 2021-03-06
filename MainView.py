from PyQt5 import QtWidgets
from gen.ui_MainView import Ui_MainWindow


class MainView(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, model, main_ctrl):
        self.model = model
        self.main_ctrl = main_ctrl
        super(MainView, self).__init__()
        self.build_ui()
        # register func with model for future model update
        self.model.subscribe_update_func(self.update_ui)

    def build_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # connect signal to method
        self.ui.testAll.clicked.connect(self.btnClicked)
        self.ui.test1.clicked.connect(self.btnClicked)
        self.ui.test2.clicked.connect(self.btnClicked)
        self.ui.test3.clicked.connect(self.btnClicked)
        self.ui.test4.clicked.connect(self.btnClicked)
        self.ui.test5.clicked.connect(self.btnClicked)
        self.ui.test6.clicked.connect(self.btnClicked)

    def enable_buttons(self, enabled):
        self.ui.testAll.setEnabled(enabled)
        self.ui.test1.setEnabled(enabled)
        self.ui.test2.setEnabled(enabled)
        self.ui.test3.setEnabled(enabled)
        self.ui.test4.setEnabled(enabled)
        self.ui.test5.setEnabled(enabled)
        self.ui.test6.setEnabled(enabled)

    def btnClicked(self):
        sender_name = self.sender().objectName()
        self.main_ctrl.run_test(sender_name)

    def update_ui(self):
        print('update_ui()++')

        msg = self.model.get_message()
        if msg != '':
            self.ui.listWidget.addItem(msg)

        self.enable_buttons(not self.model.is_testing())
