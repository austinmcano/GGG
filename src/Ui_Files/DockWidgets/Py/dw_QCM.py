# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_QCM.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(560, 623)
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

        self.gridLayout.addWidget(self.plot_type_cb, 8, 2, 1, 1)

        self.ax_cb = QComboBox(self.dockWidgetContents)
        self.ax_cb.addItem("")
        self.ax_cb.addItem("")
        self.ax_cb.setObjectName(u"ax_cb")

        self.gridLayout.addWidget(self.ax_cb, 8, 1, 1, 1)

        self.cols_plot_pb = QPushButton(self.dockWidgetContents)
        self.cols_plot_pb.setObjectName(u"cols_plot_pb")

        self.gridLayout.addWidget(self.cols_plot_pb, 8, 3, 1, 1)

        self.fill_cols_pb = QPushButton(self.dockWidgetContents)
        self.fill_cols_pb.setObjectName(u"fill_cols_pb")

        self.gridLayout.addWidget(self.fill_cols_pb, 8, 0, 1, 1)

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
        self.adp_time = QDoubleSpinBox(self.Params_Tab)
        self.adp_time.setObjectName(u"adp_time")
        self.adp_time.setMaximum(999999.000000000000000)
        self.adp_time.setValue(61.000000000000000)

        self.gridLayout_2.addWidget(self.adp_time, 12, 1, 1, 1)

        self.wait = QDoubleSpinBox(self.Params_Tab)
        self.wait.setObjectName(u"wait")
        self.wait.setMaximum(99999.000000000000000)
        self.wait.setValue(50.000000000000000)

        self.gridLayout_2.addWidget(self.wait, 4, 1, 1, 1)

        self.num_A = QSpinBox(self.Params_Tab)
        self.num_A.setObjectName(u"num_A")
        self.num_A.setValue(1)

        self.gridLayout_2.addWidget(self.num_A, 1, 1, 1, 1)

        self.bdp_time = QDoubleSpinBox(self.Params_Tab)
        self.bdp_time.setObjectName(u"bdp_time")
        self.bdp_time.setMaximum(99999.000000000000000)
        self.bdp_time.setValue(61.000000000000000)

        self.gridLayout_2.addWidget(self.bdp_time, 12, 3, 1, 1)

        self.start_time = QDoubleSpinBox(self.Params_Tab)
        self.start_time.setObjectName(u"start_time")
        self.start_time.setMaximum(99999.000000000000000)
        self.start_time.setValue(0.000000000000000)

        self.gridLayout_2.addWidget(self.start_time, 13, 1, 1, 1)

        self.label_6 = QLabel(self.Params_Tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 2, 1, 1)

        self.num_exp = QSpinBox(self.Params_Tab)
        self.num_exp.setObjectName(u"num_exp")
        self.num_exp.setMaximum(99999)
        self.num_exp.setValue(100)

        self.gridLayout_2.addWidget(self.num_exp, 13, 3, 1, 1)

        self.label_4 = QLabel(self.Params_Tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 12, 0, 1, 1)

        self.wait_time_label = QLabel(self.Params_Tab)
        self.wait_time_label.setObjectName(u"wait_time_label")

        self.gridLayout_2.addWidget(self.wait_time_label, 4, 0, 1, 1)

        self.textBrowser = QTextBrowser(self.Params_Tab)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_2.addWidget(self.textBrowser, 11, 0, 1, 4)

        self.P_Threshold = QDoubleSpinBox(self.Params_Tab)
        self.P_Threshold.setObjectName(u"P_Threshold")
        self.P_Threshold.setDecimals(3)
        self.P_Threshold.setSingleStep(0.005000000000000)
        self.P_Threshold.setValue(0.050000000000000)

        self.gridLayout_2.addWidget(self.P_Threshold, 2, 1, 1, 1)

        self.numa_label = QLabel(self.Params_Tab)
        self.numa_label.setObjectName(u"numa_label")

        self.gridLayout_2.addWidget(self.numa_label, 1, 0, 1, 1)

        self.pthress_label = QLabel(self.Params_Tab)
        self.pthress_label.setObjectName(u"pthress_label")

        self.gridLayout_2.addWidget(self.pthress_label, 2, 0, 1, 1)

        self.label_13 = QLabel(self.Params_Tab)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 13, 0, 1, 1)

        self.numb_label = QLabel(self.Params_Tab)
        self.numb_label.setObjectName(u"numb_label")

        self.gridLayout_2.addWidget(self.numb_label, 1, 2, 1, 1)

        self.label_9 = QLabel(self.Params_Tab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 12, 2, 1, 1)

        self.label_12 = QLabel(self.Params_Tab)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 13, 2, 1, 1)

        self.label_8 = QLabel(self.Params_Tab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 4, 2, 1, 1)

        self.label_3 = QLabel(self.Params_Tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 5, 2, 1, 1)

        self.pushButton = QPushButton(self.Params_Tab)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 8, 2, 1, 1)

        self.To_Time = QDoubleSpinBox(self.Params_Tab)
        self.To_Time.setObjectName(u"To_Time")
        self.To_Time.setMaximum(99999999.000000000000000)
        self.To_Time.setSingleStep(10.000000000000000)
        self.To_Time.setValue(9999999.000000000000000)

        self.gridLayout_2.addWidget(self.To_Time, 8, 3, 1, 1)

        self.From_Time = QDoubleSpinBox(self.Params_Tab)
        self.From_Time.setObjectName(u"From_Time")
        self.From_Time.setMaximum(9999999999.000000000000000)
        self.From_Time.setSingleStep(10.000000000000000)

        self.gridLayout_2.addWidget(self.From_Time, 5, 3, 1, 1)

        self.Density = QDoubleSpinBox(self.Params_Tab)
        self.Density.setObjectName(u"Density")
        self.Density.setSingleStep(0.100000000000000)
        self.Density.setValue(5.000000000000000)

        self.gridLayout_2.addWidget(self.Density, 4, 3, 1, 1)

        self.time_through_purge = QDoubleSpinBox(self.Params_Tab)
        self.time_through_purge.setObjectName(u"time_through_purge")
        self.time_through_purge.setMaximum(1.000000000000000)
        self.time_through_purge.setSingleStep(0.020000000000000)
        self.time_through_purge.setValue(0.880000000000000)

        self.gridLayout_2.addWidget(self.time_through_purge, 2, 3, 1, 1)

        self.num_B = QSpinBox(self.Params_Tab)
        self.num_B.setObjectName(u"num_B")
        self.num_B.setValue(1)

        self.gridLayout_2.addWidget(self.num_B, 1, 3, 1, 1)

        self.textBrowser_2 = QTextBrowser(self.Params_Tab)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setMaximumSize(QSize(16777215, 150))

        self.gridLayout_2.addWidget(self.textBrowser_2, 0, 0, 1, 4)

        self.line = QFrame(self.Params_Tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 9, 0, 1, 4)

        self.line_7 = QFrame(self.Params_Tab)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 10, 0, 1, 4)

        self.time_option = QComboBox(self.Params_Tab)
        self.time_option.addItem("")
        self.time_option.addItem("")
        self.time_option.setObjectName(u"time_option")

        self.gridLayout_2.addWidget(self.time_option, 5, 0, 1, 2)

        self.tabWidget.addTab(self.Params_Tab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 4, 2, 1, 1)

        self.waittime_sb = QDoubleSpinBox(self.tab)
        self.waittime_sb.setObjectName(u"waittime_sb")
        self.waittime_sb.setValue(28.000000000000000)

        self.gridLayout_4.addWidget(self.waittime_sb, 2, 3, 1, 1)

        self.threshold_sb = QDoubleSpinBox(self.tab)
        self.threshold_sb.setObjectName(u"threshold_sb")
        self.threshold_sb.setSingleStep(0.010000000000000)
        self.threshold_sb.setValue(0.020000000000000)

        self.gridLayout_4.addWidget(self.threshold_sb, 2, 1, 1, 1)

        self.label_16 = QLabel(self.tab)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 2, 0, 1, 1)

        self.label_17 = QLabel(self.tab)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 2, 2, 1, 1)

        self.intmode_rb = QRadioButton(self.tab)
        self.intmode_rb.setObjectName(u"intmode_rb")

        self.gridLayout_4.addWidget(self.intmode_rb, 0, 0, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 4, 0, 1, 1)

        self.num_a_sb = QSpinBox(self.tab)
        self.num_a_sb.setObjectName(u"num_a_sb")

        self.gridLayout_4.addWidget(self.num_a_sb, 4, 1, 1, 1)

        self.num_b_sb = QSpinBox(self.tab)
        self.num_b_sb.setObjectName(u"num_b_sb")

        self.gridLayout_4.addWidget(self.num_b_sb, 4, 3, 1, 1)

        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 5, 0, 1, 1)

        self.adptime_sb = QDoubleSpinBox(self.tab)
        self.adptime_sb.setObjectName(u"adptime_sb")

        self.gridLayout_4.addWidget(self.adptime_sb, 5, 1, 1, 1)

        self.label_15 = QLabel(self.tab)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_4.addWidget(self.label_15, 5, 2, 1, 1)

        self.bdptime_sb = QDoubleSpinBox(self.tab)
        self.bdptime_sb.setObjectName(u"bdptime_sb")

        self.gridLayout_4.addWidget(self.bdptime_sb, 5, 3, 1, 1)

        self.start_pb = QPushButton(self.tab)
        self.start_pb.setObjectName(u"start_pb")

        self.gridLayout_4.addWidget(self.start_pb, 0, 1, 1, 1)

        self.end_pb = QPushButton(self.tab)
        self.end_pb.setObjectName(u"end_pb")

        self.gridLayout_4.addWidget(self.end_pb, 0, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ave_mcpc_label = QLabel(self.tab_2)
        self.ave_mcpc_label.setObjectName(u"ave_mcpc_label")

        self.gridLayout_3.addWidget(self.ave_mcpc_label, 3, 2, 1, 1)

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 5, 0, 1, 2)

        self.ave_mcpahc_label = QLabel(self.tab_2)
        self.ave_mcpahc_label.setObjectName(u"ave_mcpahc_label")

        self.gridLayout_3.addWidget(self.ave_mcpahc_label, 4, 2, 1, 1)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 2)

        self.ave_mcpbhc_label = QLabel(self.tab_2)
        self.ave_mcpbhc_label.setObjectName(u"ave_mcpbhc_label")

        self.gridLayout_3.addWidget(self.ave_mcpbhc_label, 5, 2, 1, 1)

        self.num_doses = QLabel(self.tab_2)
        self.num_doses.setObjectName(u"num_doses")

        self.gridLayout_3.addWidget(self.num_doses, 1, 2, 1, 1)

        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 4, 0, 1, 2)

        self.textEdit = QTextEdit(self.tab_2)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_3.addWidget(self.textEdit, 6, 0, 1, 3)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 2)

        self.textBrowser_3 = QTextBrowser(self.tab_2)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_3.addWidget(self.textBrowser_3, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 5, 0, 1, 4)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        self.tabWidget.setCurrentIndex(1)


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

        self.ax_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Left Ax", None))
        self.ax_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Right Ax", None))

        self.cols_plot_pb.setText(QCoreApplication.translate("DockWidget", u"Plot", None))
        self.fill_cols_pb.setText(QCoreApplication.translate("DockWidget", u"Fill Columns", None))
        ___qtreewidgetitem = self.treeWidget_pressure.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("DockWidget", u"Pressure", None));
        ___qtreewidgetitem1 = self.treeWidget_mass.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("DockWidget", u"Mass", None));
        ___qtreewidgetitem2 = self.treeWidget_time.headerItem()
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("DockWidget", u"Time", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("DockWidget", u"Select Data", None))
        self.label_6.setText(QCoreApplication.translate("DockWidget", u"% Time", None))
        self.label_4.setText(QCoreApplication.translate("DockWidget", u"A D+PTime (s)", None))
        self.wait_time_label.setText(QCoreApplication.translate("DockWidget", u"Wait (s)", None))
        self.textBrowser.setHtml(QCoreApplication.translate("DockWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont'; font-size:13pt;\">Use this section for anything with (mass only) Find the appoximate start time.  A D+P is the A precursor dose + purge time. this needs to be exact,  same for B. The program will find the mass at the interval for the number of exposures </span></p></body></html>", None))
        self.numa_label.setText(QCoreApplication.translate("DockWidget", u"# of A", None))
        self.pthress_label.setText(QCoreApplication.translate("DockWidget", u"Pressure", None))
        self.label_13.setText(QCoreApplication.translate("DockWidget", u"Start Time (s)", None))
        self.numb_label.setText(QCoreApplication.translate("DockWidget", u"# of B", None))
        self.label_9.setText(QCoreApplication.translate("DockWidget", u"B D+P Time (s)", None))
        self.label_12.setText(QCoreApplication.translate("DockWidget", u"Num of Exposures", None))
        self.label_8.setText(QCoreApplication.translate("DockWidget", u"Den. (g/cm3)", None))
        self.label_3.setText(QCoreApplication.translate("DockWidget", u"From To Time (s)", None))
        self.pushButton.setText(QCoreApplication.translate("DockWidget", u"Refresh Params", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("DockWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont'; font-size:13pt;\">Use this section for depositions where the pressure is readable.  # of A and # of B is the number of A and B doses in succession.  Pressure is a setpoint, if the pressure goes up by a certain amount,  it will count as a dose.  % time is saying how far through the purge do you want to count the mass as the mass of the half-cycle.  Wait is a way of eliminating noise by saying the next exposure wont occur until at least the wait time</span></p></body></html>", None))
        self.time_option.setItemText(0, QCoreApplication.translate("DockWidget", u"From:To Time", None))
        self.time_option.setItemText(1, QCoreApplication.translate("DockWidget", u"Plot Limits", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Params_Tab), QCoreApplication.translate("DockWidget", u"Params w/ Pressure", None))
        self.label_7.setText(QCoreApplication.translate("DockWidget", u"Num B", None))
        self.label_16.setText(QCoreApplication.translate("DockWidget", u"Threshold (torr)", None))
        self.label_17.setText(QCoreApplication.translate("DockWidget", u"Wait Time (s)", None))
        self.intmode_rb.setText(QCoreApplication.translate("DockWidget", u"Integrate", None))
        self.label_2.setText(QCoreApplication.translate("DockWidget", u"Num A", None))
        self.label_14.setText(QCoreApplication.translate("DockWidget", u"A Dose+Purge Time", None))
        self.label_15.setText(QCoreApplication.translate("DockWidget", u"B Dose+Purge Time", None))
        self.start_pb.setText(QCoreApplication.translate("DockWidget", u"Start", None))
        self.end_pb.setText(QCoreApplication.translate("DockWidget", u"End", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("DockWidget", u"Integrate Pressure", None))
        self.ave_mcpc_label.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label_11.setText(QCoreApplication.translate("DockWidget", u"Ave Mass Change B", None))
        self.ave_mcpahc_label.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"# Doses", None))
        self.ave_mcpbhc_label.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.num_doses.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label_10.setText(QCoreApplication.translate("DockWidget", u"Ave Mass Change A", None))
        self.label_5.setText(QCoreApplication.translate("DockWidget", u"Average MCPC", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("DockWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont'; font-size:36pt; font-weight:600; font-style:italic; text-decoration: underline;\">UNDER WORK</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("DockWidget", u"Results", None))
    # retranslateUi

