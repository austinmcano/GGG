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
        DockWidget.resize(643, 681)
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
        self.SE_treeView = QTreeView(self.tab_3)
        self.SE_treeView.setObjectName(u"SE_treeView")

        self.gridLayout_3.addWidget(self.SE_treeView, 0, 1, 1, 3)

        self.tabWidget_3 = QTabWidget(self.tab_3)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_9 = QGridLayout(self.tab_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.tw_x = QTreeWidget(self.tab_7)
        self.tw_x.setObjectName(u"tw_x")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tw_x.sizePolicy().hasHeightForWidth())
        self.tw_x.setSizePolicy(sizePolicy)

        self.gridLayout_9.addWidget(self.tw_x, 0, 0, 1, 1)

        self.label_7 = QLabel(self.tab_7)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_9.addWidget(self.label_7, 2, 0, 1, 1)

        self.tw_y = QTreeWidget(self.tab_7)
        self.tw_y.setObjectName(u"tw_y")
        self.tw_y.setSelectionMode(QAbstractItemView.SingleSelection)

        self.gridLayout_9.addWidget(self.tw_y, 0, 1, 1, 1)

        self.skip_rows_sb = QSpinBox(self.tab_7)
        self.skip_rows_sb.setObjectName(u"skip_rows_sb")

        self.gridLayout_9.addWidget(self.skip_rows_sb, 2, 1, 1, 1)

        self.fill_cols_pb = QPushButton(self.tab_7)
        self.fill_cols_pb.setObjectName(u"fill_cols_pb")

        self.gridLayout_9.addWidget(self.fill_cols_pb, 3, 0, 1, 1)

        self.ax_cb = QComboBox(self.tab_7)
        self.ax_cb.addItem("")
        self.ax_cb.addItem("")
        self.ax_cb.setObjectName(u"ax_cb")

        self.gridLayout_9.addWidget(self.ax_cb, 4, 0, 1, 1)

        self.plot_type_cb = QComboBox(self.tab_7)
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.setObjectName(u"plot_type_cb")

        self.gridLayout_9.addWidget(self.plot_type_cb, 3, 1, 1, 1)

        self.plot_pb = QPushButton(self.tab_7)
        self.plot_pb.setObjectName(u"plot_pb")

        self.gridLayout_9.addWidget(self.plot_pb, 4, 1, 1, 1)

        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_10 = QGridLayout(self.tab_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.ylabel_le = QLineEdit(self.tab_8)
        self.ylabel_le.setObjectName(u"ylabel_le")

        self.gridLayout_10.addWidget(self.ylabel_le, 1, 1, 1, 1)

        self.xlabel_le = QLineEdit(self.tab_8)
        self.xlabel_le.setObjectName(u"xlabel_le")

        self.gridLayout_10.addWidget(self.xlabel_le, 1, 0, 1, 1)

        self.secolorpb = QPushButton(self.tab_8)
        self.secolorpb.setObjectName(u"secolorpb")

        self.gridLayout_10.addWidget(self.secolorpb, 3, 1, 1, 1)

        self.label_9 = QLabel(self.tab_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_10.addWidget(self.label_9, 0, 1, 1, 1)

        self.label_8 = QLabel(self.tab_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_10.addWidget(self.label_8, 0, 0, 1, 1)

        self.error_checkbox = QCheckBox(self.tab_8)
        self.error_checkbox.setObjectName(u"error_checkbox")

        self.gridLayout_10.addWidget(self.error_checkbox, 7, 1, 1, 1)

        self.label_18 = QLabel(self.tab_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_10.addWidget(self.label_18, 5, 1, 1, 1)

        self.semarkersize = QDoubleSpinBox(self.tab_8)
        self.semarkersize.setObjectName(u"semarkersize")
        self.semarkersize.setMaximum(9999.000000000000000)
        self.semarkersize.setValue(20.000000000000000)

        self.gridLayout_10.addWidget(self.semarkersize, 6, 1, 1, 1)

        self.comboBox = QComboBox(self.tab_8)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_10.addWidget(self.comboBox, 8, 1, 1, 1)

        self.zero_correct_checkb = QCheckBox(self.tab_8)
        self.zero_correct_checkb.setObjectName(u"zero_correct_checkb")
        self.zero_correct_checkb.setChecked(False)

        self.gridLayout_10.addWidget(self.zero_correct_checkb, 4, 1, 1, 1)

        self.error_tw = QTreeWidget(self.tab_8)
        self.error_tw.setObjectName(u"error_tw")

        self.gridLayout_10.addWidget(self.error_tw, 3, 0, 7, 1)

        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_11 = QGridLayout(self.tab_9)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.scrollArea_2 = QScrollArea(self.tab_9)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 575, 275))
        self.gridLayout_12 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.linfitall_pb = QPushButton(self.scrollAreaWidgetContents_2)
        self.linfitall_pb.setObjectName(u"linfitall_pb")

        self.gridLayout_12.addWidget(self.linfitall_pb, 1, 1, 1, 1)

        self.lin_fit_pb = QPushButton(self.scrollAreaWidgetContents_2)
        self.lin_fit_pb.setObjectName(u"lin_fit_pb")

        self.gridLayout_12.addWidget(self.lin_fit_pb, 1, 0, 1, 1)

        self.selectrange_box = QCheckBox(self.scrollAreaWidgetContents_2)
        self.selectrange_box.setObjectName(u"selectrange_box")

        self.gridLayout_12.addWidget(self.selectrange_box, 0, 0, 1, 1)

        self.adosethickchange = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.adosethickchange.setObjectName(u"adosethickchange")
        self.adosethickchange.setMinimum(-9999.000000000000000)
        self.adosethickchange.setMaximum(9999.000000000000000)

        self.gridLayout_12.addWidget(self.adosethickchange, 5, 0, 1, 1)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_12.addWidget(self.label_20, 2, 0, 1, 1)

        self.label_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_12.addWidget(self.label_21, 4, 0, 1, 1)

        self.negthickchange = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.negthickchange.setObjectName(u"negthickchange")
        self.negthickchange.setMinimum(-9999.000000000000000)
        self.negthickchange.setMaximum(9999.000000000000000)

        self.gridLayout_12.addWidget(self.negthickchange, 3, 0, 1, 1)

        self.bdosethickchange = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.bdosethickchange.setObjectName(u"bdosethickchange")
        self.bdosethickchange.setMinimum(-9999.000000000000000)
        self.bdosethickchange.setMaximum(9999.000000000000000)

        self.gridLayout_12.addWidget(self.bdosethickchange, 5, 1, 1, 1)

        self.label_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_12.addWidget(self.label_22, 4, 1, 1, 1)

        self.label_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_12.addWidget(self.label_19, 2, 1, 1, 1)

        self.posthickchange = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.posthickchange.setObjectName(u"posthickchange")
        self.posthickchange.setMinimum(-9999.000000000000000)
        self.posthickchange.setMaximum(9999.000000000000000)

        self.gridLayout_12.addWidget(self.posthickchange, 3, 1, 1, 1)

        self.fit_results_TE = QTextEdit(self.scrollAreaWidgetContents_2)
        self.fit_results_TE.setObjectName(u"fit_results_TE")

        self.gridLayout_12.addWidget(self.fit_results_TE, 6, 0, 1, 2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_11.addWidget(self.scrollArea_2, 0, 1, 1, 2)

        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_3.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabWidget_3, 1, 1, 1, 3)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.treeView_qms = QTreeView(self.tab)
        self.treeView_qms.setObjectName(u"treeView_qms")

        self.gridLayout_2.addWidget(self.treeView_qms, 0, 0, 1, 3)

        self.fill_cols_qms_pb = QPushButton(self.tab)
        self.fill_cols_qms_pb.setObjectName(u"fill_cols_qms_pb")

        self.gridLayout_2.addWidget(self.fill_cols_qms_pb, 2, 0, 1, 1)

        self.plot_qms_pb = QPushButton(self.tab)
        self.plot_qms_pb.setObjectName(u"plot_qms_pb")

        self.gridLayout_2.addWidget(self.plot_qms_pb, 2, 1, 1, 2)

        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_6 = QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.qmsx_tw = QTreeWidget(self.tab_5)
        self.qmsx_tw.setObjectName(u"qmsx_tw")

        self.gridLayout_6.addWidget(self.qmsx_tw, 0, 0, 1, 1)

        self.qmsy_tw = QTreeWidget(self.tab_5)
        self.qmsy_tw.setObjectName(u"qmsy_tw")

        self.gridLayout_6.addWidget(self.qmsy_tw, 0, 1, 1, 1)

        self.label_6 = QLabel(self.tab_5)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)

        self.skiprows_qms_sb = QSpinBox(self.tab_5)
        self.skiprows_qms_sb.setObjectName(u"skiprows_qms_sb")

        self.gridLayout_6.addWidget(self.skiprows_qms_sb, 1, 1, 1, 1)

        self.label_3 = QLabel(self.tab_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 5, 0, 1, 1)

        self.plot_side_cb = QComboBox(self.tab_5)
        self.plot_side_cb.addItem("")
        self.plot_side_cb.addItem("")
        self.plot_side_cb.setObjectName(u"plot_side_cb")

        self.gridLayout_6.addWidget(self.plot_side_cb, 2, 0, 1, 1)

        self.pointsperamu_label = QLabel(self.tab_5)
        self.pointsperamu_label.setObjectName(u"pointsperamu_label")

        self.gridLayout_6.addWidget(self.pointsperamu_label, 7, 1, 1, 1)

        self.label_5 = QLabel(self.tab_5)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 7, 0, 1, 1)

        self.label_4 = QLabel(self.tab_5)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 6, 0, 1, 1)

        self.mass_start_dsb = QDoubleSpinBox(self.tab_5)
        self.mass_start_dsb.setObjectName(u"mass_start_dsb")
        self.mass_start_dsb.setMaximum(1000.000000000000000)
        self.mass_start_dsb.setValue(2.000000000000000)

        self.gridLayout_6.addWidget(self.mass_start_dsb, 5, 1, 1, 1)

        self.mass_end_dsb = QDoubleSpinBox(self.tab_5)
        self.mass_end_dsb.setObjectName(u"mass_end_dsb")
        self.mass_end_dsb.setMaximum(1000.000000000000000)
        self.mass_end_dsb.setValue(300.000000000000000)

        self.gridLayout_6.addWidget(self.mass_end_dsb, 6, 1, 1, 1)

        self.plottype_cb = QComboBox(self.tab_5)
        self.plottype_cb.addItem("")
        self.plottype_cb.addItem("")
        self.plottype_cb.setObjectName(u"plottype_cb")

        self.gridLayout_6.addWidget(self.plottype_cb, 2, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_7 = QGridLayout(self.tab_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tableWidget_2 = QTableWidget(self.tab_6)
        if (self.tableWidget_2.columnCount() < 40):
            self.tableWidget_2.setColumnCount(40)
        if (self.tableWidget_2.rowCount() < 100):
            self.tableWidget_2.setRowCount(100)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setRowCount(100)
        self.tableWidget_2.setColumnCount(40)

        self.gridLayout_7.addWidget(self.tableWidget_2, 10, 0, 1, 6)

        self.calc_iso_pb = QPushButton(self.tab_6)
        self.calc_iso_pb.setObjectName(u"calc_iso_pb")

        self.gridLayout_7.addWidget(self.calc_iso_pb, 0, 0, 1, 2)

        self.mass_offset_dsb = QDoubleSpinBox(self.tab_6)
        self.mass_offset_dsb.setObjectName(u"mass_offset_dsb")
        self.mass_offset_dsb.setDecimals(3)
        self.mass_offset_dsb.setMinimum(-99.000000000000000)
        self.mass_offset_dsb.setSingleStep(0.020000000000000)

        self.gridLayout_7.addWidget(self.mass_offset_dsb, 0, 4, 1, 1)

        self.clear_combo = QComboBox(self.tab_6)
        self.clear_combo.addItem("")
        self.clear_combo.addItem("")
        self.clear_combo.setObjectName(u"clear_combo")

        self.gridLayout_7.addWidget(self.clear_combo, 0, 2, 1, 1)

        self.label_11 = QLabel(self.tab_6)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 0, 3, 1, 1)

        self.type_iso_cb = QComboBox(self.tab_6)
        self.type_iso_cb.addItem("")
        self.type_iso_cb.addItem("")
        self.type_iso_cb.setObjectName(u"type_iso_cb")

        self.gridLayout_7.addWidget(self.type_iso_cb, 0, 5, 1, 1)

        self.scrollArea = QScrollArea(self.tab_6)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 558, 640))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.s8_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s8_alpha.setObjectName(u"s8_alpha")
        self.s8_alpha.setMaximum(1.000000000000000)
        self.s8_alpha.setSingleStep(0.100000000000000)
        self.s8_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s8_alpha, 10, 7, 1, 1)

        self.s10_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s10_alpha.setObjectName(u"s10_alpha")
        self.s10_alpha.setMaximum(1.000000000000000)
        self.s10_alpha.setSingleStep(0.100000000000000)
        self.s10_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s10_alpha, 12, 7, 1, 1)

        self.s7_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s7_alpha.setObjectName(u"s7_alpha")
        self.s7_alpha.setMaximum(1.000000000000000)
        self.s7_alpha.setSingleStep(0.100000000000000)
        self.s7_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s7_alpha, 9, 7, 1, 1)

        self.s9_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s9_alpha.setObjectName(u"s9_alpha")
        self.s9_alpha.setMaximum(1.000000000000000)
        self.s9_alpha.setSingleStep(0.100000000000000)
        self.s9_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s9_alpha, 11, 7, 1, 1)

        self.size4 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size4.setObjectName(u"size4")
        self.size4.setSingleStep(0.500000000000000)
        self.size4.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size4, 6, 6, 1, 1)

        self.species6_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species6_cb.setObjectName(u"species6_cb")

        self.gridLayout_8.addWidget(self.species6_cb, 8, 0, 1, 1)

        self.species7_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species7_cb.setObjectName(u"species7_cb")

        self.gridLayout_8.addWidget(self.species7_cb, 9, 0, 1, 1)

        self.species8_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species8_cb.setObjectName(u"species8_cb")

        self.gridLayout_8.addWidget(self.species8_cb, 10, 0, 1, 1)

        self.species9_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species9_cb.setObjectName(u"species9_cb")

        self.gridLayout_8.addWidget(self.species9_cb, 11, 0, 1, 1)

        self.species10_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species10_cb.setObjectName(u"species10_cb")

        self.gridLayout_8.addWidget(self.species10_cb, 12, 0, 1, 1)

        self.species14_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species14_cb.setObjectName(u"species14_cb")

        self.gridLayout_8.addWidget(self.species14_cb, 16, 0, 1, 1)

        self.species1_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species1_cb.setObjectName(u"species1_cb")
        self.species1_cb.setChecked(True)

        self.gridLayout_8.addWidget(self.species1_cb, 3, 0, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_8.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_8.addWidget(self.label_16, 1, 2, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_8.addWidget(self.label_10, 23, 5, 1, 1)

        self.abundance_pb = QPushButton(self.scrollAreaWidgetContents)
        self.abundance_pb.setObjectName(u"abundance_pb")

        self.gridLayout_8.addWidget(self.abundance_pb, 23, 7, 1, 1)

        self.species2_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species2_cb.setObjectName(u"species2_cb")

        self.gridLayout_8.addWidget(self.species2_cb, 4, 0, 1, 1)

        self.species3_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species3_cb.setObjectName(u"species3_cb")

        self.gridLayout_8.addWidget(self.species3_cb, 5, 0, 1, 1)

        self.round_mass = QSpinBox(self.scrollAreaWidgetContents)
        self.round_mass.setObjectName(u"round_mass")
        self.round_mass.setValue(1)

        self.gridLayout_8.addWidget(self.round_mass, 23, 6, 1, 1)

        self.name1_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name1_le.setObjectName(u"name1_le")

        self.gridLayout_8.addWidget(self.name1_le, 3, 2, 1, 1)

        self.species16_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species16_cb.setObjectName(u"species16_cb")

        self.gridLayout_8.addWidget(self.species16_cb, 18, 0, 1, 1)

        self.species15_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species15_cb.setObjectName(u"species15_cb")

        self.gridLayout_8.addWidget(self.species15_cb, 17, 0, 1, 1)

        self.species17_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species17_cb.setObjectName(u"species17_cb")

        self.gridLayout_8.addWidget(self.species17_cb, 19, 0, 1, 1)

        self.species18_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species18_cb.setObjectName(u"species18_cb")

        self.gridLayout_8.addWidget(self.species18_cb, 20, 0, 1, 1)

        self.species19_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species19_cb.setObjectName(u"species19_cb")

        self.gridLayout_8.addWidget(self.species19_cb, 21, 0, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_8.addWidget(self.label_14, 1, 4, 1, 1)

        self.species12_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species12_cb.setObjectName(u"species12_cb")

        self.gridLayout_8.addWidget(self.species12_cb, 14, 0, 1, 1)

        self.species13_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species13_cb.setObjectName(u"species13_cb")

        self.gridLayout_8.addWidget(self.species13_cb, 15, 0, 1, 1)

        self.species11_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species11_cb.setObjectName(u"species11_cb")

        self.gridLayout_8.addWidget(self.species11_cb, 13, 0, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_8.addWidget(self.label_12, 1, 5, 1, 1)

        self.s1_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s1_alpha.setObjectName(u"s1_alpha")
        self.s1_alpha.setMaximum(1.000000000000000)
        self.s1_alpha.setSingleStep(0.100000000000000)
        self.s1_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s1_alpha, 3, 7, 1, 1)

        self.s3_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s3_alpha.setObjectName(u"s3_alpha")
        self.s3_alpha.setMaximum(1.000000000000000)
        self.s3_alpha.setSingleStep(0.100000000000000)
        self.s3_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s3_alpha, 5, 7, 1, 1)

        self.size1 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size1.setObjectName(u"size1")
        self.size1.setSingleStep(0.500000000000000)
        self.size1.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size1, 3, 6, 1, 1)

        self.s2_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s2_alpha.setObjectName(u"s2_alpha")
        self.s2_alpha.setMaximum(1.000000000000000)
        self.s2_alpha.setSingleStep(0.100000000000000)
        self.s2_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s2_alpha, 4, 7, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_8.addWidget(self.label_17, 1, 7, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_8.addWidget(self.label_13, 1, 6, 1, 1)

        self.s2ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s2ratio.setObjectName(u"s2ratio")
        self.s2ratio.setDecimals(4)
        self.s2ratio.setMaximum(999999.000000000000000)
        self.s2ratio.setSingleStep(0.050000000000000)
        self.s2ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s2ratio, 4, 4, 1, 1)

        self.s3ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s3ratio.setObjectName(u"s3ratio")
        self.s3ratio.setDecimals(4)
        self.s3ratio.setMaximum(999999.000000000000000)
        self.s3ratio.setSingleStep(0.050000000000000)
        self.s3ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s3ratio, 5, 4, 1, 1)

        self.s1ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s1ratio.setObjectName(u"s1ratio")
        self.s1ratio.setDecimals(4)
        self.s1ratio.setMaximum(999999.000000000000000)
        self.s1ratio.setSingleStep(0.050000000000000)
        self.s1ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s1ratio, 3, 4, 1, 1)

        self.name2_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name2_le.setObjectName(u"name2_le")

        self.gridLayout_8.addWidget(self.name2_le, 4, 2, 1, 1)

        self.size2 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size2.setObjectName(u"size2")
        self.size2.setSingleStep(0.500000000000000)
        self.size2.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size2, 4, 6, 1, 1)

        self.color_5 = QPushButton(self.scrollAreaWidgetContents)
        self.color_5.setObjectName(u"color_5")

        self.gridLayout_8.addWidget(self.color_5, 7, 5, 1, 1)

        self.color_2 = QPushButton(self.scrollAreaWidgetContents)
        self.color_2.setObjectName(u"color_2")

        self.gridLayout_8.addWidget(self.color_2, 4, 5, 1, 1)

        self.color_4 = QPushButton(self.scrollAreaWidgetContents)
        self.color_4.setObjectName(u"color_4")

        self.gridLayout_8.addWidget(self.color_4, 6, 5, 1, 1)

        self.color_3 = QPushButton(self.scrollAreaWidgetContents)
        self.color_3.setObjectName(u"color_3")

        self.gridLayout_8.addWidget(self.color_3, 5, 5, 1, 1)

        self.color_1 = QPushButton(self.scrollAreaWidgetContents)
        self.color_1.setObjectName(u"color_1")

        self.gridLayout_8.addWidget(self.color_1, 3, 5, 1, 1)

        self.color_6 = QPushButton(self.scrollAreaWidgetContents)
        self.color_6.setObjectName(u"color_6")

        self.gridLayout_8.addWidget(self.color_6, 8, 5, 1, 1)

        self.species5_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species5_cb.setObjectName(u"species5_cb")

        self.gridLayout_8.addWidget(self.species5_cb, 7, 0, 1, 1)

        self.species4_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species4_cb.setObjectName(u"species4_cb")

        self.gridLayout_8.addWidget(self.species4_cb, 6, 0, 1, 1)

        self.s5ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s5ratio.setObjectName(u"s5ratio")
        self.s5ratio.setDecimals(4)
        self.s5ratio.setMaximum(999999.000000000000000)
        self.s5ratio.setSingleStep(0.050000000000000)
        self.s5ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s5ratio, 7, 4, 1, 1)

        self.name3_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name3_le.setObjectName(u"name3_le")

        self.gridLayout_8.addWidget(self.name3_le, 5, 2, 1, 1)

        self.s4_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s4_alpha.setObjectName(u"s4_alpha")
        self.s4_alpha.setMaximum(1.000000000000000)
        self.s4_alpha.setSingleStep(0.100000000000000)
        self.s4_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s4_alpha, 6, 7, 1, 1)

        self.size3 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size3.setObjectName(u"size3")
        self.size3.setSingleStep(0.500000000000000)
        self.size3.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size3, 5, 6, 1, 1)

        self.name5_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name5_le.setObjectName(u"name5_le")

        self.gridLayout_8.addWidget(self.name5_le, 7, 2, 1, 1)

        self.name4_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name4_le.setObjectName(u"name4_le")

        self.gridLayout_8.addWidget(self.name4_le, 6, 2, 1, 1)

        self.s4ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s4ratio.setObjectName(u"s4ratio")
        self.s4ratio.setDecimals(4)
        self.s4ratio.setMaximum(999999.000000000000000)
        self.s4ratio.setSingleStep(0.050000000000000)
        self.s4ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s4ratio, 6, 4, 1, 1)

        self.s7ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s7ratio.setObjectName(u"s7ratio")
        self.s7ratio.setDecimals(4)
        self.s7ratio.setMaximum(999999.000000000000000)
        self.s7ratio.setSingleStep(0.050000000000000)
        self.s7ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s7ratio, 9, 4, 1, 1)

        self.s6ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s6ratio.setObjectName(u"s6ratio")
        self.s6ratio.setDecimals(4)
        self.s6ratio.setMaximum(999999.000000000000000)
        self.s6ratio.setSingleStep(0.050000000000000)
        self.s6ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s6ratio, 8, 4, 1, 1)

        self.s8ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s8ratio.setObjectName(u"s8ratio")
        self.s8ratio.setDecimals(4)
        self.s8ratio.setMaximum(999999.000000000000000)
        self.s8ratio.setSingleStep(0.050000000000000)
        self.s8ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s8ratio, 10, 4, 1, 1)

        self.color_8 = QPushButton(self.scrollAreaWidgetContents)
        self.color_8.setObjectName(u"color_8")

        self.gridLayout_8.addWidget(self.color_8, 10, 5, 1, 1)

        self.s10ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s10ratio.setObjectName(u"s10ratio")
        self.s10ratio.setDecimals(4)
        self.s10ratio.setMaximum(999999.000000000000000)
        self.s10ratio.setSingleStep(0.050000000000000)
        self.s10ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s10ratio, 12, 4, 1, 1)

        self.color_9 = QPushButton(self.scrollAreaWidgetContents)
        self.color_9.setObjectName(u"color_9")

        self.gridLayout_8.addWidget(self.color_9, 11, 5, 1, 1)

        self.color_7 = QPushButton(self.scrollAreaWidgetContents)
        self.color_7.setObjectName(u"color_7")

        self.gridLayout_8.addWidget(self.color_7, 9, 5, 1, 1)

        self.s9ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s9ratio.setObjectName(u"s9ratio")
        self.s9ratio.setDecimals(4)
        self.s9ratio.setMaximum(999999.000000000000000)
        self.s9ratio.setSingleStep(0.050000000000000)
        self.s9ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s9ratio, 11, 4, 1, 1)

        self.size6 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size6.setObjectName(u"size6")
        self.size6.setSingleStep(0.500000000000000)
        self.size6.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size6, 8, 6, 1, 1)

        self.s5_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s5_alpha.setObjectName(u"s5_alpha")
        self.s5_alpha.setMaximum(1.000000000000000)
        self.s5_alpha.setSingleStep(0.100000000000000)
        self.s5_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s5_alpha, 7, 7, 1, 1)

        self.color_10 = QPushButton(self.scrollAreaWidgetContents)
        self.color_10.setObjectName(u"color_10")

        self.gridLayout_8.addWidget(self.color_10, 12, 5, 1, 1)

        self.size8 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size8.setObjectName(u"size8")
        self.size8.setSingleStep(0.500000000000000)
        self.size8.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size8, 10, 6, 1, 1)

        self.size7 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size7.setObjectName(u"size7")
        self.size7.setSingleStep(0.500000000000000)
        self.size7.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size7, 9, 6, 1, 1)

        self.size9 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size9.setObjectName(u"size9")
        self.size9.setSingleStep(0.500000000000000)
        self.size9.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size9, 11, 6, 1, 1)

        self.size5 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size5.setObjectName(u"size5")
        self.size5.setSingleStep(0.500000000000000)
        self.size5.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size5, 7, 6, 1, 1)

        self.name10_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name10_le.setObjectName(u"name10_le")

        self.gridLayout_8.addWidget(self.name10_le, 12, 2, 1, 1)

        self.s6_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s6_alpha.setObjectName(u"s6_alpha")
        self.s6_alpha.setMaximum(1.000000000000000)
        self.s6_alpha.setSingleStep(0.100000000000000)
        self.s6_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s6_alpha, 8, 7, 1, 1)

        self.name9_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name9_le.setObjectName(u"name9_le")

        self.gridLayout_8.addWidget(self.name9_le, 11, 2, 1, 1)

        self.name7_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name7_le.setObjectName(u"name7_le")

        self.gridLayout_8.addWidget(self.name7_le, 9, 2, 1, 1)

        self.name8_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name8_le.setObjectName(u"name8_le")

        self.gridLayout_8.addWidget(self.name8_le, 10, 2, 1, 1)

        self.size10 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size10.setObjectName(u"size10")
        self.size10.setSingleStep(0.500000000000000)
        self.size10.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size10, 12, 6, 1, 1)

        self.name6_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name6_le.setObjectName(u"name6_le")

        self.gridLayout_8.addWidget(self.name6_le, 8, 2, 1, 1)

        self.species20_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.species20_cb.setObjectName(u"species20_cb")

        self.gridLayout_8.addWidget(self.species20_cb, 22, 0, 1, 1)

        self.name11_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name11_le.setObjectName(u"name11_le")

        self.gridLayout_8.addWidget(self.name11_le, 13, 2, 1, 1)

        self.name12_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name12_le.setObjectName(u"name12_le")

        self.gridLayout_8.addWidget(self.name12_le, 14, 2, 1, 1)

        self.name13_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name13_le.setObjectName(u"name13_le")

        self.gridLayout_8.addWidget(self.name13_le, 15, 2, 1, 1)

        self.name14_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name14_le.setObjectName(u"name14_le")

        self.gridLayout_8.addWidget(self.name14_le, 16, 2, 1, 1)

        self.name15_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name15_le.setObjectName(u"name15_le")

        self.gridLayout_8.addWidget(self.name15_le, 17, 2, 1, 1)

        self.name16_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name16_le.setObjectName(u"name16_le")

        self.gridLayout_8.addWidget(self.name16_le, 18, 2, 1, 1)

        self.name17_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name17_le.setObjectName(u"name17_le")

        self.gridLayout_8.addWidget(self.name17_le, 19, 2, 1, 1)

        self.name18_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name18_le.setObjectName(u"name18_le")

        self.gridLayout_8.addWidget(self.name18_le, 20, 2, 1, 1)

        self.name19_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name19_le.setObjectName(u"name19_le")

        self.gridLayout_8.addWidget(self.name19_le, 21, 2, 1, 1)

        self.name20_le = QLineEdit(self.scrollAreaWidgetContents)
        self.name20_le.setObjectName(u"name20_le")

        self.gridLayout_8.addWidget(self.name20_le, 22, 2, 1, 1)

        self.s11ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s11ratio.setObjectName(u"s11ratio")
        self.s11ratio.setDecimals(4)
        self.s11ratio.setMaximum(99999.000000000000000)
        self.s11ratio.setSingleStep(0.050000000000000)
        self.s11ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s11ratio, 13, 4, 1, 1)

        self.s12ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s12ratio.setObjectName(u"s12ratio")
        self.s12ratio.setDecimals(4)
        self.s12ratio.setMaximum(99999.000000000000000)
        self.s12ratio.setSingleStep(0.050000000000000)
        self.s12ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s12ratio, 14, 4, 1, 1)

        self.s13ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s13ratio.setObjectName(u"s13ratio")
        self.s13ratio.setDecimals(4)
        self.s13ratio.setMaximum(99999.000000000000000)
        self.s13ratio.setSingleStep(0.050000000000000)
        self.s13ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s13ratio, 15, 4, 1, 1)

        self.s14ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s14ratio.setObjectName(u"s14ratio")
        self.s14ratio.setDecimals(4)
        self.s14ratio.setMaximum(99999.000000000000000)
        self.s14ratio.setSingleStep(0.050000000000000)
        self.s14ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s14ratio, 16, 4, 1, 1)

        self.s15ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s15ratio.setObjectName(u"s15ratio")
        self.s15ratio.setDecimals(4)
        self.s15ratio.setMaximum(99999.000000000000000)
        self.s15ratio.setSingleStep(0.050000000000000)
        self.s15ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s15ratio, 17, 4, 1, 1)

        self.s16ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s16ratio.setObjectName(u"s16ratio")
        self.s16ratio.setDecimals(4)
        self.s16ratio.setMaximum(99999.000000000000000)
        self.s16ratio.setSingleStep(0.050000000000000)
        self.s16ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s16ratio, 18, 4, 1, 1)

        self.s17ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s17ratio.setObjectName(u"s17ratio")
        self.s17ratio.setDecimals(4)
        self.s17ratio.setMaximum(99999.000000000000000)
        self.s17ratio.setSingleStep(0.050000000000000)
        self.s17ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s17ratio, 19, 4, 1, 1)

        self.s18ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s18ratio.setObjectName(u"s18ratio")
        self.s18ratio.setDecimals(4)
        self.s18ratio.setMaximum(99999.000000000000000)
        self.s18ratio.setSingleStep(0.050000000000000)
        self.s18ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s18ratio, 20, 4, 1, 1)

        self.s19ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s19ratio.setObjectName(u"s19ratio")
        self.s19ratio.setDecimals(4)
        self.s19ratio.setMaximum(99999.000000000000000)
        self.s19ratio.setSingleStep(0.050000000000000)
        self.s19ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s19ratio, 21, 4, 1, 1)

        self.s20ratio = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s20ratio.setObjectName(u"s20ratio")
        self.s20ratio.setDecimals(4)
        self.s20ratio.setMaximum(99999.000000000000000)
        self.s20ratio.setSingleStep(0.050000000000000)
        self.s20ratio.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s20ratio, 22, 4, 1, 1)

        self.color_11 = QPushButton(self.scrollAreaWidgetContents)
        self.color_11.setObjectName(u"color_11")

        self.gridLayout_8.addWidget(self.color_11, 13, 5, 1, 1)

        self.color_12 = QPushButton(self.scrollAreaWidgetContents)
        self.color_12.setObjectName(u"color_12")

        self.gridLayout_8.addWidget(self.color_12, 14, 5, 1, 1)

        self.color_13 = QPushButton(self.scrollAreaWidgetContents)
        self.color_13.setObjectName(u"color_13")

        self.gridLayout_8.addWidget(self.color_13, 15, 5, 1, 1)

        self.color_14 = QPushButton(self.scrollAreaWidgetContents)
        self.color_14.setObjectName(u"color_14")

        self.gridLayout_8.addWidget(self.color_14, 16, 5, 1, 1)

        self.color_15 = QPushButton(self.scrollAreaWidgetContents)
        self.color_15.setObjectName(u"color_15")

        self.gridLayout_8.addWidget(self.color_15, 17, 5, 1, 1)

        self.color_16 = QPushButton(self.scrollAreaWidgetContents)
        self.color_16.setObjectName(u"color_16")

        self.gridLayout_8.addWidget(self.color_16, 18, 5, 1, 1)

        self.color_17 = QPushButton(self.scrollAreaWidgetContents)
        self.color_17.setObjectName(u"color_17")

        self.gridLayout_8.addWidget(self.color_17, 19, 5, 1, 1)

        self.color_18 = QPushButton(self.scrollAreaWidgetContents)
        self.color_18.setObjectName(u"color_18")

        self.gridLayout_8.addWidget(self.color_18, 20, 5, 1, 1)

        self.color_19 = QPushButton(self.scrollAreaWidgetContents)
        self.color_19.setObjectName(u"color_19")

        self.gridLayout_8.addWidget(self.color_19, 21, 5, 1, 1)

        self.color_20 = QPushButton(self.scrollAreaWidgetContents)
        self.color_20.setObjectName(u"color_20")

        self.gridLayout_8.addWidget(self.color_20, 22, 5, 1, 1)

        self.size11 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size11.setObjectName(u"size11")
        self.size11.setMaximum(99.000000000000000)
        self.size11.setSingleStep(0.100000000000000)
        self.size11.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size11, 13, 6, 1, 1)

        self.size12 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size12.setObjectName(u"size12")
        self.size12.setMaximum(99.000000000000000)
        self.size12.setSingleStep(0.100000000000000)
        self.size12.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size12, 14, 6, 1, 1)

        self.size13 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size13.setObjectName(u"size13")
        self.size13.setMaximum(99.000000000000000)
        self.size13.setSingleStep(0.100000000000000)
        self.size13.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size13, 15, 6, 1, 1)

        self.size14 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size14.setObjectName(u"size14")
        self.size14.setMaximum(99.000000000000000)
        self.size14.setSingleStep(0.100000000000000)
        self.size14.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size14, 16, 6, 1, 1)

        self.size15 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size15.setObjectName(u"size15")
        self.size15.setMaximum(99.000000000000000)
        self.size15.setSingleStep(0.100000000000000)
        self.size15.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size15, 17, 6, 1, 1)

        self.size16 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size16.setObjectName(u"size16")
        self.size16.setMaximum(99.000000000000000)
        self.size16.setSingleStep(0.100000000000000)
        self.size16.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size16, 18, 6, 1, 1)

        self.size17 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size17.setObjectName(u"size17")
        self.size17.setMaximum(99.000000000000000)
        self.size17.setSingleStep(0.100000000000000)
        self.size17.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size17, 19, 6, 1, 1)

        self.size18 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size18.setObjectName(u"size18")
        self.size18.setMaximum(99.000000000000000)
        self.size18.setSingleStep(0.100000000000000)
        self.size18.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size18, 20, 6, 1, 1)

        self.size19 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size19.setObjectName(u"size19")
        self.size19.setMaximum(99.000000000000000)
        self.size19.setSingleStep(0.100000000000000)
        self.size19.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size19, 21, 6, 1, 1)

        self.size20 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.size20.setObjectName(u"size20")
        self.size20.setMaximum(99.000000000000000)
        self.size20.setSingleStep(0.100000000000000)
        self.size20.setValue(5.000000000000000)

        self.gridLayout_8.addWidget(self.size20, 22, 6, 1, 1)

        self.s11_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s11_alpha.setObjectName(u"s11_alpha")
        self.s11_alpha.setMaximum(1.000000000000000)
        self.s11_alpha.setSingleStep(0.100000000000000)
        self.s11_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s11_alpha, 13, 7, 1, 1)

        self.s12_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s12_alpha.setObjectName(u"s12_alpha")
        self.s12_alpha.setMaximum(1.000000000000000)
        self.s12_alpha.setSingleStep(0.100000000000000)
        self.s12_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s12_alpha, 14, 7, 1, 1)

        self.s13_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s13_alpha.setObjectName(u"s13_alpha")
        self.s13_alpha.setMaximum(1.000000000000000)
        self.s13_alpha.setSingleStep(0.100000000000000)
        self.s13_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s13_alpha, 15, 7, 1, 1)

        self.s14_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s14_alpha.setObjectName(u"s14_alpha")
        self.s14_alpha.setMaximum(1.000000000000000)
        self.s14_alpha.setSingleStep(0.100000000000000)
        self.s14_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s14_alpha, 16, 7, 1, 1)

        self.s15_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s15_alpha.setObjectName(u"s15_alpha")
        self.s15_alpha.setMaximum(1.000000000000000)
        self.s15_alpha.setSingleStep(0.100000000000000)
        self.s15_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s15_alpha, 17, 7, 1, 1)

        self.s16_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s16_alpha.setObjectName(u"s16_alpha")
        self.s16_alpha.setMaximum(1.000000000000000)
        self.s16_alpha.setSingleStep(0.100000000000000)
        self.s16_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s16_alpha, 18, 7, 1, 1)

        self.s17_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s17_alpha.setObjectName(u"s17_alpha")
        self.s17_alpha.setMaximum(1.000000000000000)
        self.s17_alpha.setSingleStep(0.100000000000000)
        self.s17_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s17_alpha, 19, 7, 1, 1)

        self.s18_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s18_alpha.setObjectName(u"s18_alpha")
        self.s18_alpha.setMaximum(1.000000000000000)
        self.s18_alpha.setSingleStep(0.100000000000000)
        self.s18_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s18_alpha, 20, 7, 1, 1)

        self.s19_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s19_alpha.setObjectName(u"s19_alpha")
        self.s19_alpha.setMaximum(1.000000000000000)
        self.s19_alpha.setSingleStep(0.100000000000000)
        self.s19_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s19_alpha, 21, 7, 1, 1)

        self.s20_alpha = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.s20_alpha.setObjectName(u"s20_alpha")
        self.s20_alpha.setMaximum(1.000000000000000)
        self.s20_alpha.setSingleStep(0.100000000000000)
        self.s20_alpha.setValue(1.000000000000000)

        self.gridLayout_8.addWidget(self.s20_alpha, 22, 7, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_7.addWidget(self.scrollArea, 2, 0, 1, 6)

        self.tabWidget_2.addTab(self.tab_6, "")

        self.gridLayout_2.addWidget(self.tabWidget_2, 1, 0, 1, 3)

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

        self.gridLayout.addWidget(self.tabWidget, 3, 2, 1, 1)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"SE/QMS", None))
        ___qtreewidgetitem = self.tw_x.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("DockWidget", u"X-Axis", None));
        self.label_7.setText(QCoreApplication.translate("DockWidget", u"Skip Rows: ", None))
        ___qtreewidgetitem1 = self.tw_y.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("DockWidget", u"Y-Axis", None));
        self.fill_cols_pb.setText(QCoreApplication.translate("DockWidget", u"Fill Columns", None))
        self.ax_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Left Ax", None))
        self.ax_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Right Ax", None))

        self.plot_type_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Ext. Plot (half-ints)", None))
        self.plot_type_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Ext. Plot (ints)", None))
        self.plot_type_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"X vs Y", None))
        self.plot_type_cb.setItemText(3, QCoreApplication.translate("DockWidget", u"Ext. Plot (third-ints)", None))

        self.plot_pb.setText(QCoreApplication.translate("DockWidget", u"Plot", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QCoreApplication.translate("DockWidget", u"Add Line to Plot", None))
        self.ylabel_le.setText("")
        self.xlabel_le.setText("")
        self.secolorpb.setText("")
        self.label_9.setText(QCoreApplication.translate("DockWidget", u"Y Label", None))
        self.label_8.setText(QCoreApplication.translate("DockWidget", u"X Label", None))
        self.error_checkbox.setText(QCoreApplication.translate("DockWidget", u"Use Error", None))
        self.label_18.setText(QCoreApplication.translate("DockWidget", u"Marker Size", None))
        self.zero_correct_checkb.setText(QCoreApplication.translate("DockWidget", u"Zero Correct", None))
        ___qtreewidgetitem2 = self.error_tw.headerItem()
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("DockWidget", u"Error", None));
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QCoreApplication.translate("DockWidget", u"Plot Attributes", None))
        self.linfitall_pb.setText(QCoreApplication.translate("DockWidget", u"Lin. Fit. All", None))
        self.lin_fit_pb.setText(QCoreApplication.translate("DockWidget", u"Lin. Fit", None))
        self.selectrange_box.setText(QCoreApplication.translate("DockWidget", u"Select Fitting Range", None))
        self.label_20.setText(QCoreApplication.translate("DockWidget", u"Negative Thickness Change Average", None))
        self.label_21.setText(QCoreApplication.translate("DockWidget", u"A Thick Change", None))
        self.label_22.setText(QCoreApplication.translate("DockWidget", u"B Thick Change", None))
        self.label_19.setText(QCoreApplication.translate("DockWidget", u"Positive Thickness Change Average", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), QCoreApplication.translate("DockWidget", u"Linear Fit", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), QCoreApplication.translate("DockWidget", u"Error Plotting", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("DockWidget", u"Axis Properties", None))
        self.fill_cols_qms_pb.setText(QCoreApplication.translate("DockWidget", u"Fill Columns", None))
        self.plot_qms_pb.setText(QCoreApplication.translate("DockWidget", u"Plot", None))
        ___qtreewidgetitem3 = self.qmsx_tw.headerItem()
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("DockWidget", u"QMS_X", None));
        ___qtreewidgetitem4 = self.qmsy_tw.headerItem()
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("DockWidget", u"QMS Y", None));
        self.label_6.setText(QCoreApplication.translate("DockWidget", u"Skip Rows", None))
        self.label_3.setText(QCoreApplication.translate("DockWidget", u"Starting Mass", None))
        self.plot_side_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Left", None))
        self.plot_side_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Right", None))

        self.pointsperamu_label.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label_5.setText(QCoreApplication.translate("DockWidget", u"Points per amu", None))
        self.label_4.setText(QCoreApplication.translate("DockWidget", u"Ending Mass", None))
        self.plottype_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"X vs Y", None))
        self.plottype_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Mass Spectrum", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("DockWidget", u"Plot QMS", None))
        self.calc_iso_pb.setText(QCoreApplication.translate("DockWidget", u"Calculate isotopic abundance", None))
        self.clear_combo.setItemText(0, QCoreApplication.translate("DockWidget", u"Clear Lines On", None))
        self.clear_combo.setItemText(1, QCoreApplication.translate("DockWidget", u"Clear Lines Off", None))

        self.label_11.setText(QCoreApplication.translate("DockWidget", u"Mass Offset", None))
        self.type_iso_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Map 100%", None))
        self.type_iso_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"User Defined", None))

        self.species6_cb.setText(QCoreApplication.translate("DockWidget", u"Species 6", None))
        self.species7_cb.setText(QCoreApplication.translate("DockWidget", u"Species 7", None))
        self.species8_cb.setText(QCoreApplication.translate("DockWidget", u"Species 8", None))
        self.species9_cb.setText(QCoreApplication.translate("DockWidget", u"Species 9", None))
        self.species10_cb.setText(QCoreApplication.translate("DockWidget", u"Species 10", None))
        self.species14_cb.setText(QCoreApplication.translate("DockWidget", u"Species 14", None))
        self.species1_cb.setText(QCoreApplication.translate("DockWidget", u"Species 1", None))
        self.label_15.setText(QCoreApplication.translate("DockWidget", u"Turn On/Off", None))
        self.label_16.setText(QCoreApplication.translate("DockWidget", u"Molecule", None))
        self.label_10.setText(QCoreApplication.translate("DockWidget", u"Round Mass", None))
        self.abundance_pb.setText(QCoreApplication.translate("DockWidget", u"Abundance Plot", None))
        self.species2_cb.setText(QCoreApplication.translate("DockWidget", u"Species 2", None))
        self.species3_cb.setText(QCoreApplication.translate("DockWidget", u"Species 3", None))
        self.name1_le.setText(QCoreApplication.translate("DockWidget", u"B1F2", None))
        self.species16_cb.setText(QCoreApplication.translate("DockWidget", u"Species 16", None))
        self.species15_cb.setText(QCoreApplication.translate("DockWidget", u"Species 15", None))
        self.species17_cb.setText(QCoreApplication.translate("DockWidget", u"Species 17", None))
        self.species18_cb.setText(QCoreApplication.translate("DockWidget", u"Species 18", None))
        self.species19_cb.setText(QCoreApplication.translate("DockWidget", u"Species 19", None))
        self.label_14.setText(QCoreApplication.translate("DockWidget", u"User Defined Ratio", None))
        self.species12_cb.setText(QCoreApplication.translate("DockWidget", u"Species 12", None))
        self.species13_cb.setText(QCoreApplication.translate("DockWidget", u"Species 13", None))
        self.species11_cb.setText(QCoreApplication.translate("DockWidget", u"Species 11", None))
        self.label_12.setText(QCoreApplication.translate("DockWidget", u"Color", None))
        self.label_17.setText(QCoreApplication.translate("DockWidget", u"Alpha", None))
        self.label_13.setText(QCoreApplication.translate("DockWidget", u"Size", None))
        self.name2_le.setText(QCoreApplication.translate("DockWidget", u"B1F1O1H1", None))
        self.color_5.setText("")
        self.color_2.setText("")
        self.color_4.setText("")
        self.color_3.setText("")
        self.color_1.setText("")
        self.color_6.setText("")
        self.species5_cb.setText(QCoreApplication.translate("DockWidget", u"Species 5", None))
        self.species4_cb.setText(QCoreApplication.translate("DockWidget", u"Species 4", None))
        self.name3_le.setText(QCoreApplication.translate("DockWidget", u"B1O2H2", None))
        self.color_8.setText("")
        self.color_9.setText("")
        self.color_7.setText("")
        self.color_10.setText("")
        self.species20_cb.setText(QCoreApplication.translate("DockWidget", u"Species 20", None))
        self.color_11.setText("")
        self.color_12.setText("")
        self.color_13.setText("")
        self.color_14.setText("")
        self.color_15.setText("")
        self.color_16.setText("")
        self.color_17.setText("")
        self.color_18.setText("")
        self.color_19.setText("")
        self.color_20.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("DockWidget", u"Isotopic Prediction", None))
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

