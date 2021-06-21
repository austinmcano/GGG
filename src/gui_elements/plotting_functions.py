from Ui_Files.Dialogs.Save_To_CSV import Ui_Dialog as TW_ui
from PySide2 import QtWidgets
import numpy as np
from Ui_Files.Dialogs.line_dialog import Ui_Dialog as vhline_ui
from Ui_Files.Dialogs.axis_setup_dialog import Ui_Dialog as axis_setup_ui
from Ui_Files.Dialogs.Save_To_CSV import Ui_Dialog as STC_ui
from Ui_Files.Dialogs.app_settings import Ui_Dialog as app_settings
from Ui_Files.Dialogs.annotation_dialog import Ui_Dialog as annotation_ui
from Ui_Files.Dialogs.simple_text import Ui_Dialog as simple_text_ui
from Ui_Files.Dialogs.new_project_dialog import Ui_Dialog as new_project_dialog
from Ui_Files.Dialogs.simple_treeWidget_dialog import Ui_Dialog as simple_tw
from Ui_Files.Dialogs.bargraph_dialog import Ui_Dialog as bar_dialog
from Ui_Files.Dialogs.spine_color_dialog import Ui_Dialog as spine_color_dialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.pyplot import figure
import matplotlib
import pickle
from matplotlib.text import Text
import pandas as pd
from PySide2 import QtCore,QtWidgets,QtGui
import sys
from shutil import copyfile, copytree, rmtree, copy2
import os
import seaborn as sns
from gui_elements.settings import ApplicationSettings
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
            self.ax_2.yaxis.label.set_color(ui.rspine_cb.currentText())
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
    print(self.fig.canvas.callbacks.callbacks)
    for i in self.fig.canvas.callbacks.callbacks.keys():
        self.fig.canvas.callbacks.mpl_disconnect(i)
        print(i)
    print(self.fig.canvas.callbacks.callbacks)


def tight_figure(self):
    self.fig.tight_layout()
    self.canvas.draw()


def save_fig(self):
    # with open(os.path.join(self.settings.value('FIG_PATH'), 'test' + '.pkl'), 'wb') as fid:
    #     try:
    #         pickle.dump(self.fig, fid)
    #     except TypeError:
    #         msg = QtWidgets.QMessageBox()
    #         msg.setText("Can't save FigureCanvasQtAgg object")
    filename = QtWidgets.QFileDialog.getSaveFileName(None, 'Save Figure', self.settings.value('FIG_PATH'), "pickle (*.pkl);;All Files (*)")
    # text, ok = QtWidgets.QInputDialog.getText(self, 'Saving Figure', 'Save Figure As: ')
    print(filename)
    if filename[0] == '':
        print('passed')
    else:
        with open(filename[0], 'wb') as fid:
            try:
                pickle.dump(self.fig, fid)
            except TypeError:
                msg = QtWidgets.QMessageBox()
                msg.setText("Can't save FigureCanvasQtAgg object")
        msg = QtWidgets.QMessageBox()
        msg.setText('Saved as: ' + filename[0])
        msg.exec_()



