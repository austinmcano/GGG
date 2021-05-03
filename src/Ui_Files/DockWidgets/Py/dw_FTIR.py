# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_FTIR.ui'
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
        DockWidget.resize(560, 536)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 12, 1, 1, 1)

        self.sub_dir_pb = QPushButton(self.tab)
        self.sub_dir_pb.setObjectName(u"sub_dir_pb")

        self.gridLayout_2.addWidget(self.sub_dir_pb, 1, 1, 1, 1)

        self.smooth_pb = QPushButton(self.tab)
        self.smooth_pb.setObjectName(u"smooth_pb")

        self.gridLayout_2.addWidget(self.smooth_pb, 15, 3, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 15, 1, 1, 1)

        self.FTIR_treeView = QTreeView(self.tab)
        self.FTIR_treeView.setObjectName(u"FTIR_treeView")

        self.gridLayout_2.addWidget(self.FTIR_treeView, 0, 1, 1, 3)

        self.lambda_sb = QSpinBox(self.tab)
        self.lambda_sb.setObjectName(u"lambda_sb")
        self.lambda_sb.setMaximum(9999999)
        self.lambda_sb.setSingleStep(1000)
        self.lambda_sb.setValue(1000)

        self.gridLayout_2.addWidget(self.lambda_sb, 10, 2, 1, 1)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 9, 1, 1, 3)

        self.abs_dir_pb = QPushButton(self.tab)
        self.abs_dir_pb.setObjectName(u"abs_dir_pb")

        self.gridLayout_2.addWidget(self.abs_dir_pb, 1, 3, 1, 1)

        self.baseline_pb = QPushButton(self.tab)
        self.baseline_pb.setObjectName(u"baseline_pb")

        self.gridLayout_2.addWidget(self.baseline_pb, 10, 3, 1, 1)

        self.spectra_pb = QPushButton(self.tab)
        self.spectra_pb.setObjectName(u"spectra_pb")

        self.gridLayout_2.addWidget(self.spectra_pb, 4, 1, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 10, 1, 1, 1)

        self.skip_sb = QSpinBox(self.tab)
        self.skip_sb.setObjectName(u"skip_sb")
        self.skip_sb.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.skip_sb.setKeyboardTracking(False)
        self.skip_sb.setValue(0)

        self.gridLayout_2.addWidget(self.skip_sb, 6, 2, 1, 1)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 6, 1, 1, 1)

        self.diff_2_pb = QPushButton(self.tab)
        self.diff_2_pb.setObjectName(u"diff_2_pb")

        self.gridLayout_2.addWidget(self.diff_2_pb, 4, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.tab)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 4, 3, 1, 1)

        self.diff_dir_pb = QPushButton(self.tab)
        self.diff_dir_pb.setObjectName(u"diff_dir_pb")

        self.gridLayout_2.addWidget(self.diff_dir_pb, 1, 2, 1, 1)

        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 13, 1, 1, 3)

        self.smooth_sb = QSpinBox(self.tab)
        self.smooth_sb.setObjectName(u"smooth_sb")
        self.smooth_sb.setValue(11)

        self.gridLayout_2.addWidget(self.smooth_sb, 15, 2, 1, 1)

        self.p_sb = QDoubleSpinBox(self.tab)
        self.p_sb.setObjectName(u"p_sb")
        self.p_sb.setDecimals(6)
        self.p_sb.setMaximum(1000.000000000000000)
        self.p_sb.setSingleStep(0.010000000000000)
        self.p_sb.setValue(0.010000000000000)

        self.gridLayout_2.addWidget(self.p_sb, 12, 2, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 12, 3, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.textBrowser = QTextBrowser(self.tab_3)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_4.addWidget(self.textBrowser, 0, 3, 1, 3)

        self.tableWidget = QTableWidget(self.tab_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(320, 0))
        self.tableWidget.setMaximumSize(QSize(1000, 1000))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)

        self.gridLayout_4.addWidget(self.tableWidget, 7, 3, 4, 3)

        self.max_sb = QDoubleSpinBox(self.tab_3)
        self.max_sb.setObjectName(u"max_sb")
        self.max_sb.setMaximum(4000.000000000000000)
        self.max_sb.setValue(4000.000000000000000)

        self.gridLayout_4.addWidget(self.max_sb, 2, 5, 1, 1)

        self.min_sb = QDoubleSpinBox(self.tab_3)
        self.min_sb.setObjectName(u"min_sb")
        self.min_sb.setMaximum(4000.000000000000000)
        self.min_sb.setValue(400.000000000000000)

        self.gridLayout_4.addWidget(self.min_sb, 2, 4, 1, 1)

        self.integrate_pb = QPushButton(self.tab_3)
        self.integrate_pb.setObjectName(u"integrate_pb")
        self.integrate_pb.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.integrate_pb, 4, 5, 1, 1)

        self.int_type_cb = QComboBox(self.tab_3)
        self.int_type_cb.addItem("")
        self.int_type_cb.addItem("")
        self.int_type_cb.addItem("")
        self.int_type_cb.addItem("")
        self.int_type_cb.setObjectName(u"int_type_cb")

        self.gridLayout_4.addWidget(self.int_type_cb, 4, 4, 1, 1)

        self.line_3 = QFrame(self.tab_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 5, 3, 1, 3)

        self.xaxis_cb = QComboBox(self.tab_3)
        self.xaxis_cb.addItem("")
        self.xaxis_cb.addItem("")
        self.xaxis_cb.setObjectName(u"xaxis_cb")

        self.gridLayout_4.addWidget(self.xaxis_cb, 4, 3, 1, 1)

        self.leftrightaxis_cb = QComboBox(self.tab_3)
        self.leftrightaxis_cb.addItem("")
        self.leftrightaxis_cb.addItem("")
        self.leftrightaxis_cb.setObjectName(u"leftrightaxis_cb")
        self.leftrightaxis_cb.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.leftrightaxis_cb, 2, 3, 1, 1)

        self.integratemode_rb = QRadioButton(self.tab_3)
        self.integratemode_rb.setObjectName(u"integratemode_rb")

        self.gridLayout_4.addWidget(self.integratemode_rb, 1, 3, 1, 3)

        self.plottable_pb = QPushButton(self.tab_3)
        self.plottable_pb.setObjectName(u"plottable_pb")

        self.gridLayout_4.addWidget(self.plottable_pb, 11, 5, 1, 1)

        self.tabley_cb = QComboBox(self.tab_3)
        self.tabley_cb.setObjectName(u"tabley_cb")

        self.gridLayout_4.addWidget(self.tabley_cb, 11, 4, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.plot_current_pb = QPushButton(self.tab_2)
        self.plot_current_pb.setObjectName(u"plot_current_pb")

        self.gridLayout_3.addWidget(self.plot_current_pb, 2, 1, 1, 1)

        self.fit_report_TE = QTextEdit(self.tab_2)
        self.fit_report_TE.setObjectName(u"fit_report_TE")

        self.gridLayout_3.addWidget(self.fit_report_TE, 3, 0, 1, 4)

        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget_2.rowCount() < 9):
            self.tableWidget_2.setRowCount(9)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem13)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_3.addWidget(self.tableWidget_2, 1, 0, 1, 4)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.selectdata_pb = QPushButton(self.tab_2)
        self.selectdata_pb.setObjectName(u"selectdata_pb")

        self.gridLayout_3.addWidget(self.selectdata_pb, 2, 0, 1, 1)

        self.num_peaks_sb = QSpinBox(self.tab_2)
        self.num_peaks_sb.setObjectName(u"num_peaks_sb")
        self.num_peaks_sb.setMinimum(1)
        self.num_peaks_sb.setMaximum(5)

        self.gridLayout_3.addWidget(self.num_peaks_sb, 0, 1, 1, 1)

        self.fit_pb = QPushButton(self.tab_2)
        self.fit_pb.setObjectName(u"fit_pb")

        self.gridLayout_3.addWidget(self.fit_pb, 2, 3, 1, 1)

        self.import_to_constraints_pb = QPushButton(self.tab_2)
        self.import_to_constraints_pb.setObjectName(u"import_to_constraints_pb")

        self.gridLayout_3.addWidget(self.import_to_constraints_pb, 2, 2, 1, 1)

        self.fit_shape_cb = QComboBox(self.tab_2)
        self.fit_shape_cb.addItem("")
        self.fit_shape_cb.addItem("")
        self.fit_shape_cb.addItem("")
        self.fit_shape_cb.setObjectName(u"fit_shape_cb")

        self.gridLayout_3.addWidget(self.fit_shape_cb, 0, 2, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.line_5 = QFrame(self.tab_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_5, 11, 1, 1, 6)

        self.p1_sigh_sb = QDoubleSpinBox(self.tab_4)
        self.p1_sigh_sb.setObjectName(u"p1_sigh_sb")
        self.p1_sigh_sb.setMaximum(500.000000000000000)
        self.p1_sigh_sb.setValue(300.000000000000000)

        self.gridLayout_5.addWidget(self.p1_sigh_sb, 14, 2, 1, 1)

        self.p4_cenl_sb = QDoubleSpinBox(self.tab_4)
        self.p4_cenl_sb.setObjectName(u"p4_cenl_sb")
        self.p4_cenl_sb.setMaximum(4000.000000000000000)
        self.p4_cenl_sb.setValue(400.000000000000000)

        self.gridLayout_5.addWidget(self.p4_cenl_sb, 9, 5, 1, 1)

        self.p4_cenh_sb = QDoubleSpinBox(self.tab_4)
        self.p4_cenh_sb.setObjectName(u"p4_cenh_sb")
        self.p4_cenh_sb.setMaximum(4000.000000000000000)
        self.p4_cenh_sb.setValue(4000.000000000000000)

        self.gridLayout_5.addWidget(self.p4_cenh_sb, 10, 5, 1, 1)

        self.p1_cenl_sb = QDoubleSpinBox(self.tab_4)
        self.p1_cenl_sb.setObjectName(u"p1_cenl_sb")
        self.p1_cenl_sb.setMaximum(4000.000000000000000)
        self.p1_cenl_sb.setValue(400.000000000000000)

        self.gridLayout_5.addWidget(self.p1_cenl_sb, 9, 2, 1, 1)

        self.label_13 = QLabel(self.tab_4)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 10, 1, 1, 1)

        self.p4_amph_sb = QDoubleSpinBox(self.tab_4)
        self.p4_amph_sb.setObjectName(u"p4_amph_sb")
        self.p4_amph_sb.setMaximum(9999.000000000000000)
        self.p4_amph_sb.setValue(9999.000000000000000)

        self.gridLayout_5.addWidget(self.p4_amph_sb, 5, 5, 1, 1)

        self.p3_cenh_sb = QDoubleSpinBox(self.tab_4)
        self.p3_cenh_sb.setObjectName(u"p3_cenh_sb")
        self.p3_cenh_sb.setMaximum(4000.000000000000000)
        self.p3_cenh_sb.setValue(4000.000000000000000)

        self.gridLayout_5.addWidget(self.p3_cenh_sb, 10, 4, 1, 1)

        self.p2_cenl_sb = QDoubleSpinBox(self.tab_4)
        self.p2_cenl_sb.setObjectName(u"p2_cenl_sb")
        self.p2_cenl_sb.setMaximum(4000.000000000000000)
        self.p2_cenl_sb.setValue(400.000000000000000)

        self.gridLayout_5.addWidget(self.p2_cenl_sb, 9, 3, 1, 1)

        self.label_8 = QLabel(self.tab_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 3, 1, 1, 1)

        self.p3_sigl_sb = QDoubleSpinBox(self.tab_4)
        self.p3_sigl_sb.setObjectName(u"p3_sigl_sb")
        self.p3_sigl_sb.setMaximum(500.000000000000000)
        self.p3_sigl_sb.setValue(0.100000000000000)

        self.gridLayout_5.addWidget(self.p3_sigl_sb, 13, 4, 1, 1)

        self.p5_cb = QCheckBox(self.tab_4)
        self.p5_cb.setObjectName(u"p5_cb")

        self.gridLayout_5.addWidget(self.p5_cb, 1, 6, 1, 1)

        self.p2_sig_sb = QDoubleSpinBox(self.tab_4)
        self.p2_sig_sb.setObjectName(u"p2_sig_sb")
        self.p2_sig_sb.setMaximum(500.000000000000000)
        self.p2_sig_sb.setValue(50.000000000000000)

        self.gridLayout_5.addWidget(self.p2_sig_sb, 12, 3, 1, 1)

        self.p3_cenl_sb = QDoubleSpinBox(self.tab_4)
        self.p3_cenl_sb.setObjectName(u"p3_cenl_sb")
        self.p3_cenl_sb.setMaximum(4000.000000000000000)
        self.p3_cenl_sb.setValue(400.000000000000000)

        self.gridLayout_5.addWidget(self.p3_cenl_sb, 9, 4, 1, 1)

        self.p5_sig_sb = QDoubleSpinBox(self.tab_4)
        self.p5_sig_sb.setObjectName(u"p5_sig_sb")
        self.p5_sig_sb.setMaximum(500.000000000000000)
        self.p5_sig_sb.setValue(50.000000000000000)

        self.gridLayout_5.addWidget(self.p5_sig_sb, 12, 6, 1, 1)

        self.label_17 = QLabel(self.tab_4)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 1, 1, 1, 1)

        self.p2_cen_sb = QDoubleSpinBox(self.tab_4)
        self.p2_cen_sb.setObjectName(u"p2_cen_sb")
        self.p2_cen_sb.setMaximum(4000.000000000000000)
        self.p2_cen_sb.setValue(1500.000000000000000)

        self.gridLayout_5.addWidget(self.p2_cen_sb, 8, 3, 1, 1)

        self.p5_cenh_sb = QDoubleSpinBox(self.tab_4)
        self.p5_cenh_sb.setObjectName(u"p5_cenh_sb")
        self.p5_cenh_sb.setMaximum(4000.000000000000000)
        self.p5_cenh_sb.setValue(4000.000000000000000)

        self.gridLayout_5.addWidget(self.p5_cenh_sb, 10, 6, 1, 1)

        self.line_4 = QFrame(self.tab_4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_4, 7, 1, 1, 6)

        self.textEdit = QTextEdit(self.tab_4)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_5.addWidget(self.textEdit, 15, 1, 1, 6)

        self.p4_cb = QCheckBox(self.tab_4)
        self.p4_cb.setObjectName(u"p4_cb")

        self.gridLayout_5.addWidget(self.p4_cb, 1, 5, 1, 1)

        self.p2_ampl_sb = QDoubleSpinBox(self.tab_4)
        self.p2_ampl_sb.setObjectName(u"p2_ampl_sb")
        self.p2_ampl_sb.setMaximum(9999.000000000000000)

        self.gridLayout_5.addWidget(self.p2_ampl_sb, 4, 3, 1, 1)

        self.p1_cb = QCheckBox(self.tab_4)
        self.p1_cb.setObjectName(u"p1_cb")
        self.p1_cb.setChecked(True)

        self.gridLayout_5.addWidget(self.p1_cb, 1, 2, 1, 1)

        self.p5_sigh_sb = QDoubleSpinBox(self.tab_4)
        self.p5_sigh_sb.setObjectName(u"p5_sigh_sb")
        self.p5_sigh_sb.setMaximum(500.000000000000000)
        self.p5_sigh_sb.setValue(300.000000000000000)

        self.gridLayout_5.addWidget(self.p5_sigh_sb, 14, 6, 1, 1)

        self.p4_ampl_sb = QDoubleSpinBox(self.tab_4)
        self.p4_ampl_sb.setObjectName(u"p4_ampl_sb")
        self.p4_ampl_sb.setMaximum(9999.000000000000000)

        self.gridLayout_5.addWidget(self.p4_ampl_sb, 4, 5, 1, 1)

        self.p1_cen_sb = QDoubleSpinBox(self.tab_4)
        self.p1_cen_sb.setObjectName(u"p1_cen_sb")
        self.p1_cen_sb.setMaximum(4000.000000000000000)
        self.p1_cen_sb.setValue(1000.000000000000000)

        self.gridLayout_5.addWidget(self.p1_cen_sb, 8, 2, 1, 1)

        self.p5_sigl_sb = QDoubleSpinBox(self.tab_4)
        self.p5_sigl_sb.setObjectName(u"p5_sigl_sb")
        self.p5_sigl_sb.setMaximum(500.000000000000000)
        self.p5_sigl_sb.setValue(0.100000000000000)

        self.gridLayout_5.addWidget(self.p5_sigl_sb, 13, 6, 1, 1)

        self.p1_amph_sb = QDoubleSpinBox(self.tab_4)
        self.p1_amph_sb.setObjectName(u"p1_amph_sb")
        self.p1_amph_sb.setMaximum(9999.000000000000000)
        self.p1_amph_sb.setValue(9999.000000000000000)

        self.gridLayout_5.addWidget(self.p1_amph_sb, 5, 2, 1, 1)

        self.p5_cenl_sb = QDoubleSpinBox(self.tab_4)
        self.p5_cenl_sb.setObjectName(u"p5_cenl_sb")
        self.p5_cenl_sb.setMaximum(4000.000000000000000)
        self.p5_cenl_sb.setValue(400.000000000000000)

        self.gridLayout_5.addWidget(self.p5_cenl_sb, 9, 6, 1, 1)

        self.fit2_pb = QPushButton(self.tab_4)
        self.fit2_pb.setObjectName(u"fit2_pb")

        self.gridLayout_5.addWidget(self.fit2_pb, 16, 5, 1, 2)

        self.p4_sig_sb = QDoubleSpinBox(self.tab_4)
        self.p4_sig_sb.setObjectName(u"p4_sig_sb")
        self.p4_sig_sb.setMaximum(500.000000000000000)
        self.p4_sig_sb.setValue(50.000000000000000)

        self.gridLayout_5.addWidget(self.p4_sig_sb, 12, 5, 1, 1)

        self.p5_cen_sb = QDoubleSpinBox(self.tab_4)
        self.p5_cen_sb.setObjectName(u"p5_cen_sb")
        self.p5_cen_sb.setMaximum(4000.000000000000000)
        self.p5_cen_sb.setValue(3000.000000000000000)

        self.gridLayout_5.addWidget(self.p5_cen_sb, 8, 6, 1, 1)

        self.label_14 = QLabel(self.tab_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 12, 1, 1, 1)

        self.p3_sig_sb = QDoubleSpinBox(self.tab_4)
        self.p3_sig_sb.setObjectName(u"p3_sig_sb")
        self.p3_sig_sb.setMaximum(500.000000000000000)
        self.p3_sig_sb.setValue(50.000000000000000)

        self.gridLayout_5.addWidget(self.p3_sig_sb, 12, 4, 1, 1)

        self.p2_cb = QCheckBox(self.tab_4)
        self.p2_cb.setObjectName(u"p2_cb")

        self.gridLayout_5.addWidget(self.p2_cb, 1, 3, 1, 1)

        self.p5_amp_sb = QDoubleSpinBox(self.tab_4)
        self.p5_amp_sb.setObjectName(u"p5_amp_sb")
        self.p5_amp_sb.setMaximum(9999.000000000000000)
        self.p5_amp_sb.setValue(10.000000000000000)

        self.gridLayout_5.addWidget(self.p5_amp_sb, 3, 6, 1, 1)

        self.p1_sig_sb = QDoubleSpinBox(self.tab_4)
        self.p1_sig_sb.setObjectName(u"p1_sig_sb")
        self.p1_sig_sb.setMaximum(500.000000000000000)
        self.p1_sig_sb.setValue(50.000000000000000)

        self.gridLayout_5.addWidget(self.p1_sig_sb, 12, 2, 1, 1)

        self.label_9 = QLabel(self.tab_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 4, 1, 1, 1)

        self.p2_sigh_sb = QDoubleSpinBox(self.tab_4)
        self.p2_sigh_sb.setObjectName(u"p2_sigh_sb")
        self.p2_sigh_sb.setMaximum(500.000000000000000)
        self.p2_sigh_sb.setValue(300.000000000000000)

        self.gridLayout_5.addWidget(self.p2_sigh_sb, 14, 3, 1, 1)

        self.p3_cen_sb = QDoubleSpinBox(self.tab_4)
        self.p3_cen_sb.setObjectName(u"p3_cen_sb")
        self.p3_cen_sb.setMaximum(4000.000000000000000)
        self.p3_cen_sb.setValue(2000.000000000000000)

        self.gridLayout_5.addWidget(self.p3_cen_sb, 8, 4, 1, 1)

        self.p5_amph_sb = QDoubleSpinBox(self.tab_4)
        self.p5_amph_sb.setObjectName(u"p5_amph_sb")
        self.p5_amph_sb.setMaximum(9999.000000000000000)
        self.p5_amph_sb.setValue(9999.000000000000000)

        self.gridLayout_5.addWidget(self.p5_amph_sb, 5, 6, 1, 1)

        self.p4_amp_sb = QDoubleSpinBox(self.tab_4)
        self.p4_amp_sb.setObjectName(u"p4_amp_sb")
        self.p4_amp_sb.setMaximum(9999.000000000000000)
        self.p4_amp_sb.setValue(10.000000000000000)

        self.gridLayout_5.addWidget(self.p4_amp_sb, 3, 5, 1, 1)

        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 5, 1, 1, 1)

        self.label_12 = QLabel(self.tab_4)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 9, 1, 1, 1)

        self.lineshape_5 = QComboBox(self.tab_4)
        self.lineshape_5.addItem("")
        self.lineshape_5.addItem("")
        self.lineshape_5.addItem("")
        self.lineshape_5.setObjectName(u"lineshape_5")

        self.gridLayout_5.addWidget(self.lineshape_5, 2, 6, 1, 1)

        self.label_16 = QLabel(self.tab_4)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 14, 1, 1, 1)

        self.p2_amp_sb = QDoubleSpinBox(self.tab_4)
        self.p2_amp_sb.setObjectName(u"p2_amp_sb")
        self.p2_amp_sb.setMaximum(9999.000000000000000)
        self.p2_amp_sb.setValue(10.000000000000000)

        self.gridLayout_5.addWidget(self.p2_amp_sb, 3, 3, 1, 1)

        self.select_data_pb = QPushButton(self.tab_4)
        self.select_data_pb.setObjectName(u"select_data_pb")

        self.gridLayout_5.addWidget(self.select_data_pb, 16, 1, 1, 2)

        self.lineshape_2 = QComboBox(self.tab_4)
        self.lineshape_2.addItem("")
        self.lineshape_2.addItem("")
        self.lineshape_2.addItem("")
        self.lineshape_2.setObjectName(u"lineshape_2")

        self.gridLayout_5.addWidget(self.lineshape_2, 2, 3, 1, 1)

        self.p2_sigl_sb = QDoubleSpinBox(self.tab_4)
        self.p2_sigl_sb.setObjectName(u"p2_sigl_sb")
        self.p2_sigl_sb.setMaximum(500.000000000000000)
        self.p2_sigl_sb.setValue(0.100000000000000)

        self.gridLayout_5.addWidget(self.p2_sigl_sb, 13, 3, 1, 1)

        self.label_15 = QLabel(self.tab_4)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 13, 1, 1, 1)

        self.p3_amp_sb = QDoubleSpinBox(self.tab_4)
        self.p3_amp_sb.setObjectName(u"p3_amp_sb")
        self.p3_amp_sb.setMaximum(9999.000000000000000)
        self.p3_amp_sb.setValue(10.000000000000000)

        self.gridLayout_5.addWidget(self.p3_amp_sb, 3, 4, 1, 1)

        self.p1_amp_sb = QDoubleSpinBox(self.tab_4)
        self.p1_amp_sb.setObjectName(u"p1_amp_sb")
        self.p1_amp_sb.setMaximum(9999.000000000000000)
        self.p1_amp_sb.setValue(10.000000000000000)

        self.gridLayout_5.addWidget(self.p1_amp_sb, 3, 2, 1, 1)

        self.label_11 = QLabel(self.tab_4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 8, 1, 1, 1)

        self.p3_amph_sb = QDoubleSpinBox(self.tab_4)
        self.p3_amph_sb.setObjectName(u"p3_amph_sb")
        self.p3_amph_sb.setMaximum(9999.000000000000000)
        self.p3_amph_sb.setValue(9999.000000000000000)

        self.gridLayout_5.addWidget(self.p3_amph_sb, 5, 4, 1, 1)

        self.p5_ampl_sb = QDoubleSpinBox(self.tab_4)
        self.p5_ampl_sb.setObjectName(u"p5_ampl_sb")
        self.p5_ampl_sb.setMaximum(9999.000000000000000)

        self.gridLayout_5.addWidget(self.p5_ampl_sb, 4, 6, 1, 1)

        self.p4_cen_sb = QDoubleSpinBox(self.tab_4)
        self.p4_cen_sb.setObjectName(u"p4_cen_sb")
        self.p4_cen_sb.setMaximum(4000.000000000000000)
        self.p4_cen_sb.setValue(2500.000000000000000)

        self.gridLayout_5.addWidget(self.p4_cen_sb, 8, 5, 1, 1)

        self.fit_init_pb = QPushButton(self.tab_4)
        self.fit_init_pb.setObjectName(u"fit_init_pb")

        self.gridLayout_5.addWidget(self.fit_init_pb, 16, 3, 1, 2)

        self.p2_cenh_sb = QDoubleSpinBox(self.tab_4)
        self.p2_cenh_sb.setObjectName(u"p2_cenh_sb")
        self.p2_cenh_sb.setMaximum(4000.000000000000000)
        self.p2_cenh_sb.setValue(4000.000000000000000)

        self.gridLayout_5.addWidget(self.p2_cenh_sb, 10, 3, 1, 1)

        self.lineshape_1 = QComboBox(self.tab_4)
        self.lineshape_1.addItem("")
        self.lineshape_1.addItem("")
        self.lineshape_1.addItem("")
        self.lineshape_1.setObjectName(u"lineshape_1")

        self.gridLayout_5.addWidget(self.lineshape_1, 2, 2, 1, 1)

        self.p4_sigh_sb = QDoubleSpinBox(self.tab_4)
        self.p4_sigh_sb.setObjectName(u"p4_sigh_sb")
        self.p4_sigh_sb.setMaximum(500.000000000000000)
        self.p4_sigh_sb.setValue(300.000000000000000)

        self.gridLayout_5.addWidget(self.p4_sigh_sb, 14, 5, 1, 1)

        self.p4_sigl_sb = QDoubleSpinBox(self.tab_4)
        self.p4_sigl_sb.setObjectName(u"p4_sigl_sb")
        self.p4_sigl_sb.setMaximum(500.000000000000000)
        self.p4_sigl_sb.setValue(0.100000000000000)

        self.gridLayout_5.addWidget(self.p4_sigl_sb, 13, 5, 1, 1)

        self.p1_sigl_sb = QDoubleSpinBox(self.tab_4)
        self.p1_sigl_sb.setObjectName(u"p1_sigl_sb")
        self.p1_sigl_sb.setMaximum(500.000000000000000)
        self.p1_sigl_sb.setValue(0.100000000000000)

        self.gridLayout_5.addWidget(self.p1_sigl_sb, 13, 2, 1, 1)

        self.lineshape_3 = QComboBox(self.tab_4)
        self.lineshape_3.addItem("")
        self.lineshape_3.addItem("")
        self.lineshape_3.addItem("")
        self.lineshape_3.setObjectName(u"lineshape_3")

        self.gridLayout_5.addWidget(self.lineshape_3, 2, 4, 1, 1)

        self.p3_cb = QCheckBox(self.tab_4)
        self.p3_cb.setObjectName(u"p3_cb")

        self.gridLayout_5.addWidget(self.p3_cb, 1, 4, 1, 1)

        self.p1_cenh_sb = QDoubleSpinBox(self.tab_4)
        self.p1_cenh_sb.setObjectName(u"p1_cenh_sb")
        self.p1_cenh_sb.setMaximum(4000.000000000000000)
        self.p1_cenh_sb.setValue(4000.000000000000000)

        self.gridLayout_5.addWidget(self.p1_cenh_sb, 10, 2, 1, 1)

        self.lineshape_4 = QComboBox(self.tab_4)
        self.lineshape_4.addItem("")
        self.lineshape_4.addItem("")
        self.lineshape_4.addItem("")
        self.lineshape_4.setObjectName(u"lineshape_4")

        self.gridLayout_5.addWidget(self.lineshape_4, 2, 5, 1, 1)

        self.p3_ampl_sb = QDoubleSpinBox(self.tab_4)
        self.p3_ampl_sb.setObjectName(u"p3_ampl_sb")
        self.p3_ampl_sb.setMaximum(9999.000000000000000)

        self.gridLayout_5.addWidget(self.p3_ampl_sb, 4, 4, 1, 1)

        self.p2_amph_sb = QDoubleSpinBox(self.tab_4)
        self.p2_amph_sb.setObjectName(u"p2_amph_sb")
        self.p2_amph_sb.setMaximum(9999.000000000000000)
        self.p2_amph_sb.setValue(9999.000000000000000)

        self.gridLayout_5.addWidget(self.p2_amph_sb, 5, 3, 1, 1)

        self.p3_sigh_sb = QDoubleSpinBox(self.tab_4)
        self.p3_sigh_sb.setObjectName(u"p3_sigh_sb")
        self.p3_sigh_sb.setMaximum(500.000000000000000)
        self.p3_sigh_sb.setValue(300.000000000000000)

        self.gridLayout_5.addWidget(self.p3_sigh_sb, 14, 4, 1, 1)

        self.p1_ampl_sb = QDoubleSpinBox(self.tab_4)
        self.p1_ampl_sb.setObjectName(u"p1_ampl_sb")
        self.p1_ampl_sb.setMaximum(9999.000000000000000)

        self.gridLayout_5.addWidget(self.p1_ampl_sb, 4, 2, 1, 1)

        self.comboBox = QComboBox(self.tab_4)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_5.addWidget(self.comboBox, 0, 4, 1, 3)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"FTIR", None))
        self.label_6.setText(QCoreApplication.translate("DockWidget", u"P (asymetry) ", None))
        self.sub_dir_pb.setText(QCoreApplication.translate("DockWidget", u"Sub Plot (dir)", None))
        self.smooth_pb.setText(QCoreApplication.translate("DockWidget", u"Smooth", None))
        self.label_3.setText(QCoreApplication.translate("DockWidget", u"Savitzky\u2013Golay Filter", None))
        self.abs_dir_pb.setText(QCoreApplication.translate("DockWidget", u"Plot (dir)", None))
        self.baseline_pb.setText(QCoreApplication.translate("DockWidget", u"Baseline All", None))
        self.spectra_pb.setText(QCoreApplication.translate("DockWidget", u"Plot", None))
        self.label_4.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p>\u03bb  (smoothness)</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"Skip Every", None))
        self.diff_2_pb.setText(QCoreApplication.translate("DockWidget", u"Diff Plot (2)", None))
        self.pushButton_7.setText(QCoreApplication.translate("DockWidget", u"TBD", None))
        self.diff_dir_pb.setText(QCoreApplication.translate("DockWidget", u"Diff Plot (dir)", None))
        self.label_7.setText(QCoreApplication.translate("DockWidget", u"UNDER WORK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("DockWidget", u"IR Plot", None))
        self.textBrowser.setHtml(QCoreApplication.translate("DockWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont'; font-size:13pt;\">Press integrate mode.  Add the spectra to the top axis then click and hold on one limit and release on the other limit and the integral will show up on the axis below as well as in the table below here,  or manually type in the limits below and press &quot;Integrate&quot;</span></p></body></html>", None))
        self.integrate_pb.setText(QCoreApplication.translate("DockWidget", u"Integrate", None))
        self.int_type_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Subtraction", None))
        self.int_type_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Subtraction_C", None))
        self.int_type_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"Difference", None))
        self.int_type_cb.setItemText(3, QCoreApplication.translate("DockWidget", u"Absolute", None))

        self.xaxis_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Half-Ints", None))
        self.xaxis_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Ints", None))

        self.leftrightaxis_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Left Axis", None))
        self.leftrightaxis_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Right Axis", None))

        self.integratemode_rb.setText(QCoreApplication.translate("DockWidget", u"Integrate Mode", None))
        self.plottable_pb.setText(QCoreApplication.translate("DockWidget", u"Plot Table", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("DockWidget", u"Integrate", None))
        self.plot_current_pb.setText(QCoreApplication.translate("DockWidget", u"Plot Current", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DockWidget", u"Peak 1", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DockWidget", u"Peak 2", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DockWidget", u"Peak 3", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DockWidget", u"Peak 4", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DockWidget", u"Peak 5", None));
        ___qtablewidgetitem5 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DockWidget", u"Amp", None));
        ___qtablewidgetitem6 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DockWidget", u"Amp Low", None));
        ___qtablewidgetitem7 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DockWidget", u"Amp High", None));
        ___qtablewidgetitem8 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DockWidget", u"Cen", None));
        ___qtablewidgetitem9 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DockWidget", u"Cen Low", None));
        ___qtablewidgetitem10 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("DockWidget", u"Cen High", None));
        ___qtablewidgetitem11 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("DockWidget", u"Sigma", None));
        ___qtablewidgetitem12 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("DockWidget", u"Sigma Low", None));
        ___qtablewidgetitem13 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("DockWidget", u"Sigma High", None));
        self.label_5.setText(QCoreApplication.translate("DockWidget", u"Num of Peak", None))
        self.selectdata_pb.setText(QCoreApplication.translate("DockWidget", u"Select Data", None))
        self.fit_pb.setText(QCoreApplication.translate("DockWidget", u"Fit", None))
        self.import_to_constraints_pb.setText(QCoreApplication.translate("DockWidget", u"import fitted params", None))
        self.fit_shape_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Voigt", None))
        self.fit_shape_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Gaussian", None))
        self.fit_shape_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"Lorentz", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("DockWidget", u"Fitting", None))
        self.label_13.setText(QCoreApplication.translate("DockWidget", u"high", None))
        self.label_8.setText(QCoreApplication.translate("DockWidget", u"Amp", None))
        self.p5_cb.setText(QCoreApplication.translate("DockWidget", u"Peak 5", None))
        self.label_17.setText(QCoreApplication.translate("DockWidget", u"Peak #", None))
        self.p4_cb.setText(QCoreApplication.translate("DockWidget", u"Peak 4", None))
        self.p1_cb.setText(QCoreApplication.translate("DockWidget", u"Peak 1", None))
        self.fit2_pb.setText(QCoreApplication.translate("DockWidget", u"Fit", None))
        self.label_14.setText(QCoreApplication.translate("DockWidget", u"sigma", None))
        self.p2_cb.setText(QCoreApplication.translate("DockWidget", u"Peak 2", None))
        self.label_9.setText(QCoreApplication.translate("DockWidget", u"low", None))
        self.label_10.setText(QCoreApplication.translate("DockWidget", u"high", None))
        self.label_12.setText(QCoreApplication.translate("DockWidget", u"low", None))
        self.lineshape_5.setItemText(0, QCoreApplication.translate("DockWidget", u"Voigt", None))
        self.lineshape_5.setItemText(1, QCoreApplication.translate("DockWidget", u"Lorentz", None))
        self.lineshape_5.setItemText(2, QCoreApplication.translate("DockWidget", u"Gaussian", None))

        self.label_16.setText(QCoreApplication.translate("DockWidget", u"high", None))
        self.select_data_pb.setText(QCoreApplication.translate("DockWidget", u"Select Data", None))
        self.lineshape_2.setItemText(0, QCoreApplication.translate("DockWidget", u"Voigt", None))
        self.lineshape_2.setItemText(1, QCoreApplication.translate("DockWidget", u"Lorentz", None))
        self.lineshape_2.setItemText(2, QCoreApplication.translate("DockWidget", u"Gaussian", None))

        self.label_15.setText(QCoreApplication.translate("DockWidget", u"low", None))
        self.label_11.setText(QCoreApplication.translate("DockWidget", u"Cen", None))
        self.fit_init_pb.setText(QCoreApplication.translate("DockWidget", u"Fit Init", None))
        self.lineshape_1.setItemText(0, QCoreApplication.translate("DockWidget", u"Voigt", None))
        self.lineshape_1.setItemText(1, QCoreApplication.translate("DockWidget", u"Lorentz", None))
        self.lineshape_1.setItemText(2, QCoreApplication.translate("DockWidget", u"Gaussian", None))

        self.lineshape_3.setItemText(0, QCoreApplication.translate("DockWidget", u"Voigt", None))
        self.lineshape_3.setItemText(1, QCoreApplication.translate("DockWidget", u"Lorentz", None))
        self.lineshape_3.setItemText(2, QCoreApplication.translate("DockWidget", u"Gaussian ", None))

        self.p3_cb.setText(QCoreApplication.translate("DockWidget", u"Peak 3", None))
        self.lineshape_4.setItemText(0, QCoreApplication.translate("DockWidget", u"Voigt", None))
        self.lineshape_4.setItemText(1, QCoreApplication.translate("DockWidget", u"Lorentz", None))
        self.lineshape_4.setItemText(2, QCoreApplication.translate("DockWidget", u"Gaussian", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("DockWidget", u"Fitting_2", None))
    # retranslateUi

