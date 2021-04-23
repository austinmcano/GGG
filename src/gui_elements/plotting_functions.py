from src.Ui_Files.Dialogs.Save_To_CSV import Ui_Dialog as TW_ui
from PySide2 import QtWidgets
import numpy as np
from src.Ui_Files.Dialogs.line_dialog import Ui_Dialog as vhline_ui
from src.Ui_Files.Dialogs.axis_setup_dialog import Ui_Dialog as axis_setup_ui
from src.Ui_Files.Dialogs.Save_To_CSV import Ui_Dialog as STC_ui
from src.Ui_Files.Dialogs.app_settings import Ui_Dialog as app_settings
from src.Ui_Files.Dialogs.annotation_dialog import Ui_Dialog as annotation_ui
from src.Ui_Files.Dialogs.simple_text import Ui_Dialog as simple_text_ui
from src.Ui_Files.Dialogs.new_project_dialog import Ui_Dialog as new_project_dialog
from src.Ui_Files.Dialogs.simple_treeWidget_dialog import Ui_Dialog as simple_tw
from src.Ui_Files.Dialogs.bargraph_dialog import Ui_Dialog as bar_dialog
from src.Ui_Files.Dialogs.spine_color_dialog import Ui_Dialog as spine_color_dialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.pyplot import figure
import matplotlib
import pickle
import pandas as pd
from PySide2 import QtCore,QtWidgets,QtGui
import sys
from shutil import copyfile, copytree, rmtree, copy2
import os
import seaborn as sns
from src.gui_elements.settings import ApplicationSettings
from scipy import integrate
from scipy.linalg import norm
from scipy.signal import savgol_filter
from scipy import sparse
from scipy.sparse.linalg import spsolve

def spine_color_fun(self):
    def finish():
        self.ax.spines['bottom'].set_color(ui.bspine_cb.currentText())
        self.ax.spines['top'].set_color(ui.tspine_cb.currentText())
        self.ax.spines['right'].set_color(ui.rspine_cb.currentText())
        self.ax.spines['left'].set_color(ui.lspine_cb.currentText())
        self.ax.xaxis.label.set_color(ui.bspine_cb.currentText())
        self.ax.yaxis.label.set_color(ui.lspine_cb.currentText())
        self.ax.tick_params(axis='x', colors=ui.bspine_cb.currentText())
        self.ax.tick_params(axis='y', colors=ui.lspine_cb.currentText())
        self.settings.setValue('top_spine_color',ui.tspine_cb.currentText())
        self.settings.setValue('bottom_spine_color', ui.bspine_cb.currentText())
        self.settings.setValue('left_spine_color', ui.lspine_cb.currentText())
        self.settings.setValue('right_spine_color', ui.rspine_cb.currentText())
        if self.ax_2 is not None:
            self.ax_2.tick_params(axis='y', colors=ui.rspine_cb.currentText())
        self.canvas.draw()
    dialog = QtWidgets.QDialog()
    ui = spine_color_dialog()
    ui.setupUi(dialog)
    colors = ['black','red','blue','green','purple','orange','yellow','white']
    ui.bspine_cb.addItems(colors)
    ui.bspine_cb.setCurrentText(self.settings.value('bottom_spine_color'))
    ui.tspine_cb.addItems(colors)
    ui.tspine_cb.setCurrentText(self.settings.value('top_spine_color'))
    ui.lspine_cb.addItems(colors)
    ui.lspine_cb.setCurrentText(self.settings.value('left_spine_color'))
    ui.rspine_cb.addItems(colors)
    ui.rspine_cb.setCurrentText(self.settings.value('right_spine_color'))

    ui.buttonBox.accepted.connect(lambda: finish())
    dialog.exec_()

def graph_test_fun(self):
    path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Pickeled Figure', self.settings.value('FIG_PATH'))
    ax = pickle.load(open(path, 'rb'))
    self.ui.verticalLayout.removeWidget(self.toolbar)
    self.ui.verticalLayout.removeWidget(self.canvas)
    self.toolbar.close()
    self.canvas.close()
    self.ax.remove()
    sns.set(context=self.context, style=self.style, palette=self.c_palette,
            font=self.font, font_scale=self.fs, color_codes=True)
    self.fig = figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    self.canvas = FigureCanvas(self.fig)
    self.ui.verticalLayout.addWidget(NavigationToolbar(self.canvas, self.canvas, coordinates=True))
    self.ui.verticalLayout.addWidget(self.canvas)
    self.ax = ax
    self.canvas.installEventFilter(self)
    self.canvas.draw()