def show_pickled_fig(self):
    path,ext = QtWidgets.QFileDialog.getOpenFileName(self,'Pickeled Figure',self.settings.value('FIG_PATH'))
    if path == '':
        pass
    else:
        with open(path, 'rb') as fid:
            try:
                figx = pickle.load(fid)
            except EOFError:
                msg = QtWidgets.QMessageBox()
                msg.setText('There was a problem saving this so there is nothing to load')
                msg.exec_()
        try:
            ApplicationSettings.ALL_DATA_PLOTTED = {}
            self.canvas.draw()
            self.ui.verticalLayout.removeWidget(self.toolbar)
            self.toolbar.close()
            self.ui.verticalLayout.removeWidget(self.canvas)
            self.canvas.close()
            sns.set(context=self.context, style=self.style, palette=self.c_palette,
                    font=self.font, font_scale=self.fs, color_codes=True)
            self.fig = figx
            self.ax_1 = self.fig.axes[0]
            for i in self.ax_1.lines:
                ApplicationSettings.ALL_DATA_PLOTTED[str(i)] = i
            for i in self.ax_1.texts:
                ApplicationSettings.ALL_DATA_PLOTTED[str(i)] = i
            self.ax = self.ax_1
            for ax in self.fig.axes:
                if ax is not self.ax_1:
                    self.ax_2 = ax
                    for i in self.ax_2.lines:
                        ApplicationSettings.ALL_DATA_PLOTTED[str(i)] = i
                    for i in self.ax_2.texts:
                        ApplicationSettings.ALL_DATA_PLOTTED[str(i)] = i
                elif ax is not self.ax_1 and ax is not self.ax_2:
                    self.ax_3 = ax
                    for i in self.ax_3.lines:
                        ApplicationSettings.ALL_DATA_PLOTTED[str(i)] = i
                    for i in self.ax_3.texts:
                        ApplicationSettings.ALL_DATA_PLOTTED[str(i)] = i
                elif ax is not self.ax_1 and ax is not self.ax_2 and ax is not self.ax_3:
                    self.ax_4 = ax
                    for i in self.ax_4.lines:
                        ApplicationSettings.ALL_DATA_PLOTTED[str(i)] = i
                    for i in self.ax_4.texts:
                        ApplicationSettings.ALL_DATA_PLOTTED[str(i)] = i
            self.canvas = FigureCanvas(self.fig)
            self.toolbar = NavigationToolbar(self.canvas, self.canvas, coordinates=True)
            self.ui.verticalLayout.addWidget(self.toolbar)
            self.ui.verticalLayout.addWidget(self.canvas)
            self.canvas.installEventFilter(self)
            self.dragh = DragHandler(self, figure=self.fig)
            self.canvas.draw()
        except UnboundLocalError:
            msg = QtWidgets.QMessageBox()
            msg.setText('Press "Ctrl+1" for a new axes')
            msg.exec_()
