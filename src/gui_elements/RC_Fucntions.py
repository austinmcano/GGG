from gui_elements.plotting_functions import *
from gui_elements.settings import ApplicationSettings
from Ui_Files.Dialogs.Plot_Dialog_General import Ui_Dialog as plot_dialog
from Ui_Files.Dialogs.simple_text import Ui_Dialog as simple_text_dialog
import os
import pickle
from Ui_Files.Dialogs.simple_tablewidget import Ui_Dialog as tableWidget_dialog


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
    self.open_in_action = self.context_menu.addAction('Open In Excel')
    self.context_menu.addSeparator()
    self.context_menu.addSeparator()
    self.delete_action = self.context_menu.addAction(' Delete')
    self.context_menu.addSeparator()
    self.unpickle_action = self.context_menu.addAction('Show Fig')
    self.plot_menu = self.context_menu.addMenu('Plot')
    self.plot_action = self.plot_menu.addAction('Plot')
    self.directory_plot_action = self.plot_menu.addAction('Directory Plot')
    self.table_action = self.context_menu.addAction('Table')
    self.context_menu.addSeparator()
    self.graph_options_action = self.context_menu.addAction('Test')

    self.import_file_action.triggered.connect(lambda: import_file_clicked(self))
    self.plot_action.triggered.connect(lambda: plot_action_clicked(self))
    self.delete_action.triggered.connect(lambda: delete_action_clicked(self))
    self.import_directory_action.triggered.connect(lambda: import_directory_clicked(self))
    self.new_directory_action.triggered.connect(lambda: new_directory_clicked(self))
    self.get_path_action.triggered.connect(lambda: get_path_clicked(self))
    self.unpickle_action.triggered.connect(lambda: show_pickled_fig(self))
    self.table_action.triggered.connect(lambda: table_dialog(self))
    self.change_path_action.triggered.connect(lambda: change_path(self))
    self.open_in_action.triggered.connect(lambda: open_in_excel(self))
    self.graph_options_action.triggered.connect(lambda: test(self))


def test(self):
    print(self)


def open_in_excel(self):
    path = self.model.filePath(self.tree_view.currentIndex())
    os.system("start EXCEL.EXE " + '"' + path + '"')

def import_file_clicked(self):
    filepath = self.model.filePath(self.tree_view.currentIndex())
    if filepath.split('.')[-1] == 'csv' or filepath.split('.')[-1] == 'CSV':
        copyfile(filepath, ApplicationSettings.DATA_PATH+'/'+filepath.split('/')[-1])
    else:
        pass

def get_path_clicked(self):
    filepath = self.model.filePath(self.tree_view.currentIndex())
    msg = QtWidgets.QMessageBox()
    msg.setText(filepath)
    msg.exec_()

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
    # data = np.genfromtxt(path, delimiter=',',dtype='str',missing_values='',skip_header=4).T
    #     length = len(data)
    # data = np.genfromtxt(path, delimiter=',',dtype='str',missing_values=' ',usecols=np.arange(0,length)).T

    path = self.model.filePath(self.tree_view.currentIndex())
    filename, extension = os.path.splitext(self.model.filePath(self.tree_view.currentIndex()))
    # try:
    #     skip_rows = self.ui.skip_rows_sb.value()
    # except AttributeError:
    #     print('No Skipped Rows')
    #     skip_rows = 0
    if extension == '.CSV' or extension == '.csv':
        data = pd.read_csv(path, delimiter=',')
    elif extension == '.xls' or extension == '.xlsx':
        excelfile = pd.ExcelFile(path)
        data = pd.read_excel(excelfile, "Sheet1")
    elif extension == '.X01':
        data = pd.read_csv(path, delimiter='   ', engine='python')
    elif extension == '.txt':
        data = pd.read_csv(path, sep='\t')
    elif extension == '.dat':
        data = pd.read_csv(path, sep=' ')
    else:
        print(extension)
        data = pd.read_csv(path, sep='\t')
    plot_dia = QtWidgets.QDialog()
    plot_dia_ui = plot_dialog()
    plot_dia_ui.setupUi(plot_dia)

    dialog = QtWidgets.QDialog()
    ui = tableWidget_dialog()
    ui.setupUi(dialog)

    ui.tableWidget.setColumnCount(data.shape[1])
    ui.tableWidget.setRowCount(data.shape[0]+1)
    df_keys = data.keys()
    for i,key in enumerate(df_keys):
        ui.tableWidget.setItem(0, i, QtWidgets.QTableWidgetItem(key))
        for j in range(data.shape[0]-1):
            print(data[key][j])
            ui.tableWidget.setItem(j+1, i, QtWidgets.QTableWidgetItem(str(data[key][j])))
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