def tight_figure(self):
    self.fig.tight_layout()
    self.canvas.draw()

def save_fig(self):
    def finish():
        text = ui.lineEdit.text()
        # pickle.dump(self.ax, self.settings.value('FIG_PATH') + text, 'w')
        with open(self.settings.value('FIG_PATH') + text, 'wb') as f:  # should be 'wb' rather than 'w'
            pickle.dump(self.fig, f)
    dialog = QtWidgets.QDialog()
    ui = simple_text_ui()
    ui.setupUi(dialog)
    ui.buttonBox.accepted.connect(lambda: finish())
    dialog.exec_()

    # pickle.dump(self.fig, open(ApplicationSettings.FIG_PATH+text, 'wb'))

def show_pickled_fig(self):
    path,ext = QtWidgets.QFileDialog.getOpenFileName(self,'Pickeled Figure',self.settings.value('FIG_PATH'))
    figx = pickle.load(open(path, 'rb'))
    if path == '':
        pass
    else:
        self.ui.verticalLayout.removeWidget(self.toolbar)
        self.ui.verticalLayout.removeWidget(self.canvas)
        self.toolbar.close()
        self.canvas.close()
        sns.set(context=self.context, style=self.style, palette=self.c_palette,
                font=self.font, font_scale=self.fs, color_codes=True)
        self.fig = figx
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.ui.verticalLayout.addWidget(NavigationToolbar(self.canvas, self.canvas, coordinates=True))
        self.ui.verticalLayout.addWidget(self.canvas)

        self.canvas.installEventFilter(self)
        self.canvas.draw()

def Project_view_fun(self):
    self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_ProjectView)
    self.restoreDockWidget(self.dw_ProjectView)
    self.dw_ProjectView.show()

def DataBrowser_view_fun(self):
    self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_Data_Broswer)
    self.restoreDockWidget(self.dw_Data_Broswer)
    self.dw_Data_Broswer.show()

def XPS_view_fun(self):
    self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_XPS)
    self.restoreDockWidget(self.dw_XPS)
    self.dw_XPS.show()

def FTIR_view_fun(self):
    self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_FTIR)
    self.restoreDockWidget(self.dw_FTIR)
    self.dw_FTIR.show()

def QCM_view_fun(self):
    self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_QCM)
    self.restoreDockWidget(self.dw_QCM)
    self.dw_QCM.show()

def XRD_view_fun(self):
    self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_XRD)
    self.restoreDockWidget(self.dw_XRD)
    self.dw_XRD.show()

def SE_view_fun(self):
    self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_SE)
    self.restoreDockWidget(self.dw_SE)
    self.dw_SE.show()

def CF_view_fun(self):
    self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_CF)
    self.restoreDockWidget(self.dw_CF)
    self.dw_CF.show()

def Console_view_fun(self):
    pass
    # import sys
    #
    # from qtpy.QtWidgets import QApplication
    # from pyqtconsole.console import PythonConsole
    #
    # def greet():
    #     print("hello world")
    #
    # if __name__ == '__main__':
    #     appl = QApplication([])
    #
    #     console = PythonConsole()
    #     console.push_local_ns('greet', greet)
    #     console.show()
    #     console.eval_in_thread()
    #     sys.exit(appl.exec_())
    # self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_Console)
    # self.restoreDockWidget(self.dw_Console)
    # self.dw_Console.show()

def Calc_view_fun(self):
    self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dw_calc)
    self.restoreDockWidget(self.dw_calc)
    self.dw_calc.show()

def toggle_legend(self):
    if self.ax.get_legend() is None:
        self.ax.legend()
        leg_1 = self.ax.legend(loc='best')
        leg_1.set_draggable(True)
        self.canvas.draw()
    else:
        self.ax.get_legend().remove()
        if self.ax_2 is not None:
            self.ax_2.get_legend().remove()
        self.canvas.draw()