# def Project_view_fun(self):
#     self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_ProjectView)
#     self.restoreDockWidget(self.dw_ProjectView)
#     self.dw_ProjectView.show()
#
#
# def DataBrowser_view_fun(self):
#     self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_Data_Broswer)
#     self.restoreDockWidget(self.dw_Data_Broswer)
#     self.dw_Data_Broswer.show()


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
        items = ('medium','xx-small','x-small','small','large','x-large','xx-large')
        size, ok = QtWidgets.QInputDialog.getItem(self, "Legend",
                                        "size", items, 0, False)
        if ok:
            items_2 = ('best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left',
                       'center right', 'lower center', 'upper center', 'center')
            pos, ok_1 = QtWidgets.QInputDialog.getItem(self, "Legend",
                                                       "position", items_2, 0, False)
            if ok_1:
                all, ok_2 = QtWidgets.QInputDialog.getItem(self, "Legend",
                                                           "Combine all Axis Legends? ", ('No','Yes'), 0, False)
                if ok_2:
                    if all == 'Yes':
                        try:
                            lines_1, labels_1 = self.ax_1.get_legend_handles_labels()
                            lines_2, labels_2 = self.ax_2.get_legend_handles_labels()
                            lines = lines_1 + lines_2
                            labels = labels_1 + labels_2
                            self.ax.legend(lines, labels, loc=pos, fontsize = size)
                        except AttributeError:
                            self.ax.legend(loc=pos, fontsize=size)
                    else:
                        self.ax.legend(loc=pos, fontsize=size)
    else:
        self.ax.get_legend().remove()
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
            try:
                np.savetxt(str(name)+ui.save_as_LE.text()+ui.comboBox.currentText(),
                           ApplicationSettings.ALL_DATA_PLOTTED[ix.data()][0]._xy,delimiter=',')
            except TypeError:
                np.savetxt(str(name) + ui.save_as_LE.text() + ui.comboBox.currentText(),
                           ApplicationSettings.ALL_DATA_PLOTTED[ix.data()]._xy, delimiter=',')
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
            line = ApplicationSettings.ALL_DATA_PLOTTED[j.data()]
            if isinstance(line, list):
                try:
                    self.ax.lines.remove(line[0])
                    ApplicationSettings.ALL_DATA_PLOTTED.pop(j.data())
                    del line
                    self.canvas.draw()
                except ValueError:
                    msg = QtWidgets.QMessageBox()
                    msg.setText('Removing Line From Wrong Axes!')
                    msg.exec_()
                except AttributeError:
                    pass
            elif isinstance(line,matplotlib.lines.Line2D):
                try:
                    self.ax.lines.remove(line)
                    ApplicationSettings.ALL_DATA_PLOTTED.pop(j.data())
                    del line
                except ValueError:
                    msg = QtWidgets.QMessageBox()
                    msg.setText('Removing Line From Wrong Axes!')
                    msg.exec_()
            elif isinstance(line, matplotlib.offsetbox.DraggableAnnotation):
                msg = QtWidgets.QMessageBox()
                msg.text("Can't Remove Annotation :(")
                msg.exec_()
            elif isinstance(line, matplotlib.collections.PolyCollection):
                line.remove()
                ApplicationSettings.ALL_DATA_PLOTTED.pop(j.data())
                del line
            elif isinstance(line, matplotlib.text.Text):
                line.remove()
                ApplicationSettings.ALL_DATA_PLOTTED.pop(j.data())
                del line
            elif isinstance(line, matplotlib.collections.LineCollection):
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
        # os.execl(sys.executable, sys.executable, *sys.argv)
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
    ui.buttonBox.accepted.connect(lambda: function())
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
        os.makedirs(os.path.join(project_name, ui.project_le.text(), 'Graphs'))
        project_path = os.path.join(project_name, ui.project_le.text())

        self.settings.setValue('PROJECT_PATH',project_path)
        self.settings.setValue('SAVED_DATA_PATH', os.path.join(project_path,'Saved'))
        self.settings.setValue('DATA_PATH', os.path.join(project_path, 'Data'))
        self.settings.setValue('FIG_PATH', os.path.join(project_path, 'Graphs'))
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
        try:
            a_list = [ui.text.text(), ui.text_2.text(), ui.text_3.text()]
            while ("" in a_list):
                a_list.remove("")
            print(a_list)
            joined_string = "\n".join(a_list)
            print(joined_string)
            if ui.frame.currentText() == 'none':
                bbox = None
            else:
                bbox = dict(dict(boxstyle=ui.frame.currentText(), fc=ui.bgcolor.currentText(), ec="k"))
            ApplicationSettings.ALL_DATA_PLOTTED[ui.text.text()] = \
                self.ax.text(np.average(self.ax.get_xlim()), np.average(self.ax.get_ylim()), joined_string, color=ui.color.currentText(), fontsize=ui.size.value(), picker=True,
                             fontstyle=ui.fontstyle.currentText(), rotation=ui.rotation.value(), bbox=bbox,
                             alpha=ui.alpha.value(),ha=ui.ha_cb.currentText(),va='center')
            self.anno_alpha = ui.alpha.value()
            self.anno_text = ui.text.text()
            self.anno_text_2 = ui.text_2.text()
            self.anno_text_3 = ui.text_3.text()
            self.anno_bgcolor = ui.bgcolor.currentText()
            self.anno_fecolor = ui.framecolor.currentText()
            self.anno_rotation = ui.rotation.value()
            self.anno_color = ui.color.currentText()
            self.anno_frame_width = ui.framewidth_sb.value()
            self.anno_frame = ui.frame.currentText()
            self.anno_style = ui.fontstyle.currentText()
            self.anno_size = ui.size.value()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setText('Annotation Syntax Error')
            msg.exec_()

        self.canvas.draw()
    d = QtWidgets.QDialog()
    ui = annotation_ui()
    ui.setupUi(d)
    ui.bgcolor.addItems(self.color_list)
    ui.framecolor.addItems(self.color_list)
    ui.color.addItems(self.color_list)

    ui.size.setValue(self.anno_size)
    ui.bgcolor.setCurrentText(self.anno_bgcolor)
    ui.color.setCurrentText(self.anno_color)
    ui.framecolor.setCurrentText(self.anno_fecolor)
    ui.frame.setCurrentText(self.anno_frame)
    ui.alpha.setValue(self.anno_alpha)
    ui.text.setText(self.anno_text)
    ui.text_2.setText(self.anno_text_2)
    ui.text_3.setText(self.anno_text_3)
    ui.rotation.setValue(self.anno_rotation)
    ui.framewidth_sb.setValue(self.anno_frame_width)
    ui.fontstyle.setCurrentText(self.anno_style)

    ui.buttonBox.accepted.connect(lambda: finish())
    d.exec_()


