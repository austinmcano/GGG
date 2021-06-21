# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_SE.ui'
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
        DockWidget.resize(553, 583)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.plot_type_cb = QComboBox(self.tab_3)
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.setObjectName(u"plot_type_cb")

        self.gridLayout_3.addWidget(self.plot_type_cb, 11, 2, 1, 1)

        self.xlabel_le = QLineEdit(self.tab_3)
        self.xlabel_le.setObjectName(u"xlabel_le")

        self.gridLayout_3.addWidget(self.xlabel_le, 4, 2, 1, 2)

        self.ylabel_le = QLineEdit(self.tab_3)
        self.ylabel_le.setObjectName(u"ylabel_le")

        self.gridLayout_3.addWidget(self.ylabel_le, 5, 2, 1, 2)

        self.fill_cols_pb = QPushButton(self.tab_3)
        self.fill_cols_pb.setObjectName(u"fill_cols_pb")

        self.gridLayout_3.addWidget(self.fill_cols_pb, 11, 1, 1, 1)

        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 5, 1, 1, 1)

        self.zero_correct_checkb = QCheckBox(self.tab_3)
        self.zero_correct_checkb.setObjectName(u"zero_correct_checkb")
        self.zero_correct_checkb.setChecked(False)

        self.gridLayout_3.addWidget(self.zero_correct_checkb, 7, 1, 1, 1)

        self.SE_treeView = QTreeView(self.tab_3)
        self.SE_treeView.setObjectName(u"SE_treeView")

        self.gridLayout_3.addWidget(self.SE_treeView, 0, 1, 1, 3)

        self.tw_x = QTreeWidget(self.tab_3)
        self.tw_x.setObjectName(u"tw_x")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tw_x.sizePolicy().hasHeightForWidth())
        self.tw_x.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.tw_x, 1, 1, 1, 1)

        self.tw_y = QTreeWidget(self.tab_3)
        self.tw_y.setObjectName(u"tw_y")
        self.tw_y.setSelectionMode(QAbstractItemView.SingleSelection)

        self.gridLayout_3.addWidget(self.tw_y, 1, 2, 1, 2)

        self.plot_pb = QPushButton(self.tab_3)
        self.plot_pb.setObjectName(u"plot_pb")

        self.gridLayout_3.addWidget(self.plot_pb, 11, 3, 1, 1)

        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 4, 1, 1, 1)

        self.ax_cb = QComboBox(self.tab_3)
        self.ax_cb.addItem("")
        self.ax_cb.addItem("")
        self.ax_cb.setObjectName(u"ax_cb")

        self.gridLayout_3.addWidget(self.ax_cb, 7, 2, 1, 1)

        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 8, 1, 1, 1)

        self.skip_rows_sb = QSpinBox(self.tab_3)
        self.skip_rows_sb.setObjectName(u"skip_rows_sb")

        self.gridLayout_3.addWidget(self.skip_rows_sb, 8, 2, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 150))

        self.gridLayout_5.addWidget(self.textBrowser, 3, 0, 1, 5)

        self.fit_results_TE = QTextEdit(self.tab_2)
        self.fit_results_TE.setObjectName(u"fit_results_TE")

        self.gridLayout_5.addWidget(self.fit_results_TE, 4, 0, 1, 5)

        self.selectrange_box = QCheckBox(self.tab_2)
        self.selectrange_box.setObjectName(u"selectrange_box")

        self.gridLayout_5.addWidget(self.selectrange_box, 1, 1, 1, 1)

        self.axischoise_cb = QComboBox(self.tab_2)
        self.axischoise_cb.addItem("")
        self.axischoise_cb.addItem("")
        self.axischoise_cb.addItem("")
        self.axischoise_cb.addItem("")
        self.axischoise_cb.setObjectName(u"axischoise_cb")

        self.gridLayout_5.addWidget(self.axischoise_cb, 1, 0, 1, 1)

        self.lin_fit_pb = QPushButton(self.tab_2)
        self.lin_fit_pb.setObjectName(u"lin_fit_pb")

        self.gridLayout_5.addWidget(self.lin_fit_pb, 5, 1, 1, 2)

        self.linfitall_pb = QPushButton(self.tab_2)
        self.linfitall_pb.setObjectName(u"linfitall_pb")

        self.gridLayout_5.addWidget(self.linfitall_pb, 5, 3, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plot_side_cb = QComboBox(self.tab)
        self.plot_side_cb.addItem("")
        self.plot_side_cb.addItem("")
        self.plot_side_cb.setObjectName(u"plot_side_cb")

        self.gridLayout_2.addWidget(self.plot_side_cb, 9, 1, 1, 1)

        self.mass_start_dsb = QDoubleSpinBox(self.tab)
        self.mass_start_dsb.setObjectName(u"mass_start_dsb")
        self.mass_start_dsb.setMaximum(1000.000000000000000)
        self.mass_start_dsb.setValue(30.000000000000000)

        self.gridLayout_2.addWidget(self.mass_start_dsb, 3, 1, 1, 1)

        self.mass_end_dsb = QDoubleSpinBox(self.tab)
        self.mass_end_dsb.setObjectName(u"mass_end_dsb")
        self.mass_end_dsb.setMaximum(1000.000000000000000)
        self.mass_end_dsb.setValue(300.000000000000000)

        self.gridLayout_2.addWidget(self.mass_end_dsb, 4, 1, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.plottype_cb = QComboBox(self.tab)
        self.plottype_cb.addItem("")
        self.plottype_cb.addItem("")
        self.plottype_cb.setObjectName(u"plottype_cb")

        self.gridLayout_2.addWidget(self.plottype_cb, 9, 0, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.pointsperamu_label = QLabel(self.tab)
        self.pointsperamu_label.setObjectName(u"pointsperamu_label")

        self.gridLayout_2.addWidget(self.pointsperamu_label, 5, 1, 1, 2)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 3, 2, 1, 1)

        self.skiprows_qms_sb = QSpinBox(self.tab)
        self.skiprows_qms_sb.setObjectName(u"skiprows_qms_sb")

        self.gridLayout_2.addWidget(self.skiprows_qms_sb, 3, 3, 1, 1)

        self.qmsy_tw = QTreeWidget(self.tab)
        self.qmsy_tw.setObjectName(u"qmsy_tw")

        self.gridLayout_2.addWidget(self.qmsy_tw, 1, 2, 1, 2)

        self.treeView_qms = QTreeView(self.tab)
        self.treeView_qms.setObjectName(u"treeView_qms")

        self.gridLayout_2.addWidget(self.treeView_qms, 0, 0, 1, 4)

        self.qmsx_tw = QTreeWidget(self.tab)
        self.qmsx_tw.setObjectName(u"qmsx_tw")

        self.gridLayout_2.addWidget(self.qmsx_tw, 1, 0, 1, 2)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)

        self.fill_cols_qms_pb = QPushButton(self.tab)
        self.fill_cols_qms_pb.setObjectName(u"fill_cols_qms_pb")

        self.gridLayout_2.addWidget(self.fill_cols_qms_pb, 9, 2, 1, 1)

        self.plot_qms_pb = QPushButton(self.tab)
        self.plot_qms_pb.setObjectName(u"plot_qms_pb")

        self.gridLayout_2.addWidget(self.plot_qms_pb, 9, 3, 1, 1)

        self.abundance_pb = QPushButton(self.tab)
        self.abundance_pb.setObjectName(u"abundance_pb")

        self.gridLayout_2.addWidget(self.abundance_pb, 5, 3, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.tab_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 3, 0, 1, 1)

        self.plottable_pb = QPushButton(self.tab_4)
        self.plottable_pb.setObjectName(u"plottable_pb")

        self.gridLayout_4.addWidget(self.plottable_pb, 4, 1, 1, 1)

        self.xaxislabel_le = QLineEdit(self.tab_4)
        self.xaxislabel_le.setObjectName(u"xaxislabel_le")

        self.gridLayout_4.addWidget(self.xaxislabel_le, 2, 1, 1, 1)

        self.yaxislabel_le = QLineEdit(self.tab_4)
        self.yaxislabel_le.setObjectName(u"yaxislabel_le")

        self.gridLayout_4.addWidget(self.yaxislabel_le, 3, 1, 1, 1)

        self.label = QLabel(self.tab_4)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)

        self.xaxis_cb = QComboBox(self.tab_4)
        self.xaxis_cb.addItem("")
        self.xaxis_cb.addItem("")
        self.xaxis_cb.addItem("")
        self.xaxis_cb.addItem("")
        self.xaxis_cb.addItem("")
        self.xaxis_cb.addItem("")
        self.xaxis_cb.setObjectName(u"xaxis_cb")

        self.gridLayout_4.addWidget(self.xaxis_cb, 2, 2, 1, 1)

        self.yaxis_cb = QComboBox(self.tab_4)
        self.yaxis_cb.addItem("")
        self.yaxis_cb.addItem("")
        self.yaxis_cb.addItem("")
        self.yaxis_cb.addItem("")
        self.yaxis_cb.addItem("")
        self.yaxis_cb.addItem("")
        self.yaxis_cb.setObjectName(u"yaxis_cb")

        self.gridLayout_4.addWidget(self.yaxis_cb, 3, 2, 1, 1)

        self.tableWidget = QTableWidget(self.tab_4)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 2, 1, 4)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"SE", None))
        self.plot_type_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Ext. Plot (half-ints)", None))
        self.plot_type_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Ext. Plot (ints)", None))
        self.plot_type_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"X vs Y", None))
        self.plot_type_cb.setItemText(3, QCoreApplication.translate("DockWidget", u"Ext. Plot (third-ints)", None))

        self.xlabel_le.setText(QCoreApplication.translate("DockWidget", u"Cycles", None))
        self.ylabel_le.setText(QCoreApplication.translate("DockWidget", u"$\\Delta$ Thickness ($\\AA$)", None))
        self.fill_cols_pb.setText(QCoreApplication.translate("DockWidget", u"Fill Columns", None))
        self.label_9.setText(QCoreApplication.translate("DockWidget", u"Y Label", None))
        self.zero_correct_checkb.setText(QCoreApplication.translate("DockWidget", u"Zero Correct", None))
        ___qtreewidgetitem = self.tw_x.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("DockWidget", u"SE-X", None));
        ___qtreewidgetitem1 = self.tw_y.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("DockWidget", u"SE-Y", None));
        self.plot_pb.setText(QCoreApplication.translate("DockWidget", u"Plot", None))
        self.label_8.setText(QCoreApplication.translate("DockWidget", u"X Label", None))
        self.ax_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Left Ax", None))
        self.ax_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Right Ax", None))

        self.label_7.setText(QCoreApplication.translate("DockWidget", u"Skip Rows: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("DockWidget", u"Axis Properties", None))
        self.textBrowser.setHtml(QCoreApplication.translate("DockWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont'; font-size:13pt;\">There are a few parameter for plotting if you may need it,  including what the line should look like, the color (UNDER WORK) and if the data may require you to skip inital metadata at the beginning.  Lin. Fit function makes a popup dialog where you can pick a single line on the graph to linearly fit where the fit stats will show up below. The Lin. Fit. All will fit all the data on the graph and print in the line command the slopes of the data</span></p></body></html>", None))
        self.selectrange_box.setText(QCoreApplication.translate("DockWidget", u"Select Fitting Range", None))
        self.axischoise_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"axis1", None))
        self.axischoise_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"axis2", None))
        self.axischoise_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"axis3", None))
        self.axischoise_cb.setItemText(3, QCoreApplication.translate("DockWidget", u"axis4", None))

        self.lin_fit_pb.setText(QCoreApplication.translate("DockWidget", u"Lin. Fit", None))
        self.linfitall_pb.setText(QCoreApplication.translate("DockWidget", u"Lin. Fit. All", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("DockWidget", u"Fit Results", None))
        self.plot_side_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Left", None))
        self.plot_side_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Right", None))

        self.label_3.setText(QCoreApplication.translate("DockWidget", u"Starting Mass", None))
        self.plottype_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Mass Spectrum", None))
        self.plottype_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Mass Trace", None))

        self.label_4.setText(QCoreApplication.translate("DockWidget", u"Ending Mass", None))
        self.pointsperamu_label.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label_6.setText(QCoreApplication.translate("DockWidget", u"Skip Rows", None))
        ___qtreewidgetitem2 = self.qmsy_tw.headerItem()
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("DockWidget", u"QMS Y", None));
        ___qtreewidgetitem3 = self.qmsx_tw.headerItem()
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("DockWidget", u"QMS_X", None));
        self.label_5.setText(QCoreApplication.translate("DockWidget", u"Points per amu", None))
        self.fill_cols_qms_pb.setText(QCoreApplication.translate("DockWidget", u"Fill Columns", None))
        self.plot_qms_pb.setText(QCoreApplication.translate("DockWidget", u"Plot", None))
        self.abundance_pb.setText(QCoreApplication.translate("DockWidget", u"Abundance Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("DockWidget", u"QMS", None))
        self.label_2.setText(QCoreApplication.translate("DockWidget", u"Y Axis", None))
        self.plottable_pb.setText(QCoreApplication.translate("DockWidget", u"Plot Table", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"X Axis", None))
        self.xaxis_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"0", None))
        self.xaxis_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"1", None))
        self.xaxis_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"2", None))
        self.xaxis_cb.setItemText(3, QCoreApplication.translate("DockWidget", u"3", None))
        self.xaxis_cb.setItemText(4, QCoreApplication.translate("DockWidget", u"4", None))
        self.xaxis_cb.setItemText(5, QCoreApplication.translate("DockWidget", u"5", None))

        self.yaxis_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"0", None))
        self.yaxis_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"1", None))
        self.yaxis_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"2", None))
        self.yaxis_cb.setItemText(3, QCoreApplication.translate("DockWidget", u"3", None))
        self.yaxis_cb.setItemText(4, QCoreApplication.translate("DockWidget", u"4", None))
        self.yaxis_cb.setItemText(5, QCoreApplication.translate("DockWidget", u"5", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DockWidget", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DockWidget", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DockWidget", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DockWidget", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DockWidget", u"4", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DockWidget", u"5", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("DockWidget", u"Table", None))
    # retranslateUi