def Save_All_Plotted(self):
    # names = self.settings.value('Data_Names')
    # if names is None:
    #     pass
    # else:
    #     for i in names:
    #         self.settings.remove(i)
    def temp():
        temp = []
        for ix in ui.treeWidget.selectedIndexes():
            text = ix.data()
            temp.append(text)
            name = os.path.join(self.settings.value('SAVED_DATA_PATH'),ix.data())
            np.savetxt(str(name)+ui.save_as_LE.text()+ui.comboBox.currentText(),
                       ApplicationSettings.ALL_DATA_PLOTTED[ix.data()][0]._xy,delimiter=',')
            print(ApplicationSettings.ALL_DATA_PLOTTED[ix.data()][0]._xy)
    dialog = QtWidgets.QDialog()
    ui = STC_ui()
    ui.setupUi(dialog)
    dict = ApplicationSettings.ALL_DATA_PLOTTED
    Key_List = []
    for i in dict.keys():
        Key_List.append(QtWidgets.QTreeWidgetItem([i]))
    ui.treeWidget.addTopLevelItems(Key_List)
    ui.buttonBox.accepted.connect(lambda: temp())
    ui.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
    dialog.exec_()

def remove_line(self):
    def finish():
        for j in ui.treeWidget.selectedIndexes():
            print(j)
            print(j.data())
            line = ApplicationSettings.ALL_DATA_PLOTTED[j.data()]

            try:
                if isinstance(line, list):
                    try:
                        self.ax.lines.remove(line[0])
                    except ValueError:
                        pass
                    except AttributeError:
                        pass
                    try:
                        self.ax_1.lines.remove(line[0])
                    except ValueError:
                        pass
                    except AttributeError:
                        pass
                    try:
                        self.ax_2.lines.remove(line[0])
                    except ValueError:
                        pass
                    except AttributeError:
                        pass
                    try:
                        self.ax_3.lines.remove(line[0])
                    except ValueError:
                        pass
                    except AttributeError:
                        pass
                    try:
                        self.ax_3.lines.remove(line[0])
                    except ValueError:
                        pass
                    except AttributeError:
                        pass
                    ApplicationSettings.ALL_DATA_PLOTTED.pop(j.data())
                    del line
                    self.canvas.draw()
                elif isinstance(line,matplotlib.lines.Line2D):
                    self.ax.lines.remove(line)
                    ApplicationSettings.ALL_DATA_PLOTTED.pop(j.data())
                    del line
                    self.canvas.draw()
                elif isinstance(line,matplotlib.offsetbox.DraggableAnnotation):
                    print(line)
                    line.remove()
                    ApplicationSettings.ALL_DATA_PLOTTED.pop(j.data())
                    del line
                elif isinstance(line,matplotlib.collections.PolyCollection):
                    print(line)
                    line.remove()
                    ApplicationSettings.ALL_DATA_PLOTTED.pop(j.data())
                    del line
                else:
                    print(line)
                    print(type(line))
                    line_0 = line.lines[0]
                    self.ax.lines.remove(line_0)
                    ApplicationSettings.ALL_DATA_PLOTTED.pop(j.data())
                    del line_0
            except IndexError:
                print("Index Error")
    all_lines = ApplicationSettings.ALL_DATA_PLOTTED
    dialog = QtWidgets.QDialog()
    ui = simple_tw()
    ui.setupUi(dialog)
    ui.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
    Key_List = []
    for i in all_lines.keys():
        Key_List.append(QtWidgets.QTreeWidgetItem([i]))
    ui.treeWidget.addTopLevelItems(Key_List)
    ui.buttonBox.accepted.connect(lambda:finish())
    dialog.exec_()
    self.canvas.draw()

def send_to_cf(self):
    # def finish():
    #     for j in ui.treeWidget.selectedIndexes():
    #         line = ApplicationSettings.ALL_DATA_PLOTTED[j.data()]
    # all_lines = ApplicationSettings.ALL_DATA_PLOTTED
    # dialog = QtWidgets.QDialog()
    # ui = simple_tw()
    # ui.setupUi(dialog)
    # ui.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
    # Key_List = []
    # for i in all_lines.keys():
    #     Key_List.append(QtWidgets.QTreeWidgetItem([i]))
    # ui.treeWidget.addTopLevelItems(Key_List)
    # ui.buttonBox.accepted.connect(lambda:finish())
    # dialog.exec_()
    # self.canvas.draw()
    fit_list = self.dw_SE.fitted_slopes
    self.dw_CF.ui.tableWidget.setRowCount(len(fit_list))
    for row in range(len(fit_list)):
        self.dw_CF.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(fit_list[row])))