def bar_graph(self):
    d = QtWidgets.QDialog()
    ui = bar_dialog()
    ui.setupUi(d)
    l1 = [ui.x_list, ui.y1_list, ui.y2_list, ui.y3_list, ui.label1_le, ui.label2_le, ui.label3_le, ui.width_le, ui.num_sb]
    l2 = ['xlist', 'y1list', 'y2list', 'y3list', 'label1', 'label2', 'label3', 'width', 'num']
    def plot_bar():
        N = ui.num_sb.value()
        width = float(ui.width_le.text())
        labels = ui.x_list.text().split(' ')
        x = np.arange(len(labels))  # the label locations

        if N == 1:
            y1 = [float(i) for i in ui.y1_list.text().split(' ')]
            self.ax.bar(x, y1, width, label=ui.label1_le.text())
        elif N == 2:
            y1 = [float(i) for i in ui.y1_list.text().split(' ')]
            self.ax.bar(x - width / 2, y1, width, label=ui.label1_le.text())
            y2 = [float(i) for i in ui.y2_list.text().split(' ')]
            self.ax.bar(x + width / 2, y2, width, label=ui.label2_le.text())
        elif N == 3:
            y1 = [float(i) for i in ui.y1_list.text().split(' ')]
            self.ax.bar(x - 3*width / 3, y1, width, label=ui.label1_le.text())
            y2 = [float(i) for i in ui.y2_list.text().split(' ')]
            self.ax.bar(x + 3*width / 3, y2, width, label=ui.label2_le.text())
            y3 = [float(i) for i in ui.y3_list.text().split(' ')]
            self.ax.bar(x , y3, width, label=ui.label3_le.text())

        # Add some text for labels, title and custom x-axis tick labels, etc.
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(labels)
        self.ax.legend()

        # self.fig.bar_label(rects1, padding=3)
        # self.fig.bar_label(rects2, padding=3)
        for i in range(len(l1)):
            self.bar[l2[i]] = l1[i].text()
        self.canvas.draw()
    for i in range(len(l1)):
        try:
            l1[i].setText(self.bar[l2[i]])
        except AttributeError:
            l1[i].setValue(int(self.bar[l2[i]]))
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


def fill_cols_fun(self):
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


