from Ui_Files.DockWidgets.Py.dw_ProjectView import Ui_DockWidget
from gui_elements.RC_Fucntions import *
from gui_elements.settings import ApplicationSettings
from PySide2 import QtCore,QtWidgets


class ProjectBrowser(QtWidgets.QDockWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # self.dw = QtWidgets.QDockWidget()
        # self.dw_ui = Ui_DockWidget()
        # self.dw_ui.setupUi(self.dw)
        # Above for Tree() Class

        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)
        # Above for QtWidgets.QTreeView class

        self._init_vars()
        self._init_widgets()
        self._init_UI()

    def _init_vars(self):
        self.current_data_container = None

    def _init_widgets(self):
        self.tree_view = self.ui.treeView
        # Above for normal QtWidgets.QTreeView and QTree
        self.context_menu = QtWidgets.QMenu(self)

    def _init_UI(self):
        # pass
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.currentPath())

        self.tree_view.setModel(self.model)
        self.tree_view.setSortingEnabled(True)

        self.tree_view.sortByColumn(True)
        self.tree_view.setRootIndex(self.model.index(ApplicationSettings.PROJECT_PATH))

        self.tree_view.setModel(self.model)
        self.tree_view.clicked.connect(self.item_clicked)
        self.tree_view.installEventFilter(self)
        self.tree_view.setColumnWidth(0, 200)
        # Above for QTreeView class and for Tree() then pass

        # Create context menu
        rc_browser_options(self)

    def project_changed(self):
        pass

    def item_clicked(self):
        pass

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False






