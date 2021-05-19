from shutil import copyfile, copytree, rmtree
from src.Ui_Files.Dialogs.Plot_Directory_Functions import Ui_Dialog as Plot_Directory_Functions_Ui
from src.gui_elements.plotting_functions import *
from src.gui_elements.settings import ApplicationSettings
from src.Ui_Files.Dialogs.Plot_Dialog_General import Ui_Dialog as plot_dialog
from src.Ui_Files.Dialogs.simple_text import Ui_Dialog as simple_text_dialog
import os
import glob
import pickle
from src.Ui_Files.Dialogs.delete_dialog import Ui_Dialog as delete_dialog
from src.Ui_Files.Dialogs.simple_tablewidget import Ui_Dialog as tableWidget_dialog


def rc_browser_options(self):
    self.new_menu = self.context_menu.addMenu(' New')
    self.new_file_action = self.new_menu.addAction(' New File')
    self.new_directory_action = self.new_menu.addAction(' New Directory')
    self.import_menu = self.context_menu.addMenu(' Import')
    self.import_file_action = self.import_menu.addAction(' Import File')
    self.import_directory_action = self.import_menu.addAction(' Import Directory')
    self.context_menu.addSeparator()

    self.get_path_action = self.context_menu.addAction('Get Path')
    self.change_path_action = self.context_menu.addAction('Change Path')
    self.context_menu.addSeparator()
    # self.to_root_action = self.context_menu.addAction('Go To Root')
    # self.cut_action = self.context_menu.addAction(' Cut')
    # self.copy_action = self.context_menu.addAction(' Copy')
    # self.paste_action = self.context_menu.addAction(' Paste')
    self.context_menu.addSeparator()
    # self.rename_action = self.context_menu.addAction(' Rename')
    # self.move_action = self.context_menu.addAction(' Move')
    self.delete_action = self.context_menu.addAction(' Delete')
    self.context_menu.addSeparator()
    self.unpickle_action = self.context_menu.addAction('Show Fig')
    # self.new_figure_action = self.context_menu.addAction(' New Figure')
    # self.new_table_action = self.context_menu.addAction(' New Table')
    self.plot_menu = self.context_menu.addMenu('Plot')
    self.plot_action = self.plot_menu.addAction('Plot')
    self.directory_plot_action = self.plot_menu.addAction('Directory Plot')

    self.table_action = self.context_menu.addAction('Table')

    self.context_menu.addSeparator()

    self.graph_options_action = self.context_menu.addAction('Graph Options')

    self.import_file_action.triggered.connect(lambda: import_file_clicked(self))
    self.plot_action.triggered.connect(lambda: plot_action_clicked(self))
    self.delete_action.triggered.connect(lambda: delete_action_clicked(self))
    self.import_directory_action.triggered.connect(lambda: import_directory_clicked(self))
    self.new_directory_action.triggered.connect(lambda: new_directory_clicked(self))
    self.get_path_action.triggered.connect(lambda: get_path_clicked(self))
    # self.graph_options_action.triggered.connect(lambda: Graph_Options(self))
    # self.to_root_action.triggered.connect(lambda: to_root_fun(self))
    self.directory_plot_action.triggered.connect(lambda: plot_directory(self))
    self.unpickle_action.triggered.connect(lambda: show_pickled_fig(self))
    self.table_action.triggered.connect(lambda: table_dialog(self))
    self.change_path_action.triggered.connect(lambda: change_path(self))

def import_file_clicked(self):
    filepath = self.model.filePath(self.tree_view.currentIndex())
    if filepath.split('.')[-1] == 'csv' or filepath.split('.')[-1] == 'CSV':
        copyfile(filepath, ApplicationSettings.DATA_PATH+'/'+filepath.split('/')[-1])
    else:
        pass

def get_path_clicked(self):
    filepath = self.model.filePath(self.tree_view.currentIndex())
    print(filepath)

# def plot_directory(self):
#     pass
#     path = self.model.filePath(self.tree_view.currentIndex())
#
#     plot_dia = QtWidgets.QDialog()
#     plot_dia_ui = Plot_Directory_Functions_Ui()
#     plot_dia_ui.setupUi(plot_dia)
#
#     if os.path.isdir(path):
#         filename, extension = os.path.splitext(path)
#         l = []
#         list_of_csv = sorted(glob.glob(path + '/*CSV'))
#
#         for i in list_of_csv:
#             text = i.split('/')[-1]
#             #  Needed to be a list for some reason, above will only work on macs
#             l.append(QtWidgets.QTreeWidgetItem([text]))
#
#
#         plot_dia_ui.treewidget_list.addTopLevelItems(l)
#
#         # add everything to the tree
#         plot_dia.exec_()
#         from_te = int(plot_dia_ui.lineEdit_from.text())
#         to_te = int(plot_dia_ui.lineEdit_to.text())
#         skip_every = int(plot_dia_ui.lineEdit.text())
#
#         function = plot_dia_ui.treewidget_functions.indexOfTopLevelItem(plot_dia_ui.treewidget_functions.currentItem())
#
#         if function == 0:
#             plot_all_in_directory(self,list_of_csv,from_te,to_te, skip_every)
#         elif function == 1:
#             subtraction_from_survey(self, list_of_csv,from_te,to_te, skip_every)
#         elif function == 2:
#             difference_from_survey(self,list_of_csv,from_te,to_te, skip_every)
#
#         # x = plot_dia_ui.treewidget_list.indexOfTopLevelItem(plot_dia_ui.treewidget_list.currentItem())
#
#         # data_list = [np.genfromtxt(csv) for csv in list_of_csv]
#
#     else:
#         print("Needs to be a directory")