def move_line(self):
    def finish():
        for j in ui.treeWidget.selectedIndexes():
            line = ApplicationSettings.ALL_DATA_PLOTTED[j.data()]
            print(line)
            print(type(line))
            if isinstance(line, list):
                new_line = line._xy.T[1] + float(ui.lineEdit.text())
                print(new_line)
                ApplicationSettings.ALL_DATA_PLOTTED[j.data() + '_' + str(ui.lineEdit.text())] = self.ax.plot(
                    line._xy.T[0], new_line)
                self.ax.lines.remove(line[0])
                ApplicationSettings.ALL_DATA_PLOTTED.pop(j.data())
                del line
            elif isinstance(line, matplotlib.lines.Line2D):
                new_line = line._xy.T[1] + float(ui.lineEdit.text())
                print(new_line)
                ApplicationSettings.ALL_DATA_PLOTTED[j.data()+'_'+str(ui.lineEdit.text())] = self.ax.plot(
                    line._xy.T[0],new_line)
                self.ax.lines.remove(line)
                ApplicationSettings.ALL_DATA_PLOTTED.pop(j.data())
                del line
            else:
                msg = QtWidgets.QMessageBox()
                msg.setText('Make sure its a line')
                msg.exec_()

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
        self.dragh = DragHandler(self, figure=self.fig)
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
            ApplicationSettings.ALL_DATA_PLOTTED['vline'+str(ui.line_pos_sb.value())] = self.ax.axvline(x=ui.line_pos_sb.value(), linestyle="--", lw=ui.line_width_sb.value(),
                            color=ui.color_cb.currentText())
        elif ui.comboBox.currentText() == 'Horizontal Line':
            ApplicationSettings.ALL_DATA_PLOTTED['hline'+str(ui.line_pos_sb.value())] = self.ax.axhline(y=ui.line_pos_sb.value(), linestyle="--", lw=ui.line_width_sb.value(),
                            color=ui.color_cb.currentText())
        self.canvas.draw()
    d = QtWidgets.QDialog()
    ui = vhline_ui()
    ui.setupUi(d)
    ui.buttonBox.accepted.connect(lambda: finish())
    d.exec_()


def keycheck(dict, key):
    if key in dict.keys():
        return True
    else:
        return False


def addmpl(self,fig):
    self.main_window.canvas = FigureCanvas(fig)
    self.ui.verticalLayout.addWidget(self.main_window.canvas)
    self.main_window.canvas.draw()
    self.toolbar = NavigationToolbar(self.main_window.canvas,
                                     self, coordinates=True)
    self.ui.verticalLayout.addWidget(self.main_window.toolbar)


def rmmpl(self):
    self.ui.verticalLayout.removeWidget(self.main_window.canvas)
    self.main_window.canvas.close()
    self.ui.verticalLayout.removeWidget(self.main_window.toolbar)


def qcm_hc_mass(data, start_time=float, end_time=float, purge_time_a=float, purge_time_b=float, num_cycles=int):
    time = data[0]
    mass = data[2]
    exposure = []
    exposure_idx = []
    mass_hc_a = []
    mass_hc_b = []
    exp_length_idx = []
    # time_in_idx = find_nearest(time, end_time) - find_nearest(time, start_time)
    mass_process = mass[find_nearest(time, start_time): find_nearest(time, end_time)]
    time_process = time[find_nearest(time, start_time):find_nearest(time, end_time)]
    print(time_process)
    print(mass_process)
    for i in range(num_cycles):
        if i % 2 == 0:
            exposure.append(start_time + (purge_time_a * i))
            exposure_idx.append(find_nearest(time_process, start_time + (purge_time_a * i)))
        elif i % 2 == 1:
            exposure.append(start_time + (purge_time_b * i))
            exposure_idx.append(find_nearest(time_process, start_time + (purge_time_b * i)))
    for k in range(len(exposure_idx) - 1):
        exp_length_idx.append(exposure_idx[k + 1] - exposure_idx[k])
    for j in range(num_cycles - 1):
        if j % 2 == 0:
            mass_hc_a.append(
                mass_process[int((exposure_idx[j + 1] - exposure_idx[j]) * .9 + exposure_idx[j])] - mass_process[
                    exposure_idx[j]])
        elif j % 2 == 1:
            mass_hc_b.append(
                mass_process[int((exposure_idx[j + 1] - exposure_idx[j]) * .9 + exposure_idx[j])] - mass_process[
                    exposure_idx[j]])
    fc = np.zeros(len(mass_hc_b))
    for i in range(len(mass_hc_b)):
        fc[i] = mass_hc_a[i]+mass_hc_b[i]
    return mass_hc_a,mass_hc_b, fc


