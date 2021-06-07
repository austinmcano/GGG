from Ui_Files.DockWidgets.Py.dw_calculator import Ui_DockWidget
from gui_elements.RC_Fucntions import *
from PySide2 import QtCore,QtWidgets
# import numexpr


class Calculator_view(QtWidgets.QDockWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)
        self._init_vars()
        self._init_widgets()
        self._init_UI()

    def keyPressEvent(self, event):
        super(Calculator_view, self).keyPressEvent(event)
        self.keyPressed.emit(event.key())

    def _init_vars(self):
        self.text = str('')

    def _init_widgets(self):
        self.context_menu = QtWidgets.QMenu(self)
        rc_browser_options(self)

    def _init_UI(self):
        self.ui.pb0.clicked.connect(lambda: self.number_pressed('0'))
        self.ui.pb1.clicked.connect(lambda: self.number_pressed('1'))
        self.ui.pb2.clicked.connect(lambda: self.number_pressed('2'))
        self.ui.pb3.clicked.connect(lambda: self.number_pressed('3'))
        self.ui.pb4.clicked.connect(lambda: self.number_pressed('4'))
        self.ui.pb5.clicked.connect(lambda: self.number_pressed('5'))
        self.ui.pb6.clicked.connect(lambda: self.number_pressed('6'))
        self.ui.pb7.clicked.connect(lambda: self.number_pressed('7'))
        self.ui.pb8.clicked.connect(lambda: self.number_pressed('8'))
        self.ui.pb9.clicked.connect(lambda: self.number_pressed('9'))
        self.ui.pb_plus.clicked.connect(lambda: self.number_pressed('+'))
        self.ui.pb_minus.clicked.connect(lambda: self.number_pressed('-'))
        self.ui.pb_times.clicked.connect(lambda: self.number_pressed('*'))
        self.ui.pb_divide.clicked.connect(lambda: self.number_pressed('/'))

        self.ui.pb_equal.clicked.connect(lambda: self.equal_pressed())

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def number_pressed(self,num):
        self.text = self.text+num
        self.ui.lineEdit.setText(self.text)

    # def equal_pressed(self):
    #     num = numexpr.evaluate(self.ui.lineEdit.text()).item()
    #     self.ui.lineEdit.setText(str(num))
    #     self.text = str(num)

