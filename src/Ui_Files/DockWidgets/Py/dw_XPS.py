# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_XPS.ui'
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
        DockWidget.resize(594, 511)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_7 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tabWidget = QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.plot_pb = QPushButton(self.tab)
        self.plot_pb.setObjectName(u"plot_pb")

        self.gridLayout.addWidget(self.plot_pb, 3, 2, 1, 1)

        self.tw_y = QTreeWidget(self.tab)
        self.tw_y.setObjectName(u"tw_y")

        self.gridLayout.addWidget(self.tw_y, 1, 2, 1, 1)

        self.fill_cols_pb = QPushButton(self.tab)
        self.fill_cols_pb.setObjectName(u"fill_cols_pb")

        self.gridLayout.addWidget(self.fill_cols_pb, 2, 2, 1, 1)

        self.XPS_treeView = QTreeView(self.tab)
        self.XPS_treeView.setObjectName(u"XPS_treeView")
        self.XPS_treeView.setMaximumSize(QSize(1000, 16777215))

        self.gridLayout.addWidget(self.XPS_treeView, 0, 0, 1, 3)

        self.tw_x = QTreeWidget(self.tab)
        self.tw_x.setObjectName(u"tw_x")

        self.gridLayout.addWidget(self.tw_x, 1, 0, 1, 2)

        self.skip_rows_sb = QSpinBox(self.tab)
        self.skip_rows_sb.setObjectName(u"skip_rows_sb")
        self.skip_rows_sb.setValue(1)

        self.gridLayout.addWidget(self.skip_rows_sb, 3, 0, 1, 2)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_8 = QGridLayout(self.tab_13)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label = QLabel(self.tab_13)
        self.label.setObjectName(u"label")

        self.gridLayout_8.addWidget(self.label, 3, 3, 1, 1)

        self.fit_pb = QPushButton(self.tab_13)
        self.fit_pb.setObjectName(u"fit_pb")
        self.fit_pb.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_8.addWidget(self.fit_pb, 7, 4, 1, 1)

        self.num_peaks_sb = QSpinBox(self.tab_13)
        self.num_peaks_sb.setObjectName(u"num_peaks_sb")
        self.num_peaks_sb.setMaximumSize(QSize(80, 16777215))
        self.num_peaks_sb.setMinimum(1)

        self.gridLayout_8.addWidget(self.num_peaks_sb, 3, 1, 1, 1)

        self.fit_report_TE = QTextEdit(self.tab_13)
        self.fit_report_TE.setObjectName(u"fit_report_TE")

        self.gridLayout_8.addWidget(self.fit_report_TE, 6, 0, 1, 5)

        self.fit_shape_cb = QComboBox(self.tab_13)
        self.fit_shape_cb.addItem("")
        self.fit_shape_cb.addItem("")
        self.fit_shape_cb.addItem("")
        self.fit_shape_cb.setObjectName(u"fit_shape_cb")

        self.gridLayout_8.addWidget(self.fit_shape_cb, 3, 2, 1, 1)

        self.label_44 = QLabel(self.tab_13)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.label_44, 3, 0, 1, 1)

        self.tableWidget = QTableWidget(self.tab_13)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
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
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)

        self.gridLayout_8.addWidget(self.tableWidget, 5, 0, 1, 5)

        self.plot_curr_pb = QPushButton(self.tab_13)
        self.plot_curr_pb.setObjectName(u"plot_curr_pb")
        self.plot_curr_pb.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_8.addWidget(self.plot_curr_pb, 7, 0, 1, 2)

        self.shirley_pb = QPushButton(self.tab_13)
        self.shirley_pb.setObjectName(u"shirley_pb")
        self.shirley_pb.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_8.addWidget(self.shirley_pb, 7, 2, 1, 2)

        self.correctc1s_dsb = QDoubleSpinBox(self.tab_13)
        self.correctc1s_dsb.setObjectName(u"correctc1s_dsb")
        self.correctc1s_dsb.setDecimals(1)
        self.correctc1s_dsb.setMaximum(1000.000000000000000)
        self.correctc1s_dsb.setValue(284.800000000000011)

        self.gridLayout_8.addWidget(self.correctc1s_dsb, 3, 4, 1, 1)

        self.tabWidget.addTab(self.tab_13, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.fit_pb_2 = QPushButton(self.tab_2)
        self.fit_pb_2.setObjectName(u"fit_pb_2")

        self.gridLayout_2.addWidget(self.fit_pb_2, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 556, 777))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.sigma4_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sigma4_sb.setObjectName(u"sigma4_sb")
        self.sigma4_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.sigma4_sb, 17, 4, 1, 1)

        self.amp3l_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.amp3l_sb.setObjectName(u"amp3l_sb")
        self.amp3l_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.amp3l_sb, 10, 3, 1, 1)

        self.amp4h_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.amp4h_sb.setObjectName(u"amp4h_sb")
        self.amp4h_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.amp4h_sb, 9, 4, 1, 1)

        self.amp3h_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.amp3h_sb.setObjectName(u"amp3h_sb")
        self.amp3h_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.amp3h_sb, 9, 3, 1, 1)

        self.xpsrange_rb = QRadioButton(self.scrollAreaWidgetContents)
        self.xpsrange_rb.setObjectName(u"xpsrange_rb")

        self.gridLayout_4.addWidget(self.xpsrange_rb, 1, 0, 1, 1)

        self.amp2l_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.amp2l_sb.setObjectName(u"amp2l_sb")
        self.amp2l_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.amp2l_sb, 10, 2, 1, 1)

        self.cen4_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cen4_sb.setObjectName(u"cen4_sb")
        self.cen4_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.cen4_sb, 12, 4, 1, 1)

        self.sigma4l_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sigma4l_sb.setObjectName(u"sigma4l_sb")
        self.sigma4l_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.sigma4l_sb, 20, 4, 1, 1)

        self.peak3_box = QCheckBox(self.scrollAreaWidgetContents)
        self.peak3_box.setObjectName(u"peak3_box")

        self.gridLayout_4.addWidget(self.peak3_box, 4, 3, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 4, 0, 1, 1)

        self.peak5_box = QCheckBox(self.scrollAreaWidgetContents)
        self.peak5_box.setObjectName(u"peak5_box")

        self.gridLayout_4.addWidget(self.peak5_box, 4, 5, 1, 1)

        self.peak1_box = QCheckBox(self.scrollAreaWidgetContents)
        self.peak1_box.setObjectName(u"peak1_box")
        self.peak1_box.setChecked(True)

        self.gridLayout_4.addWidget(self.peak1_box, 4, 1, 1, 1)

        self.peak2_box = QCheckBox(self.scrollAreaWidgetContents)
        self.peak2_box.setObjectName(u"peak2_box")

        self.gridLayout_4.addWidget(self.peak2_box, 4, 2, 1, 1)

        self.peak4_box = QCheckBox(self.scrollAreaWidgetContents)
        self.peak4_box.setObjectName(u"peak4_box")

        self.gridLayout_4.addWidget(self.peak4_box, 4, 4, 1, 1)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 15, 0, 1, 6)

        self.amp1_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.amp1_sb.setObjectName(u"amp1_sb")
        self.amp1_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.amp1_sb, 8, 1, 1, 1)

        self.amp2h_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.amp2h_sb.setObjectName(u"amp2h_sb")
        self.amp2h_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.amp2h_sb, 9, 2, 1, 1)

        self.cen2l_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cen2l_sb.setObjectName(u"cen2l_sb")
        self.cen2l_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.cen2l_sb, 14, 2, 1, 1)

        self.sigma2_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sigma2_sb.setObjectName(u"sigma2_sb")
        self.sigma2_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.sigma2_sb, 17, 2, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 1, 1, 1, 1)

        self.correctc1s_dsb_2 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.correctc1s_dsb_2.setObjectName(u"correctc1s_dsb_2")
        self.correctc1s_dsb_2.setMaximum(1000.000000000000000)
        self.correctc1s_dsb_2.setValue(284.800000000000011)

        self.gridLayout_4.addWidget(self.correctc1s_dsb_2, 1, 2, 1, 1)

        self.sigma1_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sigma1_sb.setObjectName(u"sigma1_sb")
        self.sigma1_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.sigma1_sb, 17, 1, 1, 1)

        self.amp1h_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.amp1h_sb.setObjectName(u"amp1h_sb")
        self.amp1h_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.amp1h_sb, 9, 1, 1, 1)

        self.sigma2l_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sigma2l_sb.setObjectName(u"sigma2l_sb")
        self.sigma2l_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.sigma2l_sb, 20, 2, 1, 1)

        self.cen3l_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cen3l_sb.setObjectName(u"cen3l_sb")
        self.cen3l_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.cen3l_sb, 14, 3, 1, 1)

        self.amp1l_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.amp1l_sb.setObjectName(u"amp1l_sb")
        self.amp1l_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.amp1l_sb, 10, 1, 1, 1)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 7, 0, 1, 6)

        self.sigma3_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sigma3_sb.setObjectName(u"sigma3_sb")
        self.sigma3_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.sigma3_sb, 17, 3, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 17, 0, 1, 1)

        self.cen1_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cen1_sb.setObjectName(u"cen1_sb")
        self.cen1_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.cen1_sb, 12, 1, 1, 1)

        self.amp4l_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.amp4l_sb.setObjectName(u"amp4l_sb")
        self.amp4l_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.amp4l_sb, 10, 4, 1, 1)

        self.sigma2h_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sigma2h_sb.setObjectName(u"sigma2h_sb")
        self.sigma2h_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.sigma2h_sb, 19, 2, 1, 1)

        self.cen1h_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cen1h_sb.setObjectName(u"cen1h_sb")
        self.cen1h_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.cen1h_sb, 13, 1, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 20, 0, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 19, 0, 1, 1)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 11, 0, 1, 6)

        self.sigma3l_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sigma3l_sb.setObjectName(u"sigma3l_sb")
        self.sigma3l_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.sigma3l_sb, 20, 3, 1, 1)

        self.fitreport_te = QTextEdit(self.scrollAreaWidgetContents)
        self.fitreport_te.setObjectName(u"fitreport_te")
        self.fitreport_te.setMinimumSize(QSize(0, 400))

        self.gridLayout_4.addWidget(self.fitreport_te, 22, 0, 1, 6)

        self.sigma3h_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sigma3h_sb.setObjectName(u"sigma3h_sb")
        self.sigma3h_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.sigma3h_sb, 19, 3, 1, 1)

        self.plot_what_box = QCheckBox(self.scrollAreaWidgetContents)
        self.plot_what_box.setObjectName(u"plot_what_box")
        self.plot_what_box.setChecked(True)

        self.gridLayout_4.addWidget(self.plot_what_box, 21, 1, 1, 1)

        self.sigma1l_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sigma1l_sb.setObjectName(u"sigma1l_sb")
        self.sigma1l_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.sigma1l_sb, 20, 1, 1, 1)

        self.sigma1h_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sigma1h_sb.setObjectName(u"sigma1h_sb")
        self.sigma1h_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.sigma1h_sb, 19, 1, 1, 1)

        self.comboBox_5 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_4.addWidget(self.comboBox_5, 6, 5, 1, 1)

        self.comboBox_4 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_4.addWidget(self.comboBox_4, 6, 4, 1, 1)

        self.comboBox_2 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_4.addWidget(self.comboBox_2, 6, 2, 1, 1)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_4.addWidget(self.comboBox, 6, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_4.addWidget(self.comboBox_3, 6, 3, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 10, 0, 1, 1)

        self.amp2_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.amp2_sb.setObjectName(u"amp2_sb")
        self.amp2_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.amp2_sb, 8, 2, 1, 1)

        self.cen2h_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cen2h_sb.setObjectName(u"cen2h_sb")
        self.cen2h_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.cen2h_sb, 13, 2, 1, 1)

        self.amp3_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.amp3_sb.setObjectName(u"amp3_sb")
        self.amp3_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.amp3_sb, 8, 3, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 8, 0, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 13, 0, 1, 1)

        self.amp4_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.amp4_sb.setObjectName(u"amp4_sb")
        self.amp4_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.amp4_sb, 8, 4, 1, 1)

        self.amp5_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.amp5_sb.setObjectName(u"amp5_sb")
        self.amp5_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.amp5_sb, 8, 5, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 12, 0, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 9, 0, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 14, 0, 1, 1)

        self.cen3_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cen3_sb.setObjectName(u"cen3_sb")
        self.cen3_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.cen3_sb, 12, 3, 1, 1)

        self.cen2_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cen2_sb.setObjectName(u"cen2_sb")
        self.cen2_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.cen2_sb, 12, 2, 1, 1)

        self.cen3h_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cen3h_sb.setObjectName(u"cen3h_sb")
        self.cen3h_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.cen3h_sb, 13, 3, 1, 1)

        self.sigma4h_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sigma4h_sb.setObjectName(u"sigma4h_sb")
        self.sigma4h_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.sigma4h_sb, 19, 4, 1, 1)

        self.cen1l_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cen1l_sb.setObjectName(u"cen1l_sb")
        self.cen1l_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.cen1l_sb, 14, 1, 1, 1)

        self.fit_range_cb = QComboBox(self.scrollAreaWidgetContents)
        self.fit_range_cb.setObjectName(u"fit_range_cb")

        self.gridLayout_4.addWidget(self.fit_range_cb, 1, 3, 1, 2)

        self.cen5h_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cen5h_sb.setObjectName(u"cen5h_sb")
        self.cen5h_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.cen5h_sb, 13, 5, 1, 1)

        self.amp5l_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.amp5l_sb.setObjectName(u"amp5l_sb")
        self.amp5l_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.amp5l_sb, 10, 5, 1, 1)

        self.amp5h_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.amp5h_sb.setObjectName(u"amp5h_sb")
        self.amp5h_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.amp5h_sb, 9, 5, 1, 1)

        self.cen5l_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cen5l_sb.setObjectName(u"cen5l_sb")
        self.cen5l_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.cen5l_sb, 14, 5, 1, 1)

        self.cen4l_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cen4l_sb.setObjectName(u"cen4l_sb")
        self.cen4l_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.cen4l_sb, 14, 4, 1, 1)

        self.sigma5_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sigma5_sb.setObjectName(u"sigma5_sb")
        self.sigma5_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.sigma5_sb, 17, 5, 1, 1)

        self.cen5_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cen5_sb.setObjectName(u"cen5_sb")
        self.cen5_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.cen5_sb, 12, 5, 1, 1)

        self.cen4h_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cen4h_sb.setObjectName(u"cen4h_sb")
        self.cen4h_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.cen4h_sb, 13, 4, 1, 1)

        self.sigma5h_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sigma5h_sb.setObjectName(u"sigma5h_sb")
        self.sigma5h_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.sigma5h_sb, 19, 5, 1, 1)

        self.sigma5l_sb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sigma5l_sb.setObjectName(u"sigma5l_sb")
        self.sigma5l_sb.setMaximum(999999.000000000000000)

        self.gridLayout_4.addWidget(self.sigma5l_sb, 20, 5, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 6)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.gridLayout_10 = QGridLayout(self.tab_14)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.graphicsView = QGraphicsView(self.tab_14)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_10.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.pushButton = QPushButton(self.tab_14)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_10.addWidget(self.pushButton, 2, 1, 1, 1)

        self.tableWidget_2 = QTableWidget(self.tab_14)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        if (self.tableWidget_2.rowCount() < 4):
            self.tableWidget_2.setRowCount(4)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 3, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 4, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 4, __qtablewidgetitem43)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMaximumSize(QSize(16777215, 145))

        self.gridLayout_10.addWidget(self.tableWidget_2, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_14, "")

        self.gridLayout_7.addWidget(self.tabWidget, 0, 1, 1, 1)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"XPS", None))
        self.plot_pb.setText(QCoreApplication.translate("DockWidget", u"Plot", None))
        ___qtreewidgetitem = self.tw_y.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("DockWidget", u"Counts", None));
        self.fill_cols_pb.setText(QCoreApplication.translate("DockWidget", u"Fill Columns", None))
        ___qtreewidgetitem1 = self.tw_x.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("DockWidget", u"B.E. (e.V.)", None));
        self.label_2.setText(QCoreApplication.translate("DockWidget", u"skip rows", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("DockWidget", u"XPS Plotting", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"Correct C1s to ", None))
        self.fit_pb.setText(QCoreApplication.translate("DockWidget", u"Fit", None))
        self.fit_shape_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Voigt", None))
        self.fit_shape_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Gaussian", None))
        self.fit_shape_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"Lorentz", None))

        self.label_44.setText(QCoreApplication.translate("DockWidget", u"Num of Peaks", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DockWidget", u"Peak 1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DockWidget", u"Peak 2", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DockWidget", u"Peak 3", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DockWidget", u"Peak 4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DockWidget", u"Peak 5", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DockWidget", u"Amp", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DockWidget", u"Amp Low", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DockWidget", u"Amp High", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DockWidget", u"Cen", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DockWidget", u"Cen Low", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("DockWidget", u"Cen High", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("DockWidget", u"Sigma", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("DockWidget", u"Sigma Low", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("DockWidget", u"Sigma High", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("DockWidget", u"Type", None));
        self.plot_curr_pb.setText(QCoreApplication.translate("DockWidget", u"Plot Curr", None))
        self.shirley_pb.setText(QCoreApplication.translate("DockWidget", u"Shirley", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("DockWidget", u"Fitting", None))
        self.fit_pb_2.setText(QCoreApplication.translate("DockWidget", u"Fit", None))
        self.pushButton_2.setText(QCoreApplication.translate("DockWidget", u"Plot Current", None))
        self.xpsrange_rb.setText(QCoreApplication.translate("DockWidget", u"Select Sections", None))
        self.peak3_box.setText(QCoreApplication.translate("DockWidget", u"Peak3", None))
        self.label_12.setText(QCoreApplication.translate("DockWidget", u"Peak #", None))
        self.peak5_box.setText(QCoreApplication.translate("DockWidget", u"Peak5", None))
        self.peak1_box.setText(QCoreApplication.translate("DockWidget", u"Peak1", None))
        self.peak2_box.setText(QCoreApplication.translate("DockWidget", u"Peak2", None))
        self.peak4_box.setText(QCoreApplication.translate("DockWidget", u"Peak4", None))
        self.label_13.setText(QCoreApplication.translate("DockWidget", u"C1s", None))
        self.label_9.setText(QCoreApplication.translate("DockWidget", u"Sigma", None))
        self.label_11.setText(QCoreApplication.translate("DockWidget", u"Low", None))
        self.label_10.setText(QCoreApplication.translate("DockWidget", u"High", None))
        self.plot_what_box.setText(QCoreApplication.translate("DockWidget", u"Plot Only Best Fit", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("DockWidget", u"Voigt", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("DockWidget", u"Gaussian", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("DockWidget", u"Lorentz", None))

        self.comboBox_4.setItemText(0, QCoreApplication.translate("DockWidget", u"Voigt", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("DockWidget", u"Gaussian", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("DockWidget", u"Lorentz", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("DockWidget", u"Voigt", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("DockWidget", u"Gaussian", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("DockWidget", u"Lorentz", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("DockWidget", u"Voigt", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("DockWidget", u"Gaussian", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("DockWidget", u"Lorentz", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("DockWidget", u"Voigt", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("DockWidget", u"Gaussian", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("DockWidget", u"Lorentz", None))

        self.label_5.setText(QCoreApplication.translate("DockWidget", u"Low", None))
        self.label_3.setText(QCoreApplication.translate("DockWidget", u"Amp", None))
        self.label_7.setText(QCoreApplication.translate("DockWidget", u"High", None))
        self.label_6.setText(QCoreApplication.translate("DockWidget", u"Cen", None))
        self.label_4.setText(QCoreApplication.translate("DockWidget", u"High", None))
        self.label_8.setText(QCoreApplication.translate("DockWidget", u"Low", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("DockWidget", u"Better Fitting", None))
        self.pushButton.setText(QCoreApplication.translate("DockWidget", u"Go", None))
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("DockWidget", u"Intenisty", None));
        ___qtablewidgetitem16 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("DockWidget", u"IMFP", None));
        ___qtablewidgetitem17 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("DockWidget", u"R.S.F.", None));
        ___qtablewidgetitem18 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("DockWidget", u"# Density", None));
        ___qtablewidgetitem19 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("DockWidget", u"K.E.", None));
        ___qtablewidgetitem20 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("DockWidget", u"Layer 1", None));
        ___qtablewidgetitem21 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("DockWidget", u"Layer 2", None));
        ___qtablewidgetitem22 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("DockWidget", u"Layer 3", None));
        ___qtablewidgetitem23 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("DockWidget", u"Substrate", None));

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem24 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("DockWidget", u"1", None));
        ___qtablewidgetitem25 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("DockWidget", u"30", None));
        ___qtablewidgetitem26 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("DockWidget", u"4", None));
        ___qtablewidgetitem27 = self.tableWidget_2.item(0, 3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("DockWidget", u"5", None));
        ___qtablewidgetitem28 = self.tableWidget_2.item(0, 4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("DockWidget", u"285", None));
        ___qtablewidgetitem29 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("DockWidget", u"0", None));
        ___qtablewidgetitem30 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("DockWidget", u"0", None));
        ___qtablewidgetitem31 = self.tableWidget_2.item(1, 2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("DockWidget", u"0", None));
        ___qtablewidgetitem32 = self.tableWidget_2.item(1, 3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("DockWidget", u"0", None));
        ___qtablewidgetitem33 = self.tableWidget_2.item(1, 4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("DockWidget", u"101", None));
        ___qtablewidgetitem34 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("DockWidget", u"0", None));
        ___qtablewidgetitem35 = self.tableWidget_2.item(2, 1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("DockWidget", u"0", None));
        ___qtablewidgetitem36 = self.tableWidget_2.item(2, 2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("DockWidget", u"0", None));
        ___qtablewidgetitem37 = self.tableWidget_2.item(2, 3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("DockWidget", u"0", None));
        ___qtablewidgetitem38 = self.tableWidget_2.item(2, 4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("DockWidget", u"101", None));
        ___qtablewidgetitem39 = self.tableWidget_2.item(3, 0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("DockWidget", u"1000", None));
        ___qtablewidgetitem40 = self.tableWidget_2.item(3, 1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("DockWidget", u"30", None));
        ___qtablewidgetitem41 = self.tableWidget_2.item(3, 2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("DockWidget", u"4", None));
        ___qtablewidgetitem42 = self.tableWidget_2.item(3, 3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("DockWidget", u"5", None));
        ___qtablewidgetitem43 = self.tableWidget_2.item(3, 4)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("DockWidget", u"99", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("DockWidget", u"Thickogram", None))
    # retranslateUi