def plot_QCM(self, time,pressure,mass,a_exp=int,b_exp=int,ttp=float,threshold=float,from_time=int,to_time=int,
             wait_time=float, density = float):
    #  Few more assignments Exposures is the time of each Exposure, the Index is just what index it
    #  shows up as. M_Diff and P_Diff are the mass and pressure difference at different exposures
    #  Purge Time Index is the number of data points between one exposure and the next, does not
    #  differentiate for the exposure time.
    Exposures = []
    A_Exposures = a_exp
    Exposure_index = []
    QCM_M_Diff = []
    QCM_P_Diff = []
    MC_A = []
    MC_B = []
    MC_P = []
    MC_N = []
    MC_Cycle = []

    t = 0
    #  Time through purge is the time to "wait" after there is an exposure to not overcount exposures
    #  Time is just a temp variable that gives the time of the last exposure

    # This for loop is just for appending the exposures to Exposures and Exposure_index nee
    for num in range(len(pressure) - 10):
        QCM_M_Diff.append(mass[num + 3] - mass[num])
        QCM_P_Diff.append(pressure[num + 3] - pressure[num])
        if QCM_P_Diff[num] >= threshold and time[num] - t > wait_time and time[num] > from_time and time[num] < to_time:
            Exposures.append(time[num])
            Exposure_index.append(num)
            t = time[num]

            # self.main_window.ax.axvline(time[num], color='gray', lw=1, alpha=0.5)
            # above line will add a line for each exposure if someone is uncertain about if its right

    # This for loop is knowing how long each purge time is (or time from one exposure to next)
    Purge_Time_Index = np.zeros(len(Exposure_index))

    for num in range(len(Exposure_index) - 1):
        if (Exposure_index[num + 1] - Exposure_index[num]) < 2000:
            Purge_Time_Index[num] = Exposure_index[num + 1] - Exposure_index[num]


    Purge_Time_Index[-1] = Purge_Time_Index[0]

    # print(Purge_Time_Index)

    #  for loop finds the mass at the: Exposure time + Purge_time*(time_through_purge) which takes the time
    #  of the last exposure and then adds something like 0.8*Time of purge... Insert is to do the last one
    #  if else says if Mass_Middle was bigger or smaller than the last one and sorts it into one of two lists
    #  Last if else sorts based on if num is odd or even... For A-B experiemtns.. Nothing for A BBB or some
    #  Thing like that
    mass_middle = np.zeros(len(Exposure_index)+2)
    mass_middle[0] = mass[Exposure_index[0] - int(Purge_Time_Index[0] * ttp)]
    # mass_middle.insert(0, mass[Exposure_index[0] - int(Purge_Time_Index[0] * ttp)])

    for num in range(len(Exposure_index)):
        # mass_middle.append(mass[int(Exposure_index[num] + int(Purge_Time_Index[num] * ttp))])
        mass_middle[num+1] = mass[int(Exposure_index[num] + int(Purge_Time_Index[num] * ttp))]
        # self.main_window.ax.axvline(time[num], color='gray', lw=1, alpha=0.5)
        # above line will add a line for each time if someone is uncertain about if its right

    # mass_middle.append(mass[Exposure_index[-1] + int(Purge_Time_Index[0] * ttp)])
    mass_middle[-1] = mass[Exposure_index[-1] + int(Purge_Time_Index[0] * ttp)]

    # print('There was ' + str(len(Exposures)) + '  Precursor Exposures')
    self.main_window.dw_QCM.ui.num_doses.setText(str(len(Exposures)))

    for num in range(len(Exposure_index)):
        if mass_middle[num + 1] - mass_middle[num] > 0:
            MC_P.append(mass_middle[num + 1] - mass_middle[num])
        elif mass_middle[num + 1] - mass_middle[num] < 0:
            MC_N.append(mass_middle[num + 1] - mass_middle[num])
        if num % (b_exp + A_Exposures) == 0:
            MC_Cycle.append(mass_middle[num + b_exp + A_Exposures] - mass_middle[num])
        if num == a_exp - 1:
            MC_A.append(mass_middle[num + 1] - mass_middle[num + 1 - A_Exposures])
        elif num == b_exp + a_exp - 1:
            MC_B.append(mass_middle[num + 1] - mass_middle[num + 1 - b_exp])
        elif num == a_exp + b_exp:
            a_exp = a_exp + A_Exposures + b_exp
            if num == a_exp - 1:
                MC_A.append(mass_middle[num + 1] - mass_middle[
                    num + 1 - A_Exposures])


            # elif num == B_Doses + A_Doses:
            #     self.QCM_Dict['MC_B'].QCM_B.append(Mass_Middle[num] - Mass_Middle[num + 1 - int(B_Exposures.text())])
    half_cycle_density_A = np.zeros(len(MC_A))
    half_cycle_density_B = np.zeros(len(MC_B))
    full_cycle_density = np.zeros(len(MC_Cycle))
    for i in range(len(MC_A)):
        half_cycle_density_A[i] = MC_A[i] / (10.0 * density)
    for i in range(len(MC_B)):
        half_cycle_density_B[i] = MC_B[i] / (10.0 * density)
    for i in range(len(MC_Cycle)):
        full_cycle_density[i] = MC_Cycle[i] / (10 * density)

    return MC_A, MC_B, MC_Cycle, half_cycle_density_A, half_cycle_density_B, full_cycle_density

