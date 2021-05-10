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
        DockWidget.resize(555, 536)
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

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 7, 1, 1, 1)

        self.skiprows_sb = QSpinBox(self.tab)
        self.skiprows_sb.setObjectName(u"skiprows_sb")

        self.gridLayout_2.addWidget(self.skiprows_sb, 7, 2, 1, 1)

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
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.fit_init_pb = QPushButton(self.tab_4)
        self.fit_init_pb.setObjectName(u"fit_init_pb")

        self.gridLayout_5.addWidget(self.fit_init_pb, 15, 3, 1, 2)

        self.fit_pb = QPushButton(self.tab_4)
        self.fit_pb.setObjectName(u"fit_pb")

        self.gridLayout_5.addWidget(self.fit_pb, 15, 5, 1, 2)

        self.select_data_pb = QPushButton(self.tab_4)
        self.select_data_pb.setObjectName(u"select_data_pb")

        self.gridLayout_5.addWidget(self.select_data_pb, 15, 1, 1, 2)

        self.scrollArea = QScrollArea(self.tab_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 747, 887))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.plot_3sig_box = QCheckBox(self.scrollAreaWidgetContents)
        self.plot_3sig_box.setObjectName(u"plot_3sig_box")

        self.gridLayout_6.addWidget(self.plot_3sig_box, 20, 0, 1, 1)

        self.p5_fwhm = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p5_fwhm.setObjectName(u"p5_fwhm")
        self.p5_fwhm.setMaximum(9999.000000000000000)

        self.gridLayout_6.addWidget(self.p5_fwhm, 18, 5, 1, 1)

        self.p4_ampl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p4_ampl_sb.setObjectName(u"p4_ampl_sb")
        self.p4_ampl_sb.setMinimum(-99999.000000000000000)
        self.p4_ampl_sb.setMaximum(99999.000000000000000)

        self.gridLayout_6.addWidget(self.p4_ampl_sb, 6, 4, 1, 1)

        self.p6_amp_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p6_amp_sb.setObjectName(u"p6_amp_sb")
        self.p6_amp_sb.setMinimum(-99999.000000000000000)
        self.p6_amp_sb.setMaximum(99999.000000000000000)
        self.p6_amp_sb.setSingleStep(0.500000000000000)
        self.p6_amp_sb.setValue(1.000000000000000)

        self.gridLayout_6.addWidget(self.p6_amp_sb, 4, 6, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 18, 0, 1, 1)

        self.p3_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.p3_cb.setObjectName(u"p3_cb")

        self.gridLayout_6.addWidget(self.p3_cb, 2, 3, 1, 1)

        self.p5_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.p5_cb.setObjectName(u"p5_cb")

        self.gridLayout_6.addWidget(self.p5_cb, 2, 5, 1, 1)

        self.p2_amp_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p2_amp_sb.setObjectName(u"p2_amp_sb")
        self.p2_amp_sb.setMinimum(-99999.000000000000000)
        self.p2_amp_sb.setMaximum(99999.000000000000000)
        self.p2_amp_sb.setSingleStep(0.500000000000000)
        self.p2_amp_sb.setValue(1.000000000000000)

        self.gridLayout_6.addWidget(self.p2_amp_sb, 4, 2, 1, 1)

        self.p2_sig_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p2_sig_sb.setObjectName(u"p2_sig_sb")
        self.p2_sig_sb.setMaximum(500.000000000000000)
        self.p2_sig_sb.setValue(50.000000000000000)

        self.gridLayout_6.addWidget(self.p2_sig_sb, 14, 2, 1, 1)

        self.p2_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.p2_cb.setObjectName(u"p2_cb")

        self.gridLayout_6.addWidget(self.p2_cb, 2, 2, 1, 1)

        self.p4_amph_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p4_amph_sb.setObjectName(u"p4_amph_sb")
        self.p4_amph_sb.setMinimum(-99999.000000000000000)
        self.p4_amph_sb.setMaximum(99999.000000000000000)
        self.p4_amph_sb.setValue(9999.000000000000000)

        self.gridLayout_6.addWidget(self.p4_amph_sb, 7, 4, 1, 1)

        self.p5_amph_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p5_amph_sb.setObjectName(u"p5_amph_sb")
        self.p5_amph_sb.setMinimum(-99999.000000000000000)
        self.p5_amph_sb.setMaximum(99999.000000000000000)
        self.p5_amph_sb.setValue(9999.000000000000000)

        self.gridLayout_6.addWidget(self.p5_amph_sb, 7, 5, 1, 1)

        self.p3_sigh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p3_sigh_sb.setObjectName(u"p3_sigh_sb")
        self.p3_sigh_sb.setMaximum(500.000000000000000)
        self.p3_sigh_sb.setValue(300.000000000000000)

        self.gridLayout_6.addWidget(self.p3_sigh_sb, 17, 3, 1, 1)

        self.p4_sig_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p4_sig_sb.setObjectName(u"p4_sig_sb")
        self.p4_sig_sb.setMaximum(500.000000000000000)
        self.p4_sig_sb.setValue(50.000000000000000)

        self.gridLayout_6.addWidget(self.p4_sig_sb, 14, 4, 1, 1)

        self.p3_ampl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p3_ampl_sb.setObjectName(u"p3_ampl_sb")
        self.p3_ampl_sb.setMinimum(-99999.000000000000000)
        self.p3_ampl_sb.setMaximum(99999.000000000000000)

        self.gridLayout_6.addWidget(self.p3_ampl_sb, 6, 3, 1, 1)

        self.p4_amp_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p4_amp_sb.setObjectName(u"p4_amp_sb")
        self.p4_amp_sb.setMinimum(-99999.000000000000000)
        self.p4_amp_sb.setMaximum(99999.000000000000000)
        self.p4_amp_sb.setSingleStep(0.500000000000000)
        self.p4_amp_sb.setValue(1.000000000000000)

        self.gridLayout_6.addWidget(self.p4_amp_sb, 4, 4, 1, 1)

        self.p3_fwhm = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p3_fwhm.setObjectName(u"p3_fwhm")
        self.p3_fwhm.setMaximum(9999.000000000000000)

        self.gridLayout_6.addWidget(self.p3_fwhm, 18, 3, 1, 1)

        self.p5_ampl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p5_ampl_sb.setObjectName(u"p5_ampl_sb")
        self.p5_ampl_sb.setMinimum(-99999.000000000000000)
        self.p5_ampl_sb.setMaximum(99999.000000000000000)

        self.gridLayout_6.addWidget(self.p5_ampl_sb, 6, 5, 1, 1)

        self.p2_ampl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p2_ampl_sb.setObjectName(u"p2_ampl_sb")
        self.p2_ampl_sb.setMinimum(-99999.000000000000000)
        self.p2_ampl_sb.setMaximum(99999.000000000000000)

        self.gridLayout_6.addWidget(self.p2_ampl_sb, 6, 2, 1, 1)

        self.p3_sigl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p3_sigl_sb.setObjectName(u"p3_sigl_sb")
        self.p3_sigl_sb.setMaximum(500.000000000000000)
        self.p3_sigl_sb.setValue(0.100000000000000)

        self.gridLayout_6.addWidget(self.p3_sigl_sb, 16, 3, 1, 1)

        self.p1_amp_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p1_amp_hold.setObjectName(u"p1_amp_hold")

        self.gridLayout_6.addWidget(self.p1_amp_hold, 5, 1, 1, 1)

        self.p4_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.p4_cb.setObjectName(u"p4_cb")

        self.gridLayout_6.addWidget(self.p4_cb, 2, 4, 1, 1)

        self.p2_cen_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p2_cen_sb.setObjectName(u"p2_cen_sb")
        self.p2_cen_sb.setMaximum(4000.000000000000000)
        self.p2_cen_sb.setValue(1500.000000000000000)

        self.gridLayout_6.addWidget(self.p2_cen_sb, 9, 2, 1, 1)

        self.p1_amp_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p1_amp_sb.setObjectName(u"p1_amp_sb")
        self.p1_amp_sb.setMinimum(-99999.000000000000000)
        self.p1_amp_sb.setMaximum(99999.000000000000000)
        self.p1_amp_sb.setSingleStep(0.500000000000000)
        self.p1_amp_sb.setValue(1.000000000000000)

        self.gridLayout_6.addWidget(self.p1_amp_sb, 4, 1, 1, 1)

        self.p5_amp_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p5_amp_sb.setObjectName(u"p5_amp_sb")
        self.p5_amp_sb.setMinimum(-99999.000000000000000)
        self.p5_amp_sb.setMaximum(99999.000000000000000)
        self.p5_amp_sb.setSingleStep(0.500000000000000)
        self.p5_amp_sb.setValue(1.000000000000000)

        self.gridLayout_6.addWidget(self.p5_amp_sb, 4, 5, 1, 1)

        self.p1_fwhm = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p1_fwhm.setObjectName(u"p1_fwhm")
        self.p1_fwhm.setMaximum(9999.000000000000000)

        self.gridLayout_6.addWidget(self.p1_fwhm, 18, 1, 1, 1)

        self.p5_sigh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p5_sigh_sb.setObjectName(u"p5_sigh_sb")
        self.p5_sigh_sb.setMaximum(500.000000000000000)
        self.p5_sigh_sb.setValue(300.000000000000000)

        self.gridLayout_6.addWidget(self.p5_sigh_sb, 17, 5, 1, 1)

        self.p5_sigl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p5_sigl_sb.setObjectName(u"p5_sigl_sb")
        self.p5_sigl_sb.setMaximum(500.000000000000000)
        self.p5_sigl_sb.setValue(0.100000000000000)

        self.gridLayout_6.addWidget(self.p5_sigl_sb, 16, 5, 1, 1)

        self.p4_sigl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p4_sigl_sb.setObjectName(u"p4_sigl_sb")
        self.p4_sigl_sb.setMaximum(500.000000000000000)
        self.p4_sigl_sb.setValue(0.100000000000000)

        self.gridLayout_6.addWidget(self.p4_sigl_sb, 16, 4, 1, 1)

        self.p4_fwhm = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p4_fwhm.setObjectName(u"p4_fwhm")
        self.p4_fwhm.setMaximum(9999.000000000000000)

        self.gridLayout_6.addWidget(self.p4_fwhm, 18, 4, 1, 1)

        self.p5_cen_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p5_cen_sb.setObjectName(u"p5_cen_sb")
        self.p5_cen_sb.setMaximum(4000.000000000000000)
        self.p5_cen_sb.setValue(3000.000000000000000)

        self.gridLayout_6.addWidget(self.p5_cen_sb, 9, 5, 1, 1)

        self.p5_sig_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p5_sig_sb.setObjectName(u"p5_sig_sb")
        self.p5_sig_sb.setMaximum(500.000000000000000)
        self.p5_sig_sb.setValue(50.000000000000000)

        self.gridLayout_6.addWidget(self.p5_sig_sb, 14, 5, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 9, 0, 1, 1)

        self.p3_amph_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p3_amph_sb.setObjectName(u"p3_amph_sb")
        self.p3_amph_sb.setMinimum(-99999.000000000000000)
        self.p3_amph_sb.setMaximum(99999.000000000000000)
        self.p3_amph_sb.setValue(9999.000000000000000)

        self.gridLayout_6.addWidget(self.p3_amph_sb, 7, 3, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_6.addWidget(self.label_17, 2, 0, 1, 1)

        self.p5_cen_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p5_cen_hold.setObjectName(u"p5_cen_hold")

        self.gridLayout_6.addWidget(self.p5_cen_hold, 10, 5, 1, 1)

        self.p2_amph_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p2_amph_sb.setObjectName(u"p2_amph_sb")
        self.p2_amph_sb.setMinimum(-99999.000000000000000)
        self.p2_amph_sb.setMaximum(99999.000000000000000)
        self.p2_amph_sb.setValue(9999.000000000000000)

        self.gridLayout_6.addWidget(self.p2_amph_sb, 7, 2, 1, 1)

        self.p1_ampl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p1_ampl_sb.setObjectName(u"p1_ampl_sb")
        self.p1_ampl_sb.setMinimum(-99999.000000000000000)
        self.p1_ampl_sb.setMaximum(99999.000000000000000)

        self.gridLayout_6.addWidget(self.p1_ampl_sb, 6, 1, 1, 1)

        self.p3_amp_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p3_amp_sb.setObjectName(u"p3_amp_sb")
        self.p3_amp_sb.setMinimum(-99999.000000000000000)
        self.p3_amp_sb.setMaximum(99999.000000000000000)
        self.p3_amp_sb.setSingleStep(0.500000000000000)
        self.p3_amp_sb.setValue(1.000000000000000)

        self.gridLayout_6.addWidget(self.p3_amp_sb, 4, 3, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 6, 0, 1, 1)

        self.p1_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.p1_cb.setObjectName(u"p1_cb")
        self.p1_cb.setChecked(True)

        self.gridLayout_6.addWidget(self.p1_cb, 2, 1, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 4, 0, 1, 1)

        self.p1_cen_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p1_cen_hold.setObjectName(u"p1_cen_hold")

        self.gridLayout_6.addWidget(self.p1_cen_hold, 10, 1, 1, 1)

        self.p2_fwhm = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p2_fwhm.setObjectName(u"p2_fwhm")
        self.p2_fwhm.setMaximum(9999.000000000000000)

        self.gridLayout_6.addWidget(self.p2_fwhm, 18, 2, 1, 1)

        self.p3_cen_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p3_cen_sb.setObjectName(u"p3_cen_sb")
        self.p3_cen_sb.setMaximum(4000.000000000000000)
        self.p3_cen_sb.setValue(2000.000000000000000)

        self.gridLayout_6.addWidget(self.p3_cen_sb, 9, 3, 1, 1)

        self.p4_amp_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p4_amp_hold.setObjectName(u"p4_amp_hold")

        self.gridLayout_6.addWidget(self.p4_amp_hold, 5, 4, 1, 1)

        self.p1_sigl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p1_sigl_sb.setObjectName(u"p1_sigl_sb")
        self.p1_sigl_sb.setMaximum(500.000000000000000)
        self.p1_sigl_sb.setValue(0.100000000000000)

        self.gridLayout_6.addWidget(self.p1_sigl_sb, 16, 1, 1, 1)

        self.p4_sigma_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p4_sigma_hold.setObjectName(u"p4_sigma_hold")

        self.gridLayout_6.addWidget(self.p4_sigma_hold, 15, 4, 1, 1)

        self.p3_cenh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p3_cenh_sb.setObjectName(u"p3_cenh_sb")
        self.p3_cenh_sb.setMaximum(4000.000000000000000)
        self.p3_cenh_sb.setValue(4000.000000000000000)

        self.gridLayout_6.addWidget(self.p3_cenh_sb, 12, 3, 1, 1)

        self.p1_cenl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p1_cenl_sb.setObjectName(u"p1_cenl_sb")
        self.p1_cenl_sb.setMaximum(4000.000000000000000)
        self.p1_cenl_sb.setValue(400.000000000000000)

        self.gridLayout_6.addWidget(self.p1_cenl_sb, 11, 1, 1, 1)

        self.p2_sigl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p2_sigl_sb.setObjectName(u"p2_sigl_sb")
        self.p2_sigl_sb.setMaximum(500.000000000000000)
        self.p2_sigl_sb.setValue(0.100000000000000)

        self.gridLayout_6.addWidget(self.p2_sigl_sb, 16, 2, 1, 1)

        self.p2_sigh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p2_sigh_sb.setObjectName(u"p2_sigh_sb")
        self.p2_sigh_sb.setMaximum(500.000000000000000)
        self.p2_sigh_sb.setValue(300.000000000000000)

        self.gridLayout_6.addWidget(self.p2_sigh_sb, 17, 2, 1, 1)

        self.p1_cen_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p1_cen_sb.setObjectName(u"p1_cen_sb")
        self.p1_cen_sb.setMaximum(4000.000000000000000)
        self.p1_cen_sb.setValue(1000.000000000000000)

        self.gridLayout_6.addWidget(self.p1_cen_sb, 9, 1, 1, 1)

        self.p2_amp_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p2_amp_hold.setObjectName(u"p2_amp_hold")

        self.gridLayout_6.addWidget(self.p2_amp_hold, 5, 2, 1, 1)

        self.p3_cen_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p3_cen_hold.setObjectName(u"p3_cen_hold")

        self.gridLayout_6.addWidget(self.p3_cen_hold, 10, 3, 1, 1)

        self.p4_cen_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p4_cen_sb.setObjectName(u"p4_cen_sb")
        self.p4_cen_sb.setMaximum(4000.000000000000000)
        self.p4_cen_sb.setValue(2500.000000000000000)

        self.gridLayout_6.addWidget(self.p4_cen_sb, 9, 4, 1, 1)

        self.p5_cenl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p5_cenl_sb.setObjectName(u"p5_cenl_sb")
        self.p5_cenl_sb.setMaximum(4000.000000000000000)
        self.p5_cenl_sb.setValue(400.000000000000000)

        self.gridLayout_6.addWidget(self.p5_cenl_sb, 11, 5, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 12, 0, 1, 1)

        self.p4_sigh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p4_sigh_sb.setObjectName(u"p4_sigh_sb")
        self.p4_sigh_sb.setMaximum(500.000000000000000)
        self.p4_sigh_sb.setValue(300.000000000000000)

        self.gridLayout_6.addWidget(self.p4_sigh_sb, 17, 4, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 16, 0, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 17, 0, 1, 1)

        self.p2_cenl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p2_cenl_sb.setObjectName(u"p2_cenl_sb")
        self.p2_cenl_sb.setMaximum(4000.000000000000000)
        self.p2_cenl_sb.setValue(400.000000000000000)

        self.gridLayout_6.addWidget(self.p2_cenl_sb, 11, 2, 1, 1)

        self.p5_amp_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p5_amp_hold.setObjectName(u"p5_amp_hold")

        self.gridLayout_6.addWidget(self.p5_amp_hold, 5, 5, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 11, 0, 1, 1)

        self.p3_sig_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p3_sig_sb.setObjectName(u"p3_sig_sb")
        self.p3_sig_sb.setMaximum(500.000000000000000)
        self.p3_sig_sb.setValue(50.000000000000000)

        self.gridLayout_6.addWidget(self.p3_sig_sb, 14, 3, 1, 1)

        self.p4_cen_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p4_cen_hold.setObjectName(u"p4_cen_hold")

        self.gridLayout_6.addWidget(self.p4_cen_hold, 10, 4, 1, 1)

        self.p4_cenh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p4_cenh_sb.setObjectName(u"p4_cenh_sb")
        self.p4_cenh_sb.setMaximum(4000.000000000000000)
        self.p4_cenh_sb.setValue(4000.000000000000000)

        self.gridLayout_6.addWidget(self.p4_cenh_sb, 12, 4, 1, 1)

        self.p1_amph_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p1_amph_sb.setObjectName(u"p1_amph_sb")
        self.p1_amph_sb.setMinimum(-99999.000000000000000)
        self.p1_amph_sb.setMaximum(99999.000000000000000)
        self.p1_amph_sb.setValue(9999.000000000000000)

        self.gridLayout_6.addWidget(self.p1_amph_sb, 7, 1, 1, 1)

        self.p5_cenh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p5_cenh_sb.setObjectName(u"p5_cenh_sb")
        self.p5_cenh_sb.setMaximum(4000.000000000000000)
        self.p5_cenh_sb.setValue(4000.000000000000000)

        self.gridLayout_6.addWidget(self.p5_cenh_sb, 12, 5, 1, 1)

        self.p1_cenh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p1_cenh_sb.setObjectName(u"p1_cenh_sb")
        self.p1_cenh_sb.setMaximum(4000.000000000000000)
        self.p1_cenh_sb.setValue(4000.000000000000000)

        self.gridLayout_6.addWidget(self.p1_cenh_sb, 12, 1, 1, 1)

        self.p3_amp_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p3_amp_hold.setObjectName(u"p3_amp_hold")

        self.gridLayout_6.addWidget(self.p3_amp_hold, 5, 3, 1, 1)

        self.p1_sig_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p1_sig_sb.setObjectName(u"p1_sig_sb")
        self.p1_sig_sb.setMaximum(500.000000000000000)
        self.p1_sig_sb.setValue(50.000000000000000)

        self.gridLayout_6.addWidget(self.p1_sig_sb, 14, 1, 1, 1)

        self.p2_cen_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p2_cen_hold.setObjectName(u"p2_cen_hold")

        self.gridLayout_6.addWidget(self.p2_cen_hold, 10, 2, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_6.addWidget(self.label_10, 7, 0, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 14, 0, 1, 1)

        self.p1_sigma_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p1_sigma_hold.setObjectName(u"p1_sigma_hold")

        self.gridLayout_6.addWidget(self.p1_sigma_hold, 15, 1, 1, 1)

        self.p5_sigma_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p5_sigma_hold.setObjectName(u"p5_sigma_hold")

        self.gridLayout_6.addWidget(self.p5_sigma_hold, 15, 5, 1, 1)

        self.p3_sigma_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p3_sigma_hold.setObjectName(u"p3_sigma_hold")

        self.gridLayout_6.addWidget(self.p3_sigma_hold, 15, 3, 1, 1)

        self.p2_sigma_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p2_sigma_hold.setObjectName(u"p2_sigma_hold")

        self.gridLayout_6.addWidget(self.p2_sigma_hold, 15, 2, 1, 1)

        self.p6_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.p6_cb.setObjectName(u"p6_cb")

        self.gridLayout_6.addWidget(self.p6_cb, 2, 6, 1, 1)

        self.p6_ampl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p6_ampl_sb.setObjectName(u"p6_ampl_sb")
        self.p6_ampl_sb.setMinimum(-99999.000000000000000)
        self.p6_ampl_sb.setMaximum(99999.000000000000000)

        self.gridLayout_6.addWidget(self.p6_ampl_sb, 6, 6, 1, 1)

        self.p7_ampl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p7_ampl_sb.setObjectName(u"p7_ampl_sb")
        self.p7_ampl_sb.setMinimum(-99999.000000000000000)
        self.p7_ampl_sb.setMaximum(99999.000000000000000)

        self.gridLayout_6.addWidget(self.p7_ampl_sb, 6, 7, 1, 1)

        self.p2_cenh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p2_cenh_sb.setObjectName(u"p2_cenh_sb")
        self.p2_cenh_sb.setMaximum(4000.000000000000000)
        self.p2_cenh_sb.setValue(4000.000000000000000)

        self.gridLayout_6.addWidget(self.p2_cenh_sb, 12, 2, 1, 1)

        self.p7_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.p7_cb.setObjectName(u"p7_cb")

        self.gridLayout_6.addWidget(self.p7_cb, 2, 7, 1, 1)

        self.p7_amp_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p7_amp_sb.setObjectName(u"p7_amp_sb")
        self.p7_amp_sb.setMinimum(-99999.000000000000000)
        self.p7_amp_sb.setMaximum(99999.000000000000000)
        self.p7_amp_sb.setSingleStep(0.500000000000000)
        self.p7_amp_sb.setValue(1.000000000000000)

        self.gridLayout_6.addWidget(self.p7_amp_sb, 4, 7, 1, 1)

        self.p1_sigh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p1_sigh_sb.setObjectName(u"p1_sigh_sb")
        self.p1_sigh_sb.setMaximum(500.000000000000000)
        self.p1_sigh_sb.setValue(300.000000000000000)

        self.gridLayout_6.addWidget(self.p1_sigh_sb, 17, 1, 1, 1)

        self.p8_amp_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p8_amp_sb.setObjectName(u"p8_amp_sb")
        self.p8_amp_sb.setMinimum(-99999.000000000000000)
        self.p8_amp_sb.setMaximum(99999.000000000000000)
        self.p8_amp_sb.setSingleStep(0.500000000000000)
        self.p8_amp_sb.setValue(1.000000000000000)

        self.gridLayout_6.addWidget(self.p8_amp_sb, 4, 8, 1, 1)

        self.p4_cenl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p4_cenl_sb.setObjectName(u"p4_cenl_sb")
        self.p4_cenl_sb.setMaximum(4000.000000000000000)
        self.p4_cenl_sb.setValue(400.000000000000000)

        self.gridLayout_6.addWidget(self.p4_cenl_sb, 11, 4, 1, 1)

        self.p3_cenl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p3_cenl_sb.setObjectName(u"p3_cenl_sb")
        self.p3_cenl_sb.setMaximum(4000.000000000000000)
        self.p3_cenl_sb.setValue(400.000000000000000)

        self.gridLayout_6.addWidget(self.p3_cenl_sb, 11, 3, 1, 1)

        self.p6_sigh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p6_sigh_sb.setObjectName(u"p6_sigh_sb")

        self.gridLayout_6.addWidget(self.p6_sigh_sb, 17, 6, 1, 1)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_4, 8, 0, 1, 9)

        self.p8_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.p8_cb.setObjectName(u"p8_cb")

        self.gridLayout_6.addWidget(self.p8_cb, 2, 8, 1, 1)

        self.p8_cenh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p8_cenh_sb.setObjectName(u"p8_cenh_sb")

        self.gridLayout_6.addWidget(self.p8_cenh_sb, 12, 8, 1, 1)

        self.p6_cenh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p6_cenh_sb.setObjectName(u"p6_cenh_sb")

        self.gridLayout_6.addWidget(self.p6_cenh_sb, 12, 6, 1, 1)

        self.p8_cen_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p8_cen_hold.setObjectName(u"p8_cen_hold")

        self.gridLayout_6.addWidget(self.p8_cen_hold, 10, 8, 1, 1)

        self.p7_sig_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p7_sig_sb.setObjectName(u"p7_sig_sb")

        self.gridLayout_6.addWidget(self.p7_sig_sb, 14, 7, 1, 1)

        self.p7_amph_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p7_amph_sb.setObjectName(u"p7_amph_sb")
        self.p7_amph_sb.setMinimum(-99999.000000000000000)
        self.p7_amph_sb.setMaximum(99999.000000000000000)
        self.p7_amph_sb.setValue(99.989999999999995)

        self.gridLayout_6.addWidget(self.p7_amph_sb, 7, 7, 1, 1)

        self.p8_amph_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p8_amph_sb.setObjectName(u"p8_amph_sb")
        self.p8_amph_sb.setMinimum(-99999.000000000000000)
        self.p8_amph_sb.setMaximum(99999.000000000000000)
        self.p8_amph_sb.setValue(99.989999999999995)

        self.gridLayout_6.addWidget(self.p8_amph_sb, 7, 8, 1, 1)

        self.p7_sigma_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p7_sigma_hold.setObjectName(u"p7_sigma_hold")

        self.gridLayout_6.addWidget(self.p7_sigma_hold, 15, 7, 1, 1)

        self.p6_amp_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p6_amp_hold.setObjectName(u"p6_amp_hold")

        self.gridLayout_6.addWidget(self.p6_amp_hold, 5, 6, 1, 1)

        self.p6_sigma_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p6_sigma_hold.setObjectName(u"p6_sigma_hold")

        self.gridLayout_6.addWidget(self.p6_sigma_hold, 15, 6, 1, 1)

        self.p8_sig_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p8_sig_sb.setObjectName(u"p8_sig_sb")

        self.gridLayout_6.addWidget(self.p8_sig_sb, 14, 8, 1, 1)

        self.p8_ampl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p8_ampl_sb.setObjectName(u"p8_ampl_sb")
        self.p8_ampl_sb.setMinimum(-99999.000000000000000)
        self.p8_ampl_sb.setMaximum(99999.000000000000000)

        self.gridLayout_6.addWidget(self.p8_ampl_sb, 6, 8, 1, 1)

        self.p8_sigma_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p8_sigma_hold.setObjectName(u"p8_sigma_hold")

        self.gridLayout_6.addWidget(self.p8_sigma_hold, 15, 8, 1, 1)

        self.p6_amph_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p6_amph_sb.setObjectName(u"p6_amph_sb")
        self.p6_amph_sb.setMinimum(-99999.000000000000000)
        self.p6_amph_sb.setMaximum(99999.000000000000000)
        self.p6_amph_sb.setValue(99.989999999999995)

        self.gridLayout_6.addWidget(self.p6_amph_sb, 7, 6, 1, 1)

        self.p8_cen_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p8_cen_sb.setObjectName(u"p8_cen_sb")

        self.gridLayout_6.addWidget(self.p8_cen_sb, 9, 8, 1, 1)

        self.p7_cen_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p7_cen_hold.setObjectName(u"p7_cen_hold")

        self.gridLayout_6.addWidget(self.p7_cen_hold, 10, 7, 1, 1)

        self.p7_amp_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p7_amp_hold.setObjectName(u"p7_amp_hold")

        self.gridLayout_6.addWidget(self.p7_amp_hold, 5, 7, 1, 1)

        self.p7_cen_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p7_cen_sb.setObjectName(u"p7_cen_sb")

        self.gridLayout_6.addWidget(self.p7_cen_sb, 9, 7, 1, 1)

        self.p8_amp_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p8_amp_hold.setObjectName(u"p8_amp_hold")

        self.gridLayout_6.addWidget(self.p8_amp_hold, 5, 8, 1, 1)

        self.p6_cenl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p6_cenl_sb.setObjectName(u"p6_cenl_sb")

        self.gridLayout_6.addWidget(self.p6_cenl_sb, 11, 6, 1, 1)

        self.p7_sigl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p7_sigl_sb.setObjectName(u"p7_sigl_sb")

        self.gridLayout_6.addWidget(self.p7_sigl_sb, 16, 7, 1, 1)

        self.p8_cenl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p8_cenl_sb.setObjectName(u"p8_cenl_sb")

        self.gridLayout_6.addWidget(self.p8_cenl_sb, 11, 8, 1, 1)

        self.p7_cenl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p7_cenl_sb.setObjectName(u"p7_cenl_sb")

        self.gridLayout_6.addWidget(self.p7_cenl_sb, 11, 7, 1, 1)

        self.p6_sig_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p6_sig_sb.setObjectName(u"p6_sig_sb")

        self.gridLayout_6.addWidget(self.p6_sig_sb, 14, 6, 1, 1)

        self.p6_sigl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p6_sigl_sb.setObjectName(u"p6_sigl_sb")

        self.gridLayout_6.addWidget(self.p6_sigl_sb, 16, 6, 1, 1)

        self.p6_cen_hold = QCheckBox(self.scrollAreaWidgetContents)
        self.p6_cen_hold.setObjectName(u"p6_cen_hold")

        self.gridLayout_6.addWidget(self.p6_cen_hold, 10, 6, 1, 1)

        self.p8_sigl_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p8_sigl_sb.setObjectName(u"p8_sigl_sb")

        self.gridLayout_6.addWidget(self.p8_sigl_sb, 16, 8, 1, 1)

        self.p6_fwhm = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p6_fwhm.setObjectName(u"p6_fwhm")

        self.gridLayout_6.addWidget(self.p6_fwhm, 18, 6, 1, 1)

        self.p7_cenh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p7_cenh_sb.setObjectName(u"p7_cenh_sb")

        self.gridLayout_6.addWidget(self.p7_cenh_sb, 12, 7, 1, 1)

        self.p6_cen_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p6_cen_sb.setObjectName(u"p6_cen_sb")

        self.gridLayout_6.addWidget(self.p6_cen_sb, 9, 6, 1, 1)

        self.fit_results_te = QTextEdit(self.scrollAreaWidgetContents)
        self.fit_results_te.setObjectName(u"fit_results_te")
        self.fit_results_te.setMinimumSize(QSize(0, 400))

        self.gridLayout_6.addWidget(self.fit_results_te, 22, 0, 1, 9)

        self.p7_sigh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p7_sigh_sb.setObjectName(u"p7_sigh_sb")

        self.gridLayout_6.addWidget(self.p7_sigh_sb, 17, 7, 1, 1)

        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_6, 3, 0, 1, 9)

        self.line_7 = QFrame(self.scrollAreaWidgetContents)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_7, 19, 0, 1, 9)

        self.p7_fwhm = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p7_fwhm.setObjectName(u"p7_fwhm")

        self.gridLayout_6.addWidget(self.p7_fwhm, 18, 7, 1, 1)

        self.p8_sigh_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p8_sigh_sb.setObjectName(u"p8_sigh_sb")

        self.gridLayout_6.addWidget(self.p8_sigh_sb, 17, 8, 1, 1)

        self.p8_fwhm = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.p8_fwhm.setObjectName(u"p8_fwhm")

        self.gridLayout_6.addWidget(self.p8_fwhm, 18, 8, 1, 1)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_5, 13, 0, 1, 9)

        self.ir_range_cb = QComboBox(self.scrollAreaWidgetContents)
        self.ir_range_cb.setObjectName(u"ir_range_cb")

        self.gridLayout_6.addWidget(self.ir_range_cb, 1, 3, 1, 4)

        self.select_ir_range_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.select_ir_range_cb.setObjectName(u"select_ir_range_cb")

        self.gridLayout_6.addWidget(self.select_ir_range_cb, 1, 1, 1, 2)

        self.baseline_combo = QLabel(self.scrollAreaWidgetContents)
        self.baseline_combo.setObjectName(u"baseline_combo")

        self.gridLayout_6.addWidget(self.baseline_combo, 21, 0, 1, 1)

        self.plot_components_box = QCheckBox(self.scrollAreaWidgetContents)
        self.plot_components_box.setObjectName(u"plot_components_box")

        self.gridLayout_6.addWidget(self.plot_components_box, 20, 1, 1, 2)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_6.addWidget(self.comboBox, 21, 1, 1, 2)

        self.clear_fit_pb = QPushButton(self.scrollAreaWidgetContents)
        self.clear_fit_pb.setObjectName(u"clear_fit_pb")

        self.gridLayout_6.addWidget(self.clear_fit_pb, 1, 0, 1, 1)

        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_6.addWidget(self.label_18, 20, 3, 1, 1)

        self.slope_dsb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.slope_dsb.setObjectName(u"slope_dsb")
        self.slope_dsb.setMinimum(-999999.000000000000000)
        self.slope_dsb.setMaximum(999999.000000000000000)

        self.gridLayout_6.addWidget(self.slope_dsb, 20, 4, 1, 1)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_6.addWidget(self.label_19, 21, 3, 1, 1)

        self.intercept_dsb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.intercept_dsb.setObjectName(u"intercept_dsb")
        self.intercept_dsb.setMinimum(-999999.000000000000000)
        self.intercept_dsb.setMaximum(999999.000000000000000)

        self.gridLayout_6.addWidget(self.intercept_dsb, 21, 4, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 1, 1, 1, 6)

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
        self.label_5.setText(QCoreApplication.translate("DockWidget", u"Skip Rows", None))
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
        self.fit_init_pb.setText(QCoreApplication.translate("DockWidget", u"Fit Init", None))
        self.fit_pb.setText(QCoreApplication.translate("DockWidget", u"Fit", None))
        self.select_data_pb.setText(QCoreApplication.translate("DockWidget", u"Select Data", None))
        self.plot_3sig_box.setText(QCoreApplication.translate("DockWidget", u"Plot 3 sig", None))
        self.label_2.setText(QCoreApplication.translate("DockWidget", u"FWHM", None))
        self.p3_cb.setText(QCoreApplication.translate("DockWidget", u"Peak 3", None))
        self.p5_cb.setText(QCoreApplication.translate("DockWidget", u"Peak 5", None))
        self.p2_cb.setText(QCoreApplication.translate("DockWidget", u"Peak 2", None))
        self.p1_amp_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p4_cb.setText(QCoreApplication.translate("DockWidget", u"Peak 4", None))
        self.label_11.setText(QCoreApplication.translate("DockWidget", u"Cen", None))
        self.label_17.setText(QCoreApplication.translate("DockWidget", u"Peak #", None))
        self.p5_cen_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.label_9.setText(QCoreApplication.translate("DockWidget", u"low", None))
        self.p1_cb.setText(QCoreApplication.translate("DockWidget", u"Peak 1", None))
        self.label_8.setText(QCoreApplication.translate("DockWidget", u"Amp", None))
        self.p1_cen_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p4_amp_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p4_sigma_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p2_amp_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p3_cen_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.label_13.setText(QCoreApplication.translate("DockWidget", u"high", None))
        self.label_15.setText(QCoreApplication.translate("DockWidget", u"low", None))
        self.label_16.setText(QCoreApplication.translate("DockWidget", u"high", None))
        self.p5_amp_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.label_12.setText(QCoreApplication.translate("DockWidget", u"low", None))
        self.p4_cen_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p3_amp_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p2_cen_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.label_10.setText(QCoreApplication.translate("DockWidget", u"high", None))
        self.label_14.setText(QCoreApplication.translate("DockWidget", u"sigma", None))
        self.p1_sigma_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p5_sigma_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p3_sigma_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p2_sigma_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p6_cb.setText(QCoreApplication.translate("DockWidget", u"Peak 6", None))
        self.p7_cb.setText(QCoreApplication.translate("DockWidget", u"Peak 7", None))
        self.p8_cb.setText(QCoreApplication.translate("DockWidget", u"Peak 8", None))
        self.p8_cen_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p7_sigma_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p6_amp_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p6_sigma_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p8_sigma_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p7_cen_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p7_amp_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p8_amp_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.p6_cen_hold.setText(QCoreApplication.translate("DockWidget", u"Hold", None))
        self.select_ir_range_cb.setText(QCoreApplication.translate("DockWidget", u"Get IR Fit Range", None))
        self.baseline_combo.setText(QCoreApplication.translate("DockWidget", u"Baseline", None))
        self.plot_components_box.setText(QCoreApplication.translate("DockWidget", u"Plot Components", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("DockWidget", u"None", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("DockWidget", u"Linear", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("DockWidget", u"Constant", None))

        self.clear_fit_pb.setText(QCoreApplication.translate("DockWidget", u"Clear Fitting", None))
        self.label_18.setText(QCoreApplication.translate("DockWidget", u"slope", None))
        self.label_19.setText(QCoreApplication.translate("DockWidget", u"intercept", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("DockWidget", u"Fit Panel", None))
    # retranslateUi

