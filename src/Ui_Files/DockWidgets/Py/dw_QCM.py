# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_QCM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(560, 604)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.plot_type_cb = QComboBox(self.dockWidgetContents)
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.setObjectName(u"plot_type_cb")

        self.gridLayout.addWidget(self.plot_type_cb, 6, 2, 1, 1)

        self.fill_cols_pb = QPushButton(self.dockWidgetContents)
        self.fill_cols_pb.setObjectName(u"fill_cols_pb")

        self.gridLayout.addWidget(self.fill_cols_pb, 6, 0, 1, 1)

        self.cols_plot_pb = QPushButton(self.dockWidgetContents)
        self.cols_plot_pb.setObjectName(u"cols_plot_pb")

        self.gridLayout.addWidget(self.cols_plot_pb, 6, 3, 1, 1)

        self.ax_cb = QComboBox(self.dockWidgetContents)
        self.ax_cb.addItem("")
        self.ax_cb.addItem("")
        self.ax_cb.setObjectName(u"ax_cb")

        self.gridLayout.addWidget(self.ax_cb, 6, 1, 1, 1)

        self.tabWidget = QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.treeWidget_pressure = QTreeWidget(self.tab_3)
        self.treeWidget_pressure.setObjectName(u"treeWidget_pressure")

        self.gridLayout_5.addWidget(self.treeWidget_pressure, 1, 1, 1, 1)

        self.treeWidget_mass = QTreeWidget(self.tab_3)
        self.treeWidget_mass.setObjectName(u"treeWidget_mass")

        self.gridLayout_5.addWidget(self.treeWidget_mass, 1, 2, 1, 1)

        self.treeWidget_time = QTreeWidget(self.tab_3)
        self.treeWidget_time.setObjectName(u"treeWidget_time")

        self.gridLayout_5.addWidget(self.treeWidget_time, 1, 0, 1, 1)

        self.line_3 = QFrame(self.tab_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 2, 0, 1, 3)

        self.QCMtreeView = QTreeView(self.tab_3)
        self.QCMtreeView.setObjectName(u"QCMtreeView")

        self.gridLayout_5.addWidget(self.QCMtreeView, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_3, "")
        self.Params_Tab = QWidget()
        self.Params_Tab.setObjectName(u"Params_Tab")
        self.gridLayout_2 = QGridLayout(self.Params_Tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.Params_Tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 6, 3, 1, 1)

        self.numa_label = QLabel(self.Params_Tab)
        self.numa_label.setObjectName(u"numa_label")

        self.gridLayout_2.addWidget(self.numa_label, 0, 0, 1, 1)

        self.wait_LE = QLineEdit(self.Params_Tab)
        self.wait_LE.setObjectName(u"wait_LE")

        self.gridLayout_2.addWidget(self.wait_LE, 4, 1, 1, 1)

        self.P_Threshold = QLineEdit(self.Params_Tab)
        self.P_Threshold.setObjectName(u"P_Threshold")

        self.gridLayout_2.addWidget(self.P_Threshold, 2, 1, 1, 1)

        self.numb_label = QLabel(self.Params_Tab)
        self.numb_label.setObjectName(u"numb_label")

        self.gridLayout_2.addWidget(self.numb_label, 0, 3, 1, 1)

        self.pushButton = QPushButton(self.Params_Tab)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 9, 3, 1, 1)

        self.To_Time = QLineEdit(self.Params_Tab)
        self.To_Time.setObjectName(u"To_Time")

        self.gridLayout_2.addWidget(self.To_Time, 9, 4, 1, 1)

        self.Density = QLineEdit(self.Params_Tab)
        self.Density.setObjectName(u"Density")

        self.gridLayout_2.addWidget(self.Density, 4, 4, 1, 1)

        self.time_through_purge = QLineEdit(self.Params_Tab)
        self.time_through_purge.setObjectName(u"time_through_purge")

        self.gridLayout_2.addWidget(self.time_through_purge, 2, 4, 1, 1)

        self.label_6 = QLabel(self.Params_Tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 3, 1, 1)

        self.time_option = QComboBox(self.Params_Tab)
        self.time_option.addItem("")
        self.time_option.addItem("")
        self.time_option.setObjectName(u"time_option")

        self.gridLayout_2.addWidget(self.time_option, 6, 0, 1, 2)

        self.From_Time = QLineEdit(self.Params_Tab)
        self.From_Time.setObjectName(u"From_Time")

        self.gridLayout_2.addWidget(self.From_Time, 6, 4, 1, 1)

        self.label_8 = QLabel(self.Params_Tab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 4, 3, 1, 1)

        self.wait_time_label = QLabel(self.Params_Tab)
        self.wait_time_label.setObjectName(u"wait_time_label")

        self.gridLayout_2.addWidget(self.wait_time_label, 4, 0, 1, 1)

        self.pthress_label = QLabel(self.Params_Tab)
        self.pthress_label.setObjectName(u"pthress_label")

        self.gridLayout_2.addWidget(self.pthress_label, 2, 0, 1, 1)

        self.line = QFrame(self.Params_Tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 5)

        self.line_2 = QFrame(self.Params_Tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 5, 0, 1, 5)

        self.num_A = QSpinBox(self.Params_Tab)
        self.num_A.setObjectName(u"num_A")
        self.num_A.setValue(1)

        self.gridLayout_2.addWidget(self.num_A, 0, 1, 1, 1)

        self.num_B = QSpinBox(self.Params_Tab)
        self.num_B.setObjectName(u"num_B")
        self.num_B.setValue(1)

        self.gridLayout_2.addWidget(self.num_B, 0, 4, 1, 1)

        self.tabWidget.addTab(self.Params_Tab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.num_exp_LE = QLineEdit(self.tab)
        self.num_exp_LE.setObjectName(u"num_exp_LE")

        self.gridLayout_4.addWidget(self.num_exp_LE, 4, 1, 1, 1)

        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 4, 0, 1, 1)

        self.adp_time_LE = QLineEdit(self.tab)
        self.adp_time_LE.setObjectName(u"adp_time_LE")

        self.gridLayout_4.addWidget(self.adp_time_LE, 0, 1, 1, 1)

        self.start_time_LE = QLineEdit(self.tab)
        self.start_time_LE.setObjectName(u"start_time_LE")

        self.gridLayout_4.addWidget(self.start_time_LE, 2, 1, 1, 1)

        self.bdp_time_LE = QLineEdit(self.tab)
        self.bdp_time_LE.setObjectName(u"bdp_time_LE")

        self.gridLayout_4.addWidget(self.bdp_time_LE, 0, 3, 1, 1)

        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 2, 2, 1, 1)

        self.end_time_LE = QLineEdit(self.tab)
        self.end_time_LE.setObjectName(u"end_time_LE")

        self.gridLayout_4.addWidget(self.end_time_LE, 2, 3, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 0, 2, 1, 1)

        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 2, 0, 1, 1)

        self.line_4 = QFrame(self.tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_4, 1, 0, 1, 4)

        self.line_5 = QFrame(self.tab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_5, 3, 0, 1, 4)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_19 = QLabel(self.tab_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 2, 3, 1, 1)

        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 3, 3, 1, 1)

        self.total_ml_label = QLabel(self.tab_2)
        self.total_ml_label.setObjectName(u"total_ml_label")

        self.gridLayout_3.addWidget(self.total_ml_label, 0, 3, 1, 1)

        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)

        self.ave_mcpahc_label = QLabel(self.tab_2)
        self.ave_mcpahc_label.setObjectName(u"ave_mcpahc_label")

        self.gridLayout_3.addWidget(self.ave_mcpahc_label, 3, 1, 1, 1)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 4, 3, 1, 1)

        self.ave_mcpbhc_label = QLabel(self.tab_2)
        self.ave_mcpbhc_label.setObjectName(u"ave_mcpbhc_label")

        self.gridLayout_3.addWidget(self.ave_mcpbhc_label, 4, 1, 1, 1)

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 4, 0, 1, 1)

        self.num_doses = QLabel(self.tab_2)
        self.num_doses.setObjectName(u"num_doses")

        self.gridLayout_3.addWidget(self.num_doses, 0, 1, 1, 1)

        self.ave_mcpc_label = QLabel(self.tab_2)
        self.ave_mcpc_label.setObjectName(u"ave_mcpc_label")

        self.gridLayout_3.addWidget(self.ave_mcpc_label, 2, 1, 1, 1)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 4, 2, 1, 1)

        self.label_17 = QLabel(self.tab_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 3, 2, 1, 1)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_20 = QLabel(self.tab_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 2, 2, 1, 1)

        self.textEdit = QTextEdit(self.tab_2)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_3.addWidget(self.textEdit, 5, 0, 1, 4)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 5, 0, 1, 4)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"QCM", None))
        self.plot_type_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Pressure", None))
        self.plot_type_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Mass", None))
        self.plot_type_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"Mass Sub", None))
        self.plot_type_cb.setItemText(3, QCoreApplication.translate("DockWidget", u"Half+Full Cycle", None))
        self.plot_type_cb.setItemText(4, QCoreApplication.translate("DockWidget", u"Half Cycle", None))
        self.plot_type_cb.setItemText(5, QCoreApplication.translate("DockWidget", u"Half+Full Cycle (Mass Only)", None))
        self.plot_type_cb.setItemText(6, QCoreApplication.translate("DockWidget", u"Half Cycle (Mass Only)", None))
        self.plot_type_cb.setItemText(7, QCoreApplication.translate("DockWidget", u"Half+Full Cycle Density", None))
        self.plot_type_cb.setItemText(8, QCoreApplication.translate("DockWidget", u"Half+Full Cycle Density (Mass Only)", None))

        self.fill_cols_pb.setText(QCoreApplication.translate("DockWidget", u"Fill Columns", None))
        self.cols_plot_pb.setText(QCoreApplication.translate("DockWidget", u"Plot", None))
        self.ax_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Left Ax", None))
        self.ax_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Right Ax", None))

        ___qtreewidgetitem = self.treeWidget_pressure.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("DockWidget", u"Pressure", None));
        ___qtreewidgetitem1 = self.treeWidget_mass.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("DockWidget", u"Mass", None));
        ___qtreewidgetitem2 = self.treeWidget_time.headerItem()
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("DockWidget", u"Time", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("DockWidget", u"Columns", None))
        self.label_3.setText(QCoreApplication.translate("DockWidget", u"From To Time (s)", None))
        self.numa_label.setText(QCoreApplication.translate("DockWidget", u"# of A", None))
        self.wait_LE.setText(QCoreApplication.translate("DockWidget", u"58", None))
        self.P_Threshold.setText(QCoreApplication.translate("DockWidget", u"0.05", None))
        self.numb_label.setText(QCoreApplication.translate("DockWidget", u"# of B", None))
        self.pushButton.setText(QCoreApplication.translate("DockWidget", u"Refresh Params", None))
        self.To_Time.setText(QCoreApplication.translate("DockWidget", u"9999999", None))
        self.Density.setText(QCoreApplication.translate("DockWidget", u"1", None))
        self.time_through_purge.setText(QCoreApplication.translate("DockWidget", u".88", None))
        self.label_6.setText(QCoreApplication.translate("DockWidget", u"% Time", None))
        self.time_option.setItemText(0, QCoreApplication.translate("DockWidget", u"From:To Time", None))
        self.time_option.setItemText(1, QCoreApplication.translate("DockWidget", u"Plot Limits", None))

        self.From_Time.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label_8.setText(QCoreApplication.translate("DockWidget", u"Den. (g/cm3)", None))
        self.wait_time_label.setText(QCoreApplication.translate("DockWidget", u"Wait (s)", None))
        self.pthress_label.setText(QCoreApplication.translate("DockWidget", u"Pressure", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Params_Tab), QCoreApplication.translate("DockWidget", u"Params w/ Pressure", None))
        self.num_exp_LE.setText(QCoreApplication.translate("DockWidget", u"100", None))
        self.label_12.setText(QCoreApplication.translate("DockWidget", u"Num of Exposures", None))
        self.adp_time_LE.setText(QCoreApplication.translate("DockWidget", u"61", None))
        self.start_time_LE.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.bdp_time_LE.setText(QCoreApplication.translate("DockWidget", u"61", None))
        self.label_14.setText(QCoreApplication.translate("DockWidget", u"End Time (s)", None))
        self.end_time_LE.setText(QCoreApplication.translate("DockWidget", u"9999", None))
        self.label_4.setText(QCoreApplication.translate("DockWidget", u"A D+PTime (s)", None))
        self.label_9.setText(QCoreApplication.translate("DockWidget", u"B D+P Time (s)", None))
        self.label_13.setText(QCoreApplication.translate("DockWidget", u"Start Time (s)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("DockWidget", u"Params w/ Mass", None))
        self.label_19.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label_16.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.total_ml_label.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label_10.setText(QCoreApplication.translate("DockWidget", u"Ave Mass Change A", None))
        self.ave_mcpahc_label.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label_5.setText(QCoreApplication.translate("DockWidget", u"Average MCPC", None))
        self.label_18.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.ave_mcpbhc_label.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label_11.setText(QCoreApplication.translate("DockWidget", u"Ave Mass Change B", None))
        self.num_doses.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.ave_mcpc_label.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"# Doses", None))
        self.label_15.setText(QCoreApplication.translate("DockWidget", u"StDev", None))
        self.label_17.setText(QCoreApplication.translate("DockWidget", u"StDev", None))
        self.label_2.setText(QCoreApplication.translate("DockWidget", u"Total Mass Lost", None))
        self.label_20.setText(QCoreApplication.translate("DockWidget", u"StDev", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("DockWidget", u"Results", None))
    # retranslateUi