def plot_action_clicked(self):
    path = self.model.filePath(self.tree_view.currentIndex())
    plot_dia = QtWidgets.QDialog()
    plot_dia_ui = plot_dialog()
    plot_dia_ui.setupUi(plot_dia)

    filename, extension = os.path.splitext(path)

    if extension == '.CSV' or extension=='.csv':
        data = np.genfromtxt(path, delimiter=',').T
        strings = [[str(col)] for col in range(len(data))]
        TW1 = plot_dia_ui.treeWidget
        TW2 = plot_dia_ui.treeWidget_2
        column_list_x = []
        column_list_y = []
        for i in strings:
            column_list_x.append(QtWidgets.QTreeWidgetItem(i))
            column_list_y.append(QtWidgets.QTreeWidgetItem(i))

            # l.append(QtWidgets.QTreeWidgetItem(i))  # create QTreeWidgetItem's and append them
        TW1.addTopLevelItems(column_list_x)
        TW2.addTopLevelItems(column_list_y)
        TW2.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        # plot_dia_ui.QP_pushbutton.clicked.connect()
        # add everything to the tree
        plot_dia.exec_()


        data = np.delete(data,[range(int(plot_dia_ui.skip_rows_num.toPlainText()))],1)
        x = TW1.indexOfTopLevelItem(TW1.currentItem())
        y = TW2.indexOfTopLevelItem(TW2.currentItem())
        ApplicationSettings.ALL_DATA_PLOTTED['Plot'] = self.main_window.ax.plot(data[x], data[y])
        self.main_window.ax.set_xlabel(plot_dia_ui.x_label.text())
        self.main_window.ax.set_ylabel(plot_dia_ui.y_label.text())
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

def table_dialog(self):
    path = self.model.filePath(self.tree_view.currentIndex())
    data = np.genfromtxt(path, delimiter=',',dtype='str',missing_values='',skip_header=4).T
    length = len(data)
    data = np.genfromtxt(path, delimiter=',',dtype='str',missing_values=' ',usecols=np.arange(0,length)).T

    plot_dia = QtWidgets.QDialog()
    plot_dia_ui = plot_dialog()
    plot_dia_ui.setupUi(plot_dia)

    dialog = QtWidgets.QDialog()
    ui = tableWidget_dialog()
    ui.setupUi(dialog)

    ui.tableWidget.setColumnCount(len(data))
    ui.tableWidget.setRowCount(len(data[0]))
    print(data)
    for row in range(len(data[0])):
        for column in range(len(data)):
            ui.tableWidget.setItem(row,column,QtWidgets.QTableWidgetItem(data[column][row]))
    dialog.exec_()

def delete_action_clicked(self):
    path = self.model.filePath(self.tree_view.currentIndex())
    msg = QtWidgets.QMessageBox()
    msg.setText('Delete? This cannot be undone.')
    msg.setDetailedText(path)
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
    returnValue = msg.exec()
    if returnValue == QtWidgets.QMessageBox.Ok:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            rmtree(path)


def import_directory_clicked(self):
    dirpath = self.model.filePath(self.tree_view.currentIndex())
    if os.path.isdir(dirpath):
        # dirname = dirpath.split('/')
        copytree(dirpath, ApplicationSettings.DATA_PATH+str(dirpath.split('/')[-1]))
    elif os.path.isfile(dirpath):
        print('isnotdir')

def new_directory_clicked(self):
    simple_text = QtWidgets.QDialog()
    simple_text_ui = simple_text_dialog()
    simple_text_ui.setupUi(simple_text)
    simple_text.exec_()

    text = simple_text_ui.lineEdit.text()
    dirpath = self.model.filePath(self.tree_view.currentIndex())
    newdirpath = dirpath +'/'+ text+'/'

    if not os.path.exists(newdirpath):
        os.mkdir(newdirpath, 0o700)
    else:
        print('Path Exists')
        print(newdirpath)


def change_path(self):
    path = QtWidgets.QFileDialog.getExistingDirectory()
    print(self)
    if type(path) is str:
        self.tree_view.setRootIndex(self.model.index(path))
        self.main_window.settings.setValue('PROJECT_PATH',path)
    else:
        print(path)


def show_pickled_fig(self):
    path = self.model.filePath(self.tree_view.currentIndex())
    figx = pickle.load(open(path, 'rb'))
    # print(self.main_window.ui.verticalLayout)
    print(self.main_window.fig)

    self.main_window.fig = figx
    print(self.main_window.fig)
    self.main_window.canvas.draw()
    # self.main_window.ui.verticalLayout.removeWidget(self.main_window.canvas)
    # self.main_window.ui.verticalLayout.removeWidget(self.main_window.toolbar)
    # self.main_window.canvas.close()
    # self.main_window.toolbar.close()
    # self.main_window.fig = figx
    # self.main_window.canvas = FigureCanvas(figx)
    # self.main_window.ui.gridLayout.addWidget(NavigationToolbar(self.main_window.canvas, self.main_window.canvas, coordinates=True))
    # self.main_window.ui.gridLayout.addWidget(self.main_window.canvas)
    # self.main_window.canvas.installEventFilter(self.main_window)
    # self.main_window.canvas.draw()