def find_nearest(array: object, value: object) -> object:
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx


def baseline_als(y, lam, p, niter=10):
    # where y is the data needed to be corrected, lam is lambda and is a smoothing
    # parameter and p is the asymmetry of the baseline, niter is the num of iterations
    L = len(y)
    D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
    w = np.ones(L)
    for i in range(niter):
        W = sparse.spdiags(w, 0, L, L)
        Z = W + lam * D.dot(D.transpose())
        z = spsolve(Z, w*y)
        w = p * (y > z) + (1-p) * (y < z)

def label_size(self):
    size, ok = QtWidgets.QInputDialog.getInt(None, 'Axis Label Size', 'Size: ')
    if ok:
        self.ax_1.set_xlabel(self.ax_1.get_xlabel(), fontsize=size)
        self.ax_1.set_ylabel(self.ax_1.get_ylabel(), fontsize=size)
        self.ax_1.set_xticklabels(self.ax_1.get_xticklabels(), fontsize=size)
        self.ax_1.set_yticklabels(self.ax_1.get_yticklabels(), fontsize=size)
        try:
            self.ax_2.set_xlabel(self.ax_2.get_xlabel(), fontsize=size)
            self.ax_2.set_xticklabels(self.ax_2.get_xticklabels(), fontsize=size)
        except AttributeError:
            print('AttError')
        try:
            self.ax_2.set_ylabel(self.ax_2.get_ylabel(), fontsize=size)
            self.ax_2.set_yticklabels(self.ax_2.get_yticklabels(), fontsize=size)
        except AttributeError:
            print('AttError')
        self.canvas.draw()

class DragHandler(object):
    """ A simple class to handle Drag n Drop.

    This is a simple example, which works for Text objects only
    """
    def __init__(self, main_window, figure=None):
        """ Create a new drag handler and connect it to the figure's event system.
        If the figure handler is not given, the current figure is used instead
        """
        if figure is None : figure = matplotlib.pyplot.gcf()
        # simple attibute to store the dragged text object
        self.dragged = None
        self.main_window = main_window
        # Connect events and callbacks
        figure.canvas.mpl_connect("pick_event", self.on_pick_event)
        figure.canvas.mpl_connect("button_release_event", self.on_release_event)
        # figure.canvas.mpl_connect("button_release_event", self.on_release)

    def on_pick_event(self, event):
        " Store which text object was picked and were the pick event occurs."
        if isinstance(event.artist, Text):
            self.dragged = event.artist
            self.pick_pos = (event.mouseevent.xdata, event.mouseevent.ydata)
        return True

    def on_release_event(self, event):
        " Update text position and redraw"
        if self.dragged is not None:
            old_pos = self.dragged.get_position()
            new_pos = (old_pos[0] + event.xdata - self.pick_pos[0],
                       old_pos[1] + event.ydata - self.pick_pos[1])
            self.dragged.set_position(new_pos)
            self.dragged = None
            self.main_window.canvas.draw()
        return True