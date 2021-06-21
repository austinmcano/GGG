from Ui_Files.DockWidgets.Py.dw_SE import Ui_DockWidget
from gui_elements.RC_Fucntions import *
from gui_elements.plotting_functions import *
from PySide2 import QtCore,QtWidgets
from lmfit.models import LinearModel
from Ui_Files.Dialogs.simple_treeWidget_dialog import Ui_Dialog as twDialog_ui
from matplotlib.widgets import SpanSelector
from Ui_Files.Dialogs.mass_spec_line_dialog import Ui_Dialog as mslines_ui
import xlrd
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
        self.mslinemass = [100., 101.,102., 103.,104., 105.,106., 107.]
        self.mslineabund = [100., 50., 0.0,0.0,0.0,0.0,0.0,0.0]

    def _init_widgets(self):
        self.tree_view = self.ui.SE_treeView
        self.context_menu = QtWidgets.QMenu(self)
        # Create context menu
        rc_browser_options(self)
        self.ui.tableWidget.setRowCount(50)

    def _init_UI(self):
        self.model = QtWidgets.QFileSystemModel()
        self.modelqms = QtWidgets.QFileSystemModel()
        # self.model.setRootPath(QtCore.QDir.currentPath())
        self.model.setRootPath('')
        self.modelqms.setRootPath('')

        self.tree_view.setModel(self.model)
        self.tree_view.setSortingEnabled(True)
        self.tree_view.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.tree_view.setRootIndex(self.model.index(self.main_window.settings.value('SE_PATH')))
        self.tree_view.setModel(self.model)
        self.tree_view.installEventFilter(self)
        self.tree_view.setColumnWidth(0, 200)

        self.ui.treeView_qms.setModel(self.modelqms)
        self.ui.treeView_qms.setSortingEnabled(True)
        self.ui.treeView_qms.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.ui.treeView_qms.setRootIndex(self.modelqms.index(self.main_window.settings.value('CF_PATH')))
        self.ui.treeView_qms.setModel(self.modelqms)
        self.ui.treeView_qms.installEventFilter(self)
        self.ui.treeView_qms.setColumnWidth(0, 200)

        self.ui.tw_y.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        for rows in range(self.ui.tableWidget.rowCount()):
            for cols in range(self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(rows,cols,QtWidgets.QTableWidgetItem('0'))

        self.ui.fill_cols_pb.clicked.connect(lambda: self.fill_cols_fun('SE'))
        self.ui.fill_cols_qms_pb.clicked.connect(lambda: self.fill_cols_fun('QMS'))
        self.ui.plot_pb.clicked.connect(lambda: self.plot_type_organizer())
        self.ui.lin_fit_pb.clicked.connect(lambda: self.linear_SE())
        self.ui.plottable_pb.clicked.connect(lambda: self.plot_table_data())
        self.ui.linfitall_pb.clicked.connect(lambda: self.lin_fit_all_fun())
        self.ui.axischoise_cb.currentTextChanged.connect(lambda: self.change_axis())
        self.ui.selectrange_box.toggled.connect(self.select_fit_range)
        self.ui.plot_qms_pb.clicked.connect(lambda: self.qms_plot())
        self.ui.abundance_pb.clicked.connect(lambda: self.abundance_plot())

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
        y = self.ui.tw_y.currentIndex().data()
        x_data = self.data[x].to_numpy()

        if self.ui.zero_correct_checkb.isChecked():
            for i in self.ui.tw_y.selectedItems():
                y_data = self.data[i.text(0)].to_numpy()
                ApplicationSettings.ALL_DATA_PLOTTED[str(x) + str(i.text(0))] = \
                    ax.plot(x_data, y_data-y_data[0],'.-',label=y)
        elif not self.ui.zero_correct_checkb.isChecked():
            for i in self.ui.tw_y.selectedItems():
                y_data = self.data[i.text(0)].to_numpy()
                ApplicationSettings.ALL_DATA_PLOTTED[str(x) + str(i.text(0))] = \
                    ax.plot(x_data, y_data, '.-',label=y)
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

    def fill_cols_fun(self, tab):
        if tab == 'SE':
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
        elif tab == 'QMS':
            self.ui.qmsx_tw.clear()
            self.ui.qmsy_tw.clear()
            self.path = self.modelqms.filePath(self.ui.treeView_qms.currentIndex())
            filename, extension = os.path.splitext(self.modelqms.filePath(self.ui.treeView_qms.currentIndex()))
            try:
                skip_rows = self.ui.skiprows_qms_sb.value()
            except AttributeError:
                print('No Skipped Rows')
                skip_rows = 0
            if extension == '.CSV' or extension == '.csv':
                self.data = pd.read_csv(self.path, delimiter=',', skiprows=skip_rows)
            elif extension == '.xls' or extension == '.xlsx':
                try:
                    excelfile = pd.ExcelFile(self.path)
                    self.data = pd.read_excel(excelfile, "Sheet1", skiprows=skip_rows)
                except xlrd.biffh.XLRDError:
                    sheet = QtWidgets.QInputDialog.getText('Sheet Name: ')
                    excelfile = pd.ExcelFile(self.path)
                    self.data = pd.read_excel(excelfile, sheet, skiprows=skip_rows)
            elif extension == '.X01':
                self.data = pd.read_csv(self.path, delimiter='   ', skiprows=48, engine='python')
            elif extension == '.txt':
                self.data = pd.read_csv(self.path, sep='\t', skiprows=skip_rows)
            else:
                print(extension)
                self.data_qms = pd.read_csv(self.path, sep='\t')

            strings = [col for col in self.data.columns]
            column_list_x = []
            column_list_y = []
            for i in strings:
                column_list_x.append(QtWidgets.QTreeWidgetItem([i]))
                column_list_y.append(QtWidgets.QTreeWidgetItem([i]))
                self.ui.qmsx_tw.addTopLevelItems(column_list_x)
                self.ui.qmsy_tw.addTopLevelItems(column_list_y)

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
        y = self.ui.tw_y.currentIndex().data()
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
                ax.plot(np.linspace(0, len(y_data) - 1, len(y_data)), y_data, '.-',label=y)
        elif self.ui.plot_type_cb.currentText() == 'Ext. Plot (half-ints)':
            ApplicationSettings.ALL_DATA_PLOTTED[name] = \
                ax.plot(np.linspace(0, (len(y_data) - 1) / 2, len(y_data)), y_data,'.-',label=y)
        elif self.ui.plot_type_cb.currentText() == 'Ext. Plot (third-ints)':
            ApplicationSettings.ALL_DATA_PLOTTED[name] = \
                ax.plot(np.linspace(0, (len(y_data) - 1) / 3, len(y_data)), y_data, '.-',label=y)
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
            try:
                data_x = ApplicationSettings.ALL_DATA_PLOTTED[key][0]._xy.T[0]
                data_y = ApplicationSettings.ALL_DATA_PLOTTED[key][0]._xy.T[1]
            except TypeError:
                data_x = ApplicationSettings.ALL_DATA_PLOTTED[key]._xy.T[0]
                data_y = ApplicationSettings.ALL_DATA_PLOTTED[key]._xy.T[1]
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

    def qms_plot(self):
        name = os.path.basename(self.path)
        x = self.ui.qmsx_tw.currentIndex().data()
        y = self.ui.qmsy_tw.currentIndex().data()
        if keycheck(ApplicationSettings.ALL_DATA_PLOTTED, name) is True:
            name = name + '_'
        if self.ui.plot_side_cb.currentText() == 'Left':
            ax = self.main_window.ax
        elif self.ui.plot_side_cb.currentText() == 'Right':
            self.main_window.ax_2 = self.main_window.ax.twinx()
            ax = self.main_window.ax_2
        # for i in self.ui.qmsy_tw.selectedItems():
        #     temp = self.data[i.text(0)].to_numpy()
        #     for j in temp:
        #         if not np.isnan(j):
        #             y_data.append(j)
        y_data = self.data[self.ui.qmsy_tw.selectedItems()[0].text(0)].to_numpy()
        x_data = self.data[self.ui.qmsx_tw.selectedItems()[0].text(0)].to_numpy()
        print(x_data)
        if self.ui.plottype_cb.currentText() == 'Mass Spectrum':
            ApplicationSettings.ALL_DATA_PLOTTED[name] = \
                ax.plot(x_data, y_data, '.-', label=y)
            ax.set_xlabel('m/z')
            ax.set_ylabel('Intensity (mV)')
        elif self.ui.plottype_cb.currentText() == 'Mass Trace':
            ApplicationSettings.ALL_DATA_PLOTTED[name] = \
                ax.plot(np.linspace(self.ui.mass_start_dsb.value(), self.ui.mass_end_dsb.value(), len(y_data)), y_data,'.-', label=y)
            ax.set_xlabel('Time (min)')
            ax.set_ylabel('Intensity (mV)')
        self.main_window.canvas.draw()

    def abundance_plot(self):
        def finish():
            max_abun = data[1][find_nearest(data[0], ui.m1.value())]
            allabund = [ui.a1, ui.a2, ui.a3, ui.a4, ui.a5, ui.a6, ui.a7, ui.a8]
            allmasses = [ui.m1, ui.m2, ui.m3, ui.m4, ui.m5, ui.m6, ui.m7, ui.m8]
            indexes = [i for i in range(len(allabund)) if allabund[i].value() != 0]
            rel_abund = []

            for i in indexes:
                ApplicationSettings.ALL_DATA_PLOTTED['abundline_' + str(allmasses[i].value())] = \
                    self.main_window.ax.vlines(x=allmasses[i].value(), ymin=0, ymax=allabund[i].value()*max_abun/100,
                                    linestyle="--", lw=2, color='red')
            for i in range(len(self.mslinemass)):
                self.mslinemass[i] = allmasses[i].value()
                self.mslineabund[i] = allabund[i].value()

        data = self.main_window.ax.lines[0]._xy.T
        d = QtWidgets.QDialog()
        ui = mslines_ui()
        ui.setupUi(d)

        allabund = [ui.a1, ui.a2, ui.a3, ui.a4, ui.a5, ui.a6, ui.a7, ui.a8]
        allmasses = [ui.m1, ui.m2, ui.m3, ui.m4, ui.m5, ui.m6, ui.m7, ui.m8]

        for i in range(len(allabund)):
            allabund[i].setValue(self.mslineabund[i])
            allmasses[i].setValue(self.mslinemass[i])

        ui.buttonBox.accepted.connect(finish)
        d.exec_()
        self.main_window.canvas.draw()

