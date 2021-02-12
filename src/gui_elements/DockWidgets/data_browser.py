from src.Ui_Files.DockWidgets.Py.dw_dirModel import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
from src.gui_elements.settings import *
from PySide2 import QtCore,QtWidgets


class DataBrowser(QtWidgets.QDockWidget):
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
        self.tree_view = self.ui.treeView
        self.context_menu = QtWidgets.QMenu(self)
        # Create context menu
        rc_browser_options(self)

    def _init_UI(self):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.currentPath())

        self.tree_view.setModel(self.model)
        self.tree_view.setSortingEnabled(True)

        self.tree_view.sortByColumn(True)
        self.tree_view.setRootIndex(self.model.index(ApplicationSettings.DATABROWSER_PATH))



        self.tree_view.setModel(self.model)
        self.tree_view.clicked.connect(self.item_clicked)
        self.tree_view.installEventFilter(self)
        self.tree_view.setColumnWidth(0,200)

    def project_changed(self):
        pass

    def item_clicked(self):
        pass

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False
#
#     def import_file_clicked(self):
#         filepath = self.model.filePath(self.tree_view.currentIndex())
#         if filepath.split('.')[-1] =='csv' or filepath.split('.')[-1] =='CSV':
#             copyfile(filepath, DATA_PATH+'/'+filepath.split('/')[-1])
#         else:
#             pass
#
#     def plot_action_clicked(self):
#         filepath = self.model.filePath(self.tree_view.currentIndex())
#         if filepath.split('.')[-1] =='csv' or filepath.split('.')[-1] =='CSV':
#             data = pd.read_csv(filepath)
#             data.plot(ax=self.main_window.ax, x=0, y=1)
#             # self.main_window.ax.plot(data[0], data[1])
#             self.main_window.canvas.draw()
#         else:
#             pass
#
#     def delete_action_clicked(self):
#         filepath = self.model.filePath(self.tree_view.currentIndex())
#         os.remove(filepath)

