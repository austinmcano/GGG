from src.Ui_Files.DockWidgets.Py.dw_SE import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
from src.gui_elements.plotting_functions import *
from PySide2 import QtCore,QtWidgets
from lmfit.models import LinearModel
from src.gui_elements.general_functions import *
from src.Ui_Files.Dialogs.simple_treeWidget_dialog import Ui_Dialog as twDialog_ui
from matplotlib.widgets import SpanSelector
from lmfit import Parameters


class SE_view(QtWidgets.QDockWidget):
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
        self.fitted_slopes = None
        self.data_x = None
        self.data_y = None
        self.ui.yaxis_cb.addItems([0,1,2,3,4,5])
        self.path = None

    def _init_widgets(self):
        self.tree_view = self.ui.SE_treeView
        self.context_menu = QtWidgets.QMenu(self)
        # Create context menu
        rc_browser_options(self)
        self.ui.tableWidget.setRowCount(50)

    def _init_UI(self):
        self.model = QtWidgets.QFileSystemModel()
        # self.model.setRootPath(QtCore.QDir.currentPath())
        self.model.setRootPath('')

        self.tree_view.setModel(self.model)
        self.tree_view.setSortingEnabled(True)

        self.tree_view.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.tree_view.setRootIndex(self.model.index(self.main_window.settings.value('SE_PATH')))

        self.tree_view.setModel(self.model)
        self.tree_view.installEventFilter(self)
        self.tree_view.setColumnWidth(0, 200)

        self.ui.tw_y.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        for rows in range(self.ui.tableWidget.rowCount()):
            for cols in range(self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(rows,cols,QtWidgets.QTableWidgetItem('0'))

        self.ui.fill_cols_pb.clicked.connect(lambda: self.fill_cols_fun())
        self.ui.plot_pb.clicked.connect(lambda: self.plot_type_organizer())
        self.ui.lin_fit_pb.clicked.connect(lambda: self.linear_SE())
        self.ui.plottable_pb.clicked.connect(lambda: self.plot_table_data())
        self.ui.linfitall_pb.clicked.connect(lambda: self.lin_fit_all_fun())
        self.ui.axischoise_cb.currentTextChanged.connect(lambda: self.change_axis())
        self.ui.selectrange_box.toggled.connect(self.select_fit_range)

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def plot_type_organizer(self):
        if self.ui.plot_type_cb.currentText() == 'X vs Y':
            self.plot_se()
        elif self.ui.plot_type_cb.currentText() == 'Ext. Plot (half-ints)' or self.ui.plot_type_cb.currentText() == \
                'Ext. Plot (ints)' or self.ui.plot_type_cb.currentText() == 'Ext. Plot (third-ints)':
            self.extended_plot_fun()

    def plot_se(self):
        if self.ui.ax_cb.currentText() == 'Left Ax':
            ax = self.main_window.ax
        elif self.ui.ax_cb.currentText() == 'Right Ax':
            if self.main_window.ax_2 is None:
                self.main_window.ax_2 = self.main_window.ax.twinx()
            ax = self.main_window.ax_2
        x = self.ui.tw_x.currentIndex().data()
        # y = self.ui.tw_y.currentIndex().data()
        x_data = self.data[x].to_numpy()

        if self.ui.zero_correct_checkb.isChecked():
            for i in self.ui.tw_y.selectedItems():
                y_data = self.data[i.text(0)].to_numpy()
                ApplicationSettings.ALL_DATA_PLOTTED[str(x) + str(i.text(0))] = \
                    ax.plot(x_data, y_data-y_data[0],self.ui.linetype_cb.currentText(),label=x)
        elif not self.ui.zero_correct_checkb.isChecked():
            for i in self.ui.tw_y.selectedItems():
                y_data = self.data[i.text(0)].to_numpy()
                ApplicationSettings.ALL_DATA_PLOTTED[str(x) + str(i.text(0))] = \
                    ax.plot(x_data, y_data, self.ui.linetype_cb.currentText(),label=x)
        ax.set_xlabel(self.ui.xlabel_le.text())
        ax.set_ylabel(self.ui.ylabel_le.text())
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

    def linear_SE(self):
        def finish():
            if self.ui.line_name_checkbox.isChecked():
                name = self.ui.line_name_le.text()
            else:
                name = self.ui.tw_y.currentIndex().data()
            if keycheck(dict, name) is True:
                name = name + '_'
            key = ui.treeWidget.currentItem().text(0)
            self.data_x = dict[key][0]._xy.T[0]
            self.data_y = dict[key][0]._xy.T[1]
            model = LinearModel()
            pars = model.guess(self.data_y,x=self.data_x)
            fit = model.fit(self.data_y,pars,x=self.data_x)
            ApplicationSettings.ALL_DATA_PLOTTED[name+' Fit'] = \
                self.main_window.ax.plot(self.data_x,fit.best_fit,label=name+' Fit')
            self.ui.fit_results_TE.setText(fit.fit_report())
            self.main_window.canvas.draw()
        dialog = QtWidgets.QDialog()
        ui = twDialog_ui()
        ui.setupUi(dialog)
        dict = ApplicationSettings.ALL_DATA_PLOTTED
        Key_List = []
        for i in dict.keys():
            Key_List.append(QtWidgets.QTreeWidgetItem([i]))
        ui.treeWidget.addTopLevelItems(Key_List)
        ui.buttonBox.accepted.connect(lambda: finish())
        dialog.exec_()

    def fill_cols_fun(self):
        self.ui.tw_x.clear()
        self.ui.tw_y.clear()
        self.path = self.model.filePath(self.tree_view.currentIndex())
        filename, extension = os.path.splitext(self.model.filePath(self.tree_view.currentIndex()))
        try:
            skip_rows = self.ui.skip_rows_sb.value()
        except AttributeError:
            print('No Skipped Rows')
            skip_rows = 0
        if extension == '.CSV' or extension == '.csv':
            self.data = pd.read_csv(self.path, delimiter=',', skiprows=skip_rows)
        elif extension == '.xls' or extension == '.xlsx':
            excelfile = pd.ExcelFile(self.path)
            self.data = pd.read_excel(excelfile, "Sheet1", skiprows=skip_rows)
        elif extension == '.X01':
            self.data = pd.read_csv(self.path, delimiter='   ', skiprows=48, engine='python')
        elif extension == '.txt':
            self.data = pd.read_csv(self.path, sep='\t', skiprows=skip_rows)
        else:
            print(extension)
            self.data = pd.read_csv(self.path, sep='\t')

        strings = [col for col in self.data.columns]
        column_list_x = []
        column_list_y = []
        for i in strings:
            column_list_x.append(QtWidgets.QTreeWidgetItem([i]))
            column_list_y.append(QtWidgets.QTreeWidgetItem([i]))
            self.ui.tw_x.addTopLevelItems(column_list_x)
            self.ui.tw_y.addTopLevelItems(column_list_y)

    def lin_fit_all_fun(self):
        dict = ApplicationSettings.ALL_DATA_PLOTTED
        keys = dict.keys()
        model = LinearModel()
        listofslopes = []
        names_of_slopes = []
        for i in keys:
            self.data_x = dict[i][0]._xy.T[0]
            self.data_y = dict[i][0]._xy.T[1]
            x_lim = ApplicationSettings.C_X_LIM
            # indexs = [find_nearest(self.data_x, x_lim[0]), find_nearest(self.data_x, x_lim[1])]
            # self.data_x = self.data_x[indexs[0]:indexs[1]]
            # self.data_y = self.data_y[indexs[0]:indexs[1]]
            pars = model.guess(self.data_y, x=self.data_x)
            fit = model.fit(self.data_y, pars, x=self.data_x)
            self.main_window.ax.plot(self.data_x, fit.best_fit, label=str(i) + '_Fit')
            listofslopes.append(fit.values['slope'])
            names_of_slopes.append(i)
        print(self.ui.tableWidget.item(0, 1).text())
        if self.ui.tableWidget.item(0, 1).text() == '0':
            a = 1
        elif self.ui.tableWidget.item(0, 2).text() == '0':
            a = 2
        elif self.ui.tableWidget.item(0, 3).text() == '0':
            a = 3
        elif self.ui.tableWidget.item(0, 4).text() == '0':
            a = 4
        elif self.ui.tableWidget.item(0, 5).text() == '0':
            a = 5
        else:
            print('passed')
        for i in range(len(listofslopes)):
            self.ui.tableWidget.setItem(i,a,QtWidgets.QTableWidgetItem(str(listofslopes[i])))
        print(names_of_slopes)
        print(listofslopes)
        self.main_window.canvas.draw()

    def extended_plot_fun(self):
        name = os.path.basename(self.path)
        if keycheck(ApplicationSettings.ALL_DATA_PLOTTED,name) is True:
                name = name + '_'
        if self.ui.ax_cb.currentText() == 'Left Ax':
            ax = self.main_window.ax
        elif self.ui.ax_cb.currentText() == 'Right Ax':
            # if self.ax_2 is None:
            self.main_window.ax_2 = self.main_window.ax.twinx()
            ax = self.main_window.ax_2
        y_data = []
        for i in self.ui.tw_y.selectedItems():
            temp = self.data[i.text(0)].to_numpy()
            for j in temp:
                if not np.isnan(j):
                    y_data.append(j)
        if self.ui.zero_correct_checkb.isChecked():
            y_data = y_data-y_data[0]
        if self.ui.plot_type_cb.currentText() == 'Ext. Plot (ints)':
            ApplicationSettings.ALL_DATA_PLOTTED[name] = \
                ax.plot(np.linspace(0, len(y_data) - 1, len(y_data)), y_data, '.-',label=name)
        elif self.ui.plot_type_cb.currentText() == 'Ext. Plot (half-ints)':
            ApplicationSettings.ALL_DATA_PLOTTED[name] = \
                ax.plot(np.linspace(0, (len(y_data) - 1) / 2, len(y_data)), y_data,'.-',label=name)
        elif self.ui.plot_type_cb.currentText() == 'Ext. Plot (third-ints)':
            ApplicationSettings.ALL_DATA_PLOTTED[name] = \
                ax.plot(np.linspace(0, (len(y_data) - 1) / 3, len(y_data)), y_data, '.-',label=name)
        ax.set_xlabel(self.ui.xlabel_le.text())
        ax.set_ylabel(self.ui.ylabel_le.text())
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

    def plot_table_data(self):
        rowcount = self.ui.tableWidget.rowCount()
        columncount = self.ui.tableWidget.columnCount()
        data = np.zeros([columncount,rowcount])
        for row in range(rowcount):
            for column in range(columncount):
                data[column][row] = float(self.ui.tableWidget.item(row, column).text())
        x = np.trim_zeros(data[int(self.ui.xaxis_cb.currentText())],'b')
        lenofx = len(x)
        # y = np.trim_zeros(data[int(self.ui.yaxis_cb.currentText())], 'b')
        y= data[int(self.ui.yaxis_cb.currentText())][0:len(x)]
        ApplicationSettings.ALL_DATA_PLOTTED[self.ui.xaxis_cb.currentText()+'_'+self.ui.yaxis_cb.currentText()] = \
            self.main_window.ax.plot(x,y,self.ui.linetype_cb.currentText(), label=self.ui.yaxislabel_le.text())
        self.main_window.ax.set_xlabel(self.ui.xaxislabel_le.text())
        self.main_window.ax.set_ylabel(self.ui.yaxislabel_le.text())
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

    def select_fit_range(self, enabled):
        if enabled:
            self.span = SpanSelector(self.main_window.ax, self.on_select, 'horizontal', useblit=False,
                                     rectprops=dict(alpha=0.2, facecolor='blue'))
        else:
            del self.span

    def on_select(self,minimum, maximum):
        def finish():
            key = ui.treeWidget.currentItem().text(0)
            data_x = ApplicationSettings.ALL_DATA_PLOTTED[key][0]._xy.T[0]
            data_y = ApplicationSettings.ALL_DATA_PLOTTED[key][0]._xy.T[1]
            lims = [find_nearest(data_x, minimum), find_nearest(data_x, maximum)]
            data_x = data_x[lims[0]:lims[1]]
            data_y = data_y[lims[0]:lims[1]]
            model = LinearModel()
            pars = model.guess(data_y,x=data_x)
            result = model.fit(data_y,pars,x=data_x)
            ApplicationSettings.ALL_DATA_PLOTTED[key+'_fit'] = \
                self.main_window.ax.plot(data_x,result.best_fit,'-',label=key+'_fit')
            self.ui.fit_results_TE.setText(result.fit_report())
        dialog = QtWidgets.QDialog()
        ui = twDialog_ui()
        ui.setupUi(dialog)
        Key_List = []
        for i in ApplicationSettings.ALL_DATA_PLOTTED.keys():
            Key_List.append(QtWidgets.QTreeWidgetItem([i]))
        ui.treeWidget.addTopLevelItems(Key_List)
        ui.buttonBox.accepted.connect(lambda: finish())
        dialog.exec_()
        self.ui.selectrange_box.setChecked(False)
        self.main_window.canvas.draw()

# class Fit_Object(object):
#     def __init__(self, x_data,y_data,minimum, maximum):
#         # initialize all class attributes
#         self.peak_constraints = []
#         self.constraints = []
#         self.peak_type = {}
#         self.peak_fitted_values = {}
#         self.shirley = None
#         self.x_data = x_data
#         self.y_data = y_data
#         self.shirley_in_range(minimum, maximum)
#         self.mini = minimum
#         self.maxi = maximum
#         self.init_constraints(minimum, maximum)
#         self.fit_result = None
#
#     def fit(self):
#         self.update_constraints(cons)
#         mod = LinearModel()
#         params = Parameters()
#         params.guess
#         return result