def random_c_plot(self):
    Z = np.random.rand(6, 10)
    c = self.ax.pcolor(Z)
    self.canvas.draw()
    self.fig.colorbar(c, ax=self.ax)

def app_settings_fun(self):
    def function():
        self.settings.setValue('app_style',ui.comboBox.currentText())
        os.execl(sys.executable, sys.executable, *sys.argv)
    def change_path(settings_type):
        path = QtWidgets.QFileDialog.getExistingDirectory()
        self.settings.setValue(settings_type, path)
        if settings_type == 'FTIR_PATH':
            self.dw_FTIR.tree_view.setRootIndex(self.dw_FTIR.model.index(path))
        elif settings_type == 'QCM_PATH':
            self.dw_QCM.tree_view.setRootIndex(self.dw_QCM.model.index(path))
        elif settings_type == 'SE_PATH':
            self.dw_SE.tree_view.setRootIndex(self.dw_SE.model.index(path))
        elif settings_type == 'XPS_PATH':
            self.dw_XPS.tree_view.setRootIndex(self.dw_XPS.model.index(path))
        elif settings_type == 'XRD_PATH':
            self.dw_XRD.tree_view.setRootIndex(self.dw_XRD.model.index(path))
        update()
    def update():
        ui.datapath_le.setText(str(self.settings.value('DATA_PATH')))
        ui.projectpath_le.setText(str(self.settings.value('PROJECT_PATH')))
        ui.savepath_le.setText(str(self.settings.value('SAVED_DATA_PATH')))
        ui.fig_path_label.setText(str(self.settings.value('FIG_PATH')))
        ui.ftir_path_label.setText(str(self.settings.value('FTIR_PATH')))
        ui.se_path_label.setText(str(self.settings.value('SE_PATH')))
        ui.qcm_path_label.setText(str(self.settings.value('QCM_PATH')))
        ui.cf_path_label.setText(str(self.settings.value('CF_PATH')))
        ui.xps_path_label.setText(str(self.settings.value('XPS_PATH')))
        ui.xrd_path_label.setText(str(self.settings.value('XRD_PATH')))
        ui.comboBox.setCurrentText(self.settings.value('app_style'))

    d = QtWidgets.QDialog()
    ui = app_settings()
    ui.setupUi(d)
    ui.comboBox.addItems(QtWidgets.QStyleFactory.keys())
    ui.comboBox.addItems(['DarkStyle'])
    ui.comboBox.addItems(['DarkFusion'])
    ui.comboBox.addItems(['GrayFusion'])
    update()
    # ui.buttonBox.accepted.connect(lambda: function())
    ui.comboBox.currentTextChanged.connect(lambda: function())
    ui.changedatapath_pb.clicked.connect(lambda: change_path('DATA_PATH'))
    ui.changesavepath_pb.clicked.connect(lambda: change_path('SAVED_DATA_PATH'))
    ui.changeprojectpath_pb.clicked.connect(lambda: change_path('PROJECT_PATH'))
    ui.change_figpath_pb.clicked.connect(lambda: change_path('FIG_PATH'))
    ui.change_ir_pb.clicked.connect(lambda: change_path('FTIR_PATH'))
    ui.change_qcm_pb.clicked.connect(lambda: change_path('QCM_PATH'))
    ui.change_se_pb.clicked.connect(lambda: change_path('SE_PATH'))
    ui.change_cf_pb.clicked.connect(lambda: change_path('CF_PATH'))
    ui.change_xps_pb.clicked.connect(lambda: change_path('XPS_PATH'))
    ui.changexrdpath_pb.clicked.connect(lambda: change_path('XRD_PATH'))
    d.exec_()

def send_to_custom_data(self):
    pass
    def temp():
        for ix in ui.treeWidget.selectedIndexes():
            text = ix.data()  # or ix.data()
            np.savetxt(ui.save_as_LE.text() + '.csv',
                       ApplicationSettings.ALL_DATA_PLOTTED[text][0]._xy, delimiter=',')
    dialog = QtWidgets.QDialog()
    ui = STC_ui()
    ui.setupUi(dialog)
    dict = ApplicationSettings.ALL_DATA_PLOTTED
    Key_List = []
    for i in dict.keys():
        Key_List.append(QtWidgets.QTreeWidgetItem([i]))
    ui.treeWidget.addTopLevelItems(Key_List)
    ui.buttonBox.accepted.connect(lambda: temp())
    dialog.exec_()

