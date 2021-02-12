from src.Ui_Files.DockWidgets.Py.dw_Console import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
from PySide2 import QtCore,QtWidgets


class Console_view(QtWidgets.QDockWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)

        self._init_vars()
        self._init_widgets()
        self._init_UI()

    def _init_vars(self):
        self.current_data_container = None

    def _init_widgets(self):
        self.console = self.ui.widget
        self.context_menu = QtWidgets.QMenu(self)
        # Create context menu
        rc_browser_options(self)

    def _init_UI(self):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.currentPath())

        # app = QApplication([])
        # console = PythonConsole()
        # console.show()
        # console.eval_in_thread()
        #
        # sys.exit(self.console.exec_())
        # self.tree_view.setModel(self.model)
        # self.tree_view.setSortingEnabled(True)
        #
        # self.tree_view.sortByColumn(True)
        # self.tree_view.setRootIndex(self.model.index(ApplicationSettings.PROJECT_PATH))
        #
        # self.tree_view.setModel(self.model)
        # self.tree_view.installEventFilter(self)
        # self.tree_view.setColumnWidth(0, 200)



    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False



