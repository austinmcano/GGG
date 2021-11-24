import matplotlib.lines
import numpy as np

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
from gui_elements.qms_functions import isotopic_prediction

from dataclasses import dataclass

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
        self.colors = [self.ui.color_1, self.ui.color_2, self.ui.color_3, self.ui.color_4, self.ui.color_5,
                       self.ui.color_6, self.ui.color_7, self.ui.color_8, self.ui.color_9, self.ui.color_10,
                       self.ui.color_11, self.ui.color_12, self.ui.color_13, self.ui.color_14, self.ui.color_15,
                       self.ui.color_16, self.ui.color_17, self.ui.color_18, self.ui.color_19, self.ui.color_20
                       ]
        self.ui.secolorpb.setStyleSheet("background-color: {}".format('#ff0000'))
        self.ui.secolorpb.setText('#ff0000')
        for i in self.colors:
            i.setStyleSheet("background-color: {}".format('#ff0000'))
            i.setText('#ff0000')

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
        # self.ui.axischoise_cb.currentTextChanged.connect(lambda: self.change_axis())
        self.ui.selectrange_box.toggled.connect(self.select_fit_range)
        self.ui.plot_qms_pb.clicked.connect(lambda: self.qms_plot())
        # self.ui.abundance_pb.clicked.connect(lambda: self.abundance_plot())

        self.ui.color_1.clicked.connect(lambda: color_test(self.ui.color_1))
        self.ui.color_2.clicked.connect(lambda: color_test(self.ui.color_2))
        self.ui.color_3.clicked.connect(lambda: color_test(self.ui.color_3))
        self.ui.color_4.clicked.connect(lambda: color_test(self.ui.color_4))
        self.ui.color_5.clicked.connect(lambda: color_test(self.ui.color_5))
        self.ui.color_6.clicked.connect(lambda: color_test(self.ui.color_6))
        self.ui.color_7.clicked.connect(lambda: color_test(self.ui.color_7))
        self.ui.color_8.clicked.connect(lambda: color_test(self.ui.color_8))
        self.ui.color_9.clicked.connect(lambda: color_test(self.ui.color_9))
        self.ui.color_10.clicked.connect(lambda: color_test(self.ui.color_10))
        self.ui.color_11.clicked.connect(lambda: color_test(self.ui.color_11))
        self.ui.color_12.clicked.connect(lambda: color_test(self.ui.color_12))
        self.ui.color_13.clicked.connect(lambda: color_test(self.ui.color_13))
        self.ui.color_14.clicked.connect(lambda: color_test(self.ui.color_14))
        self.ui.color_15.clicked.connect(lambda: color_test(self.ui.color_15))
        self.ui.color_16.clicked.connect(lambda: color_test(self.ui.color_16))
        self.ui.color_17.clicked.connect(lambda: color_test(self.ui.color_17))
        self.ui.color_18.clicked.connect(lambda: color_test(self.ui.color_18))
        self.ui.color_19.clicked.connect(lambda: color_test(self.ui.color_19))
        self.ui.color_20.clicked.connect(lambda: color_test(self.ui.color_20))

        self.ui.secolorpb.clicked.connect(lambda: color_test(self.ui.secolorpb))

        self.ui.calc_iso_pb.clicked.connect(lambda: self.calc_iso())

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
            # if self.main_window.ax_2 is None:
            ax = self.main_window.ax.twinx()
            # ax = self.main_window.ax_2
        x = self.ui.tw_x.currentIndex().data()
        y = self.ui.tw_y.currentIndex().data()
        if self.ui.error_checkbox.isChecked() == True:
            err = self.ui.error_tw.currentIndex().data()
            err_data = self.data[err].to_numpy()
        x_data = self.data[x].to_numpy()
        if self.ui.zero_correct_checkb.isChecked():
            for i in self.ui.tw_y.selectedItems():
                y_data = self.data[i.text(0)].to_numpy()
                if self.ui.error_checkbox.isChecked():
                    ApplicationSettings.ALL_DATA_PLOTTED[str(x) + str(i.text(0))] = \
                        ax.errorbar(x_data,y_data-y_data[0], yerr= err_data,  color='blue', marker='.', ms=20, mew=4,
                                        capsize=4, linestyle='')
                else:
                    ApplicationSettings.ALL_DATA_PLOTTED[str(x) + str(i.text(0))] = \
                        ax.plot(x_data, y_data-y_data[0], '.-', label=y, color=self.ui.secolorpb.text(),
                                markersize=self.ui.semarkersize.value())
        elif not self.ui.zero_correct_checkb.isChecked():
            for i in self.ui.tw_y.selectedItems():
                y_data = self.data[i.text(0)].to_numpy()
                if self.ui.error_checkbox.isChecked():
                    ApplicationSettings.ALL_DATA_PLOTTED[str(x) + str(i.text(0))] = \
                        ax.errorbar(x_data, y_data, yerr=err_data,  color='blue', marker='.', ms=20, mew=4,
                                    capsize=4, linestyle='')
                else:
                    ApplicationSettings.ALL_DATA_PLOTTED[str(x) + str(i.text(0))] = \
                        ax.plot(x_data, y_data, '.-',label=y, color=self.ui.secolorpb.text(),
                                markersize=self.ui.semarkersize.value())
        ax.set_xlabel(self.ui.xlabel_le.text())
        ax.set_ylabel(self.ui.ylabel_le.text())
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

    def linear_SE(self):
        def finish():
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
                self.main_window.ax.plot(self.data_x, fit.best_fit,label=name+' Fit')
            self.ui.fit_results_TE.setText(fit.fit_report())
            self.main_window.canvas.draw()

            posnegdict = {'pos':[],'neg':[],'adose':[],'bdose':[]}

            for num in range(len(self.data_y)-1):
                if self.data_y[num+1] > self.data_y[num]:
                    posnegdict['pos'].append(self.data_y[num+1] - self.data_y[num])
                else:
                    posnegdict['neg'].append(self.data_y[num+1] - self.data_y[num])
            for num in range(len(self.data_y)-1):
                if num % 2 == 0:
                    posnegdict['adose'].append(self.data_y[num+1] - self.data_y[num])
                else:
                    posnegdict['bdose'].append(self.data_y[num+1] - self.data_y[num])
            pave = np.average(posnegdict['pos'])
            nave = np.average(posnegdict['neg'])
            aave = np.average(posnegdict['adose'])
            bave = np.average(posnegdict['bdose'])

            self.ui.adosethickchange.setValue(aave)
            self.ui.bdosethickchange.setValue(bave)
            self.ui.posthickchange.setValue(pave)
            self.ui.negthickchange.setValue(nave)
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
        @dataclass
        class fill_data:
            column_list_x = []
            column_list_y = []
            column_list_err = []
        if tab == 'SE':
            self.ui.tw_x.clear()
            self.ui.tw_y.clear()
            self.ui.error_tw.clear()
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
                self.data = pd.read_csv(self.path, sep='\t', skiprows=skip_rows)

            strings = [col for col in self.data.columns]
            for i in strings:
                fill_data.column_list_x.append(QtWidgets.QTreeWidgetItem([i]))
                fill_data.column_list_y.append(QtWidgets.QTreeWidgetItem([i]))
                fill_data.column_list_err.append(QtWidgets.QTreeWidgetItem([i]))
                self.ui.tw_x.addTopLevelItems(fill_data.column_list_x)
                self.ui.tw_y.addTopLevelItems(fill_data.column_list_y)
                self.ui.error_tw.addTopLevelItems(fill_data.column_list_err)
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
            for i in strings:
                fill_data.column_list_x.append(QtWidgets.QTreeWidgetItem([i]))
                fill_data.column_list_y.append(QtWidgets.QTreeWidgetItem([i]))
                fill_data.column_list_err.append(QtWidgets.QTreeWidgetItem([i]))
                self.ui.qmsx_tw.addTopLevelItems(fill_data.column_list_x)
                self.ui.qmsy_tw.addTopLevelItems(fill_data.column_list_y)

    def lin_fit_all_fun(self):
        dict = ApplicationSettings.ALL_DATA_PLOTTED
        keys = dict.keys()
        model = LinearModel()
        listofslopes = []
        names_of_slopes = []

        for i in keys:
            if isinstance(dict[i],list):
                self.data_x = dict[i][0]._xy.T[0]
                self.data_y = dict[i][0]._xy.T[1]
            else:
                self.data_x = dict[i]._xy.T[0]
                self.data_y = dict[i]._xy.T[1]
            # x_lim = ApplicationSettings.C_X_LIM
            pars = model.guess(self.data_y, x=self.data_x)
            fit = model.fit(self.data_y, pars, x=self.data_x)
            self.main_window.ax.plot(self.data_x, fit.best_fit, label=str(i) + '_Fit')
            listofslopes.append(fit.values['slope'])
            names_of_slopes.append(i)
        # print(self.ui.tableWidget.item(0, 1).text())
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
            x_data = np.linspace(0, len(y_data) - 1, len(y_data))
        elif self.ui.plot_type_cb.currentText() == 'Ext. Plot (half-ints)':
            x_data = np.linspace(0, (len(y_data) - 1) / 2, len(y_data))
        elif self.ui.plot_type_cb.currentText() == 'Ext. Plot (third-ints)':
            x_data = np.linspace(0, (len(y_data) - 1) / 3, len(y_data))
        if self.ui.error_checkbox.isChecked():
            err_data = []
            for i in self.ui.error_tw.selectedItems():
                temp = self.data[i.text(0)].to_numpy()
            for j in temp:
                if not np.isnan(j):
                    err_data.append(j)
            ApplicationSettings.ALL_DATA_PLOTTED[name+y] = \
                ax.errorbar(x_data,y_data, yerr= err_data,  color=self.ui.secolorpb.text(), marker='.', ms=20, mew=4,
                            capsize=4, linestyle='')
        else:
            ApplicationSettings.ALL_DATA_PLOTTED[name+y] = \
                ax.plot(x_data, y_data, '.-', label=name+y,
                        color=self.ui.secolorpb.text(), markersize=self.ui.semarkersize.value())

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
        if self.ui.plottype_cb.currentText() == 'X vs Y':
            x_data = self.data[self.ui.qmsx_tw.selectedItems()[0].text(0)].to_numpy()
            ApplicationSettings.ALL_DATA_PLOTTED[y] = \
                ax.plot(x_data, y_data, '.-', label=y)
            ax.set_xlabel('Time')
            ax.set_ylabel('Intensity (mV)')
        elif self.ui.plottype_cb.currentText() == 'Mass Spectrum':
            y_data = y_data[np.logical_not(np.isnan(y_data))]
            ApplicationSettings.ALL_DATA_PLOTTED[name] = \
                ax.plot(np.linspace(self.ui.mass_start_dsb.value(), self.ui.mass_end_dsb.value(), len(y_data)), y_data,'.-', label=y)
            ax.set_xlabel('m/z')
            ax.set_ylabel('Intensity (mV)')
        self.main_window.canvas.draw()

    def abundance_plot(self):
        def finish():
            max_abun = data[1][find_nearest(data[0], ui.m1.value())]
            allabund = [ui.a1, ui.a2, ui.a3, ui.a4, ui.a5, ui.a6, ui.a7, ui.a8]
            allmasses = [ui.m1, ui.m2, ui.m3, ui.m4, ui.m5, ui.m6, ui.m7, ui.m8]
            indexes = [i for i in range(len(allabund)) if allabund[i].value() != 0]

            for i in indexes:
                ApplicationSettings.ALL_DATA_PLOTTED['abundline_' + str(allmasses[i].value())] = \
                    self.main_window.ax.vlines(x=allmasses[i].value(), ymin=0, ymax=allabund[i].value()*max_abun/100,
                                    linestyle="-", lw=3, color='red',label='abundline_'+str(allmasses[i].value()))
                print(ApplicationSettings.ALL_DATA_PLOTTED['abundline_' + str(allmasses[i].value())])
            for i in range(len(self.mslinemass)):
                self.mslinemass[i] = allmasses[i].value()
                self.mslineabund[i] = allabund[i].value()

        try:
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
        except IndexError:
            msg = QtWidgets.QMessageBox()
            msg.setText('Need data to work')
            msg.exec_()

    def removing_qms_lines(self):
        for i in list(ApplicationSettings.ALL_DATA_PLOTTED):
            line = ApplicationSettings.ALL_DATA_PLOTTED[i]
            if isinstance(line, matplotlib.collections.LineCollection):
                line.remove()
                ApplicationSettings.ALL_DATA_PLOTTED.pop(i)
                del line
        self.main_window.canvas.draw()

    def calc_iso(self):
        if self.ui.clear_combo.currentText() == 'Clear Lines On':
            self.removing_qms_lines()
        intensityOS = self.ui.intensityoffset.value()
        self.ui.tableWidget_2.clear()
        checked = [self.ui.species1_cb.isChecked(), self.ui.species2_cb.isChecked(), self.ui.species3_cb.isChecked(),
                   self.ui.species4_cb.isChecked(), self.ui.species5_cb.isChecked(), self.ui.species6_cb.isChecked(),
                   self.ui.species7_cb.isChecked(), self.ui.species8_cb.isChecked(), self.ui.species9_cb.isChecked(),
                   self.ui.species10_cb.isChecked(), self.ui.species11_cb.isChecked(), self.ui.species12_cb.isChecked(),
                   self.ui.species13_cb.isChecked(), self.ui.species14_cb.isChecked(), self.ui.species15_cb.isChecked(),
                   self.ui.species16_cb.isChecked(), self.ui.species17_cb.isChecked(), self.ui.species18_cb.isChecked(),
                   self.ui.species19_cb.isChecked(), self.ui.species20_cb.isChecked()]
        num = 0
        all_species = [self.ui.name1_le.text(), self.ui.name2_le.text(), self.ui.name3_le.text(),
                       self.ui.name4_le.text(), self.ui.name5_le.text(), self.ui.name6_le.text(),
                       self.ui.name7_le.text(), self.ui.name8_le.text(), self.ui.name9_le.text(),
                       self.ui.name10_le.text(), self.ui.name11_le.text(), self.ui.name12_le.text(), self.ui.name13_le.text(),
                       self.ui.name14_le.text(), self.ui.name15_le.text(), self.ui.name16_le.text(),
                       self.ui.name17_le.text(), self.ui.name18_le.text(), self.ui.name19_le.text(),
                       self.ui.name20_le.text()]
        current_colors = [self.ui.color_1.text(), self.ui.color_2.text(), self.ui.color_3.text(),
                          self.ui.color_4.text(), self.ui.color_5.text(), self.ui.color_6.text(),
                          self.ui.color_7.text(), self.ui.color_8.text(), self.ui.color_9.text(),
                          self.ui.color_10.text(), self.ui.color_11.text(), self.ui.color_12.text(), self.ui.color_13.text(),
                          self.ui.color_14.text(), self.ui.color_15.text(), self.ui.color_16.text(),
                          self.ui.color_17.text(), self.ui.color_18.text(), self.ui.color_19.text(),
                          self.ui.color_20.text()]
        alphas = [self.ui.s1_alpha.value(), self.ui.s2_alpha.value(), self.ui.s3_alpha.value(),
                  self.ui.s4_alpha.value(), self.ui.s5_alpha.value(), self.ui.s6_alpha.value(),
                  self.ui.s7_alpha.value(), self.ui.s8_alpha.value(), self.ui.s9_alpha.value(),
                  self.ui.s10_alpha.value(), self.ui.s11_alpha.value(), self.ui.s12_alpha.value(), self.ui.s13_alpha.value(),
                  self.ui.s14_alpha.value(), self.ui.s15_alpha.value(), self.ui.s16_alpha.value(),
                  self.ui.s17_alpha.value(), self.ui.s18_alpha.value(), self.ui.s19_alpha.value(),
                  self.ui.s20_alpha.value()]
        sizes = [self.ui.size1.value(), self.ui.size2.value(), self.ui.size3.value(), self.ui.size4.value(),
                 self.ui.size5.value(), self.ui.size6.value(), self.ui.size7.value(), self.ui.size8.value(),
                 self.ui.size9.value(), self.ui.size10.value(), self.ui.size11.value(), self.ui.size12.value(), self.ui.size13.value(), self.ui.size14.value(),
                 self.ui.size15.value(), self.ui.size16.value(), self.ui.size17.value(), self.ui.size18.value(),
                 self.ui.size19.value(), self.ui.size20.value()]
        if self.ui.type_iso_cb.currentText() == 'User Defined':
            user_ratio = [self.ui.s1ratio.value(), self.ui.s2ratio.value(), self.ui.s3ratio.value(),
                          self.ui.s4ratio.value(), self.ui.s5ratio.value(), self.ui.s6ratio.value(),
                          self.ui.s7ratio.value(), self.ui.s8ratio.value(), self.ui.s9ratio.value(),
                          self.ui.s10ratio.value(), self.ui.s11ratio.value(), self.ui.s12ratio.value(), self.ui.s13ratio.value(),
                          self.ui.s14ratio.value(), self.ui.s15ratio.value(), self.ui.s16ratio.value(),
                          self.ui.s17ratio.value(), self.ui.s18ratio.value(), self.ui.s19ratio.value(),
                          self.ui.s20ratio.value()]

            dict_all = {}
            @dataclass()
            class allspecies:
                mass = []
                abundance = []

            for j in range(len(checked)):
                if checked[j] is True:
                    masses, abunds = isotopic_prediction(all_species[j], round=self.ui.round_mass.value())
                    dict_all[all_species[j]] = [masses+self.ui.mass_offset_dsb.value(), abunds * user_ratio[j],
                                                current_colors[j], num, alphas[j], sizes[j]]
                    num = num + 2
            allmasses = []
            allabund = []
            for i in dict_all.keys():
                for j in range(len(dict_all[i][0])):
                    if dict_all[i][0][j] in allmasses:
                        idx = allmasses.index(dict_all[i][0][j])
                        ApplicationSettings.ALL_DATA_PLOTTED[i + '_'+str(j)] = \
                            self.main_window.ax.vlines(dict_all[i][0][j], allabund[idx]+intensityOS,
                                                       allabund[idx]+dict_all[i][1][j]+intensityOS,
                                                       label='_' + i, linestyle="-", lw=dict_all[i][5], color=dict_all[i][2],
                                                       alpha=dict_all[i][4])
                        allabund[idx] = allabund[idx]+dict_all[i][1][j]
                    else:
                        allmasses.append(dict_all[i][0][j])
                        allabund.append(dict_all[i][1][j])
                        ApplicationSettings.ALL_DATA_PLOTTED[i + '_'+str(j)] = \
                            self.main_window.ax.vlines(dict_all[i][0][j], intensityOS, dict_all[i][1][j]+intensityOS,
                                                       label='_' + i, linestyle="-", lw=dict_all[i][5], color=dict_all[i][2],
                                                       alpha=dict_all[i][4])
                    self.ui.tableWidget_2.setItem(j,dict_all[i][3],QtWidgets.QTableWidgetItem(str(np.round(dict_all[i][0][j],self.ui.round_mass.value()))))
                    self.ui.tableWidget_2.setItem(j, dict_all[i][3]+1, QtWidgets.QTableWidgetItem(str(np.round(dict_all[i][1][j],2))))
                self.ui.tableWidget_2.setHorizontalHeaderItem(dict_all[i][3], QtWidgets.QTableWidgetItem(i+' mass'))
                self.ui.tableWidget_2.setHorizontalHeaderItem(dict_all[i][3]+1, QtWidgets.QTableWidgetItem(i+' abund (mV)'))
        else:
            dict_all = {}
            for j in range(len(checked)):
                if checked[j] is True:
                    masses, abunds = isotopic_prediction(all_species[j], round=self.ui.round_mass.value())
                    dict_all[all_species[j]] = [masses+self.ui.mass_offset_dsb.value(), abunds, current_colors[j],
                                                num, alphas[j], sizes[j]]
                    num = num + 2
            data = self.main_window.ax.lines[0]._xy.T
            for i in dict_all.keys():
                index_ = np.where(dict_all[i][1] == 100)[0][0]
                max_abun = data[1][find_nearest(data[0], dict_all[i][0][index_])]
                for j in range(len(dict_all[i][0])):
                    dict_all[i][1][j] = dict_all[i][1][j] * max_abun / 100
                    ApplicationSettings.ALL_DATA_PLOTTED[i + '_'+str(j)] = \
                        self.main_window.ax.vlines(dict_all[i][0][j], 0, dict_all[i][1][j],
                                                   label='_' + i, linestyle="-", lw=dict_all[i][5], color=dict_all[i][2],
                                                   alpha=dict_all[i][4])
                    self.ui.tableWidget_2.setItem(j,dict_all[i][3],QtWidgets.QTableWidgetItem(str(dict_all[i][0][j]+self.ui.mass_offset_dsb.value())))
                    self.ui.tableWidget_2.setItem(j, dict_all[i][3]+1, QtWidgets.QTableWidgetItem(str(dict_all[i][1][j])))
                self.ui.tableWidget_2.setHorizontalHeaderItem(dict_all[i][3], QtWidgets.QTableWidgetItem(i+' mass'))
                self.ui.tableWidget_2.setHorizontalHeaderItem(dict_all[i][3]+1, QtWidgets.QTableWidgetItem(i+' abund'))
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()