def new_project(self):
    def new_pro(project_name):
        os.makedirs(os.path.join(project_name,ui.project_le.text()))
        os.makedirs(os.path.join(project_name,ui.project_le.text(),'Data'))
        os.makedirs(os.path.join(project_name, ui.project_le.text(), 'Saved'))
        project_path = os.path.join(project_name, ui.project_le.text())

        self.settings.setValue('PROJECT_PATH',project_path)
        self.settings.setValue('SAVED_DATA_PATH', os.path.join(project_path,'Saved'))
        self.settings.setValue('DATA_PATH', os.path.join(project_path, 'Data'))
    dialog_path = QtWidgets.QFileDialog.getExistingDirectory()
    d = QtWidgets.QDialog()
    ui = new_project_dialog()
    ui.setupUi(d)
    ui.buttonBox.accepted.connect(lambda: new_pro(dialog_path))
    d.exec_()

def open_project(self):
    dialog = QtWidgets.QFileDialog.getExistingDirectory()
    self.settings.setValue('PROJECT_PATH', dialog)

def load_data(self):
    temp = self.settings.value()
    key_list = [i for i in temp.keys()]
    for i in key_list:
        data = temp[i][0]._xy.T
        self.ax.plot(data[0],data[1])
    self.canvas.draw()

def import_file(self):
    filepath = QtWidgets.QFileDialog.getOpenFileName()[0]
    try:
        filename = os.path.basename(filepath)
        datapath = self.settings.value('DATA_PATH')
        copy2(filepath, os.path.join(datapath,filename))
    except FileNotFoundError:
        pass

def import_directiory_function(self):
    src_directory = QtWidgets.QFileDialog.getExistingDirectory()
    dirname = src_directory.split('/')[-1]
    print(os.path.join(self.settings.value('DATA_PATH'),dirname))
    copytree(src_directory,os.path.join(self.settings.value('DATA_PATH'),dirname))

def plot_annotation(self):
    def finish():
        if ui.frame_cb.currentText() == 'No Frame':
            ApplicationSettings.ALL_DATA_PLOTTED[ui.text_le.text()] = \
                self.ax.annotate(ui.text_le.text(), xy=(.5, .5),xycoords='figure fraction',horizontalalignment='left',
                                 verticalalignment='top',fontsize=ui.size_sb.value()).draggable()
        else:
            frame = str(ui.frame_cb.currentText())
            # spot = [np.average(ApplicationSettings.C_X_LIM),np.average(ApplicationSettings.C_Y_LIM)]
            # if type(spot[0]) is float and type(spot[1]) is float:
            #     ApplicationSettings.ALL_DATA_PLOTTED[ui.text_le.text()] = self.ax.annotate(ui.text_le.text(),xy=(spot[0],spot[1])).draggable()
            # else:
            ApplicationSettings.ALL_DATA_PLOTTED[ui.text_le.text()] = \
                self.ax.annotate(ui.text_le.text(),xy=(.5, .5), xycoords='figure fraction',horizontalalignment='left',
                                 verticalalignment='top',fontsize=ui.size_sb.value(),
                                 bbox=dict(boxstyle=frame+",pad=0.3", fc=ui.framebgcolor_cb.currentText(),
                                           ec=ui.framecolor_cb.currentText(), lw=ui.framewidth_sb.value())).draggable()
        self.canvas.draw()
    d = QtWidgets.QDialog()
    ui = annotation_ui()
    ui.setupUi(d)
    ui.buttonBox.accepted.connect(lambda: finish())
    d.exec_()

def bar_graph(self):
    def plot_bar():
        N = ui.num_sb.value()
        xlist = ui.x_list.text().split(' ')
        ind = np.arange(N)
        width = float(ui.width_le.text())
        try:
            y1list_ = ui.y1_list.text().split(' ')
            y1list = [float(i) for i in y1list_]
            self.ax.bar(ind, y1list, width, label=ui.label1_le.text())
        except ValueError:
            print('ValueError')
        try:
            y2list_ = ui.y2_list.text().split(' ')
            y2list = [float(i) for i in y2list_]
            self.ax.bar(ind+width, y2list, width, label=ui.label2_le.text())
        except ValueError:
            print('ValueError')
        try:
            y3list_ = ui.y3_list.text().split(' ')
            y3list = [float(i) for i in y3list_]
            self.ax.bar(ind+width+width, y3list, width, label=ui.label3_le.text())
        except ValueError:
            print('ValueError')
        self.bar['xlist'] = ui.x_list.text()
        self.bar['y1list'] = ui.y1_list.text()
        self.bar['y2list'] = ui.y2_list.text()
        self.bar['y3list'] = ui.y3_list.text()
        self.bar['label1'] = ui.label1_le.text()
        self.bar['label2'] = ui.label2_le.text()
        self.bar['label3'] = ui.label3_le.text()
        self.bar['width'] = ui.width_le.text()
        self.bar['num'] = ui.num_sb.value()
        self.ax.set_xticks(ind + width / N, xlist)
        self.ax.legend(loc='best')
        self.canvas.draw()
    d = QtWidgets.QDialog()
    ui = bar_dialog()
    ui.setupUi(d)
    ui.x_list.setText(self.bar['xlist'])
    ui.y1_list.setText(self.bar['y1list'])
    ui.y2_list.setText(self.bar['y2list'])
    ui.y3_list.setText(self.bar['y3list'])
    ui.label1_le.setText(self.bar['label1'])
    ui.label2_le.setText(self.bar['label2'])
    ui.label3_le.setText(self.bar['label3'])
    ui.width_le.setText(self.bar['width'])
    ui.num_sb.setValue(self.bar['num'])
    ui.buttonBox.accepted.connect(lambda: plot_bar())
    d.exec_()

def baseline_als(y, lam, p, niter=10):
    L = len(y)
    D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
    w = np.ones(L)
    for i in range(niter):
        W = sparse.spdiags(w, 0, L, L)
        Z = W + lam * D.dot(D.transpose())
        z = spsolve(Z, w*y)
        w = p * (y > z) + (1-p) * (y < z)
    print(z)
    return z

def fil_cols_fun(self):
    self.ui.tw_x.clear()
    self.ui.tw_y.clear()
    path = self.model.filePath(self.tree_view.currentIndex())
    filename, extension = os.path.splitext(self.model.filePath(self.tree_view.currentIndex()))
    try:
        skip_rows = self.ui.skip_rows_sb.value()
    except AttributeError:
        print('No Skipped Rows')
        skip_rows = 0
    if extension == '.CSV' or extension == '.csv':
        self.data = pd.read_csv(path, delimiter=',', skiprows=skip_rows)
    elif extension == '.xls' or extension == '.xlsx':
        excelfile = pd.ExcelFile(path)
        self.data = pd.read_excel(excelfile, "Sheet1", skiprows=skip_rows)
    elif extension == '.X01':
        self.data = pd.read_csv(path, delimiter='   ', skiprows=48, engine='python')
    elif extension =='.txt':
        self.data = pd.read_csv(path, sep='\t', skiprows=skip_rows)
    else:
        print(extension)
        self.data = pd.read_csv(path, sep='\t')

    strings = [col for col in self.data.columns]
    column_list_x = []
    column_list_y = []
    for i in strings:
        column_list_x.append(QtWidgets.QTreeWidgetItem([i]))
        column_list_y.append(QtWidgets.QTreeWidgetItem([i]))
        self.ui.tw_x.addTopLevelItems(column_list_x)
        self.ui.tw_y.addTopLevelItems(column_list_y)

def change_axis(self,axis):
    if axis =='axis1':
        self.ax = self.ax_1
    elif axis =='axis2':
        self.ax = self.ax_2
    elif axis =='axis3':
        self.ax = self.ax_3
    elif axis =='axis4':
        self.ax = self.ax_4
    try:
        self.ax.callbacks.connect('xlim_changed', self.lims_change)
    except AttributeError:
        print('No Axis made yet')

def axis_setup_fun(self,ax_num):
    self.ax.clear()
    self.fig.clf()
    self.ui.verticalLayout.removeWidget(self.toolbar)
    self.ui.verticalLayout.removeWidget(self.canvas)
    self.toolbar.close()
    self.canvas.close()
    self.fig = figure(num=None, figsize=(8, 6), dpi=80)
    self.canvas = FigureCanvas(self.fig)
    self.toolbar = NavigationToolbar(self.canvas, self.canvas, coordinates=True)
    self.ui.verticalLayout.addWidget(self.toolbar)
    self.ui.verticalLayout.addWidget(self.canvas)
    self.canvas.installEventFilter(self)
    ApplicationSettings.ALL_DATA_PLOTTED = {}
    if ax_num == 1:
        self.ax_1 = self.fig.add_subplot(111)
    elif ax_num == 2:
        self.ax_1 = self.fig.add_subplot(211)
        self.ax_2 = self.fig.add_subplot(212)
    elif ax_num == 3:
        self.ax_1 = self.fig.add_subplot(211)
        self.ax_2 = self.fig.add_subplot(223)
        self.ax_3 = self.fig.add_subplot(224)
    elif ax_num >= 4:
        self.ax_1 = self.fig.add_subplot(221)
        self.ax_2 = self.fig.add_subplot(222)
        self.ax_3 = self.fig.add_subplot(223)
        self.ax_4 = self.fig.add_subplot(224)

    self.ax = self.ax_1

    self.ax.callbacks.connect('xlim_changed', self.lims_change)
    self.fig.tight_layout()
    self.canvas.draw()

def axis_setup_function(self,ax_num):
    def axis_fun():
        self.ax.clear()
        self.fig.clf()
        self.ui.verticalLayout.removeWidget(self.toolbar)
        self.ui.verticalLayout.removeWidget(self.canvas)
        self.toolbar.close()
        self.canvas.close()
        self.fig = figure(num=None, figsize=(8, 6), dpi=80)
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas, self.canvas, coordinates=True)
        self.ui.verticalLayout.addWidget(self.toolbar)
        self.ui.verticalLayout.addWidget(self.canvas)
        self.canvas.installEventFilter(self)
        self.ax.callbacks.connect('xlim_changed', self.lims_change)
        axis1 = ui.axis1_cb.currentText()
        axis2 = ui.axis2_cb.currentText()
        axis3 = ui.axis3_cb.currentText()
        axis4 = ui.axis4_cb.currentText()
        if axis1 == 'ON' and all(i == 'OFF' for i in [axis2,axis3,axis4]):
            self.ax_1 = self.fig.add_subplot(111)
            self.ax_2 = None
            self.ax_3 = None
            self.ax_4 = None
        elif axis1 == 'ON' and axis2 == 'ON' and axis3 == 'OFF' and axis4 == 'OFF':
            self.ax_1 = self.fig.add_subplot(211)
            self.ax_2 = self.fig.add_subplot(212)
            self.ax_3 = None
            self.ax_4 = None
        elif axis1 == 'ON' and axis2 == 'ON' and axis3 == 'ON' and axis4 == 'OFF':
            self.ax_1 = self.fig.add_subplot(211)
            self.ax_2 = self.fig.add_subplot(223)
            self.ax_3 = self.fig.add_subplot(224)
            self.ax_4 = None
        elif axis1 == 'ON' and axis2 == 'ON' and axis3 == 'ON' and axis4 == 'ON':
            self.ax_1 = self.fig.add_subplot(221)
            self.ax_2 = self.fig.add_subplot(222)
            self.ax_3 = self.fig.add_subplot(223)
            self.ax_4 = self.fig.add_subplot(224)
        self.ax = self.ax_1
        self.fig.tight_layout()
        self.canvas.draw()
    dialog = QtWidgets.QDialog()
    ui = axis_setup_ui()
    ui.setupUi(dialog)
    ui.buttonBox.accepted.connect(lambda: axis_fun())
    dialog.exec_()

def add_line_to_graph(self):
    def finish():
        if ui.comboBox.currentText() == 'Verticle Line':
            self.ax.axvline(x=ui.line_pos_sb.value(), linestyle="--", lw=ui.line_width_sb.value(),
                            color=ui.color_cb.currentText())
        elif ui.comboBox.currentText() == 'Horizontal Line':
            self.ax.axhline(y=ui.line_pos_sb.value(), linestyle="--", lw=ui.line_width_sb.value(),
                            color=ui.color_cb.currentText())
        self.canvas.draw()
    d = QtWidgets.QDialog()
    ui = vhline_ui()
    ui.setupUi(d)
    ui.buttonBox.accepted.connect(lambda: finish())
    d.exec_()