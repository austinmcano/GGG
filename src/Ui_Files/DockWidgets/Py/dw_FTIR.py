# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_FTIR.ui'
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
        DockWidget.resize(516, 600)
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

        self.gridLayout_2.addWidget(self.label_6, 13, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.smooth_pb = QPushButton(self.tab)
        self.smooth_pb.setObjectName(u"smooth_pb")

        self.gridLayout_2.addWidget(self.smooth_pb, 16, 3, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 16, 1, 1, 1)

        self.FTIR_treeView = QTreeView(self.tab)
        self.FTIR_treeView.setObjectName(u"FTIR_treeView")

        self.gridLayout_2.addWidget(self.FTIR_treeView, 0, 1, 1, 3)

        self.lambda_sb = QSpinBox(self.tab)
        self.lambda_sb.setObjectName(u"lambda_sb")
        self.lambda_sb.setMaximum(9999999)
        self.lambda_sb.setSingleStep(1000)
        self.lambda_sb.setValue(1000)

        self.gridLayout_2.addWidget(self.lambda_sb, 11, 2, 1, 1)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 10, 1, 1, 3)

        self.baseline_pb = QPushButton(self.tab)
        self.baseline_pb.setObjectName(u"baseline_pb")

        self.gridLayout_2.addWidget(self.baseline_pb, 11, 3, 1, 1)

        self.ir_plot_cb = QComboBox(self.tab)
        self.ir_plot_cb.addItem("")
        self.ir_plot_cb.addItem("")
        self.ir_plot_cb.addItem("")
        self.ir_plot_cb.addItem("")
        self.ir_plot_cb.addItem("")
        self.ir_plot_cb.setObjectName(u"ir_plot_cb")

        self.gridLayout_2.addWidget(self.ir_plot_cb, 5, 1, 1, 2)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 11, 1, 1, 1)

        self.skip_sb = QSpinBox(self.tab)
        self.skip_sb.setObjectName(u"skip_sb")
        self.skip_sb.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.skip_sb.setKeyboardTracking(False)
        self.skip_sb.setValue(0)

        self.gridLayout_2.addWidget(self.skip_sb, 7, 2, 1, 1)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 7, 1, 1, 1)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 5, 3, 1, 1)

        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 14, 1, 1, 3)

        self.smooth_sb = QSpinBox(self.tab)
        self.smooth_sb.setObjectName(u"smooth_sb")

        self.gridLayout_2.addWidget(self.smooth_sb, 16, 2, 1, 1)

        self.p_sb = QDoubleSpinBox(self.tab)
        self.p_sb.setObjectName(u"p_sb")
        self.p_sb.setDecimals(6)
        self.p_sb.setMaximum(1000.000000000000000)
        self.p_sb.setSingleStep(0.010000000000000)
        self.p_sb.setValue(0.010000000000000)

        self.gridLayout_2.addWidget(self.p_sb, 13, 2, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 13, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 4, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 3, 1, 1)

        self.pushButton_6 = QPushButton(self.tab)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 4, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.tab)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 4, 3, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.doubleSpinBox_47 = QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_47.setObjectName(u"doubleSpinBox_47")

        self.gridLayout_4.addWidget(self.doubleSpinBox_47, 2, 4, 1, 1)

        self.integratemode_rb = QRadioButton(self.tab_3)
        self.integratemode_rb.setObjectName(u"integratemode_rb")

        self.gridLayout_4.addWidget(self.integratemode_rb, 1, 3, 1, 1)

        self.tableWidget = QTableWidget(self.tab_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(320, 0))
        self.tableWidget.setMaximumSize(QSize(1000, 1000))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)

        self.gridLayout_4.addWidget(self.tableWidget, 4, 3, 4, 2)

        self.comboBox = QComboBox(self.tab_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.comboBox, 1, 4, 1, 1)

        self.doubleSpinBox_46 = QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_46.setObjectName(u"doubleSpinBox_46")

        self.gridLayout_4.addWidget(self.doubleSpinBox_46, 2, 3, 1, 1)

        self.line_3 = QFrame(self.tab_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 9, 3, 1, 2)

        self.integrate_pb = QPushButton(self.tab_3)
        self.integrate_pb.setObjectName(u"integrate_pb")
        self.integrate_pb.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.integrate_pb, 3, 4, 1, 1)

        self.textBrowser = QTextBrowser(self.tab_3)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_4.addWidget(self.textBrowser, 0, 3, 1, 2)

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
        self.doubleSpinBox_13 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_13.setObjectName(u"doubleSpinBox_13")

        self.gridLayout_5.addWidget(self.doubleSpinBox_13, 6, 2, 1, 1)

        self.doubleSpinBox_11 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_11.setObjectName(u"doubleSpinBox_11")

        self.gridLayout_5.addWidget(self.doubleSpinBox_11, 4, 2, 1, 1)

        self.textEdit = QTextEdit(self.tab_4)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_5.addWidget(self.textEdit, 10, 1, 1, 6)

        self.doubleSpinBox_31 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_31.setObjectName(u"doubleSpinBox_31")

        self.gridLayout_5.addWidget(self.doubleSpinBox_31, 7, 4, 1, 1)

        self.label_8 = QLabel(self.tab_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 1, 1, 1, 1)

        self.doubleSpinBox_21 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_21.setObjectName(u"doubleSpinBox_21")

        self.gridLayout_5.addWidget(self.doubleSpinBox_21, 7, 3, 1, 1)

        self.doubleSpinBox_25 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_25.setObjectName(u"doubleSpinBox_25")

        self.gridLayout_5.addWidget(self.doubleSpinBox_25, 3, 5, 1, 1)

        self.doubleSpinBox_39 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_39.setObjectName(u"doubleSpinBox_39")

        self.gridLayout_5.addWidget(self.doubleSpinBox_39, 6, 6, 1, 1)

        self.label_15 = QLabel(self.tab_4)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 8, 1, 1, 1)

        self.doubleSpinBox_17 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_17.setObjectName(u"doubleSpinBox_17")

        self.gridLayout_5.addWidget(self.doubleSpinBox_17, 3, 3, 1, 1)

        self.doubleSpinBox_10 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_10.setObjectName(u"doubleSpinBox_10")

        self.gridLayout_5.addWidget(self.doubleSpinBox_10, 3, 2, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout_5.addWidget(self.doubleSpinBox, 1, 3, 1, 1)

        self.doubleSpinBox_26 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_26.setObjectName(u"doubleSpinBox_26")

        self.gridLayout_5.addWidget(self.doubleSpinBox_26, 2, 6, 1, 1)

        self.radioButton_5 = QRadioButton(self.tab_4)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout_5.addWidget(self.radioButton_5, 0, 5, 1, 1)

        self.radioButton_6 = QRadioButton(self.tab_4)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout_5.addWidget(self.radioButton_6, 0, 6, 1, 1)

        self.doubleSpinBox_23 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_23.setObjectName(u"doubleSpinBox_23")

        self.gridLayout_5.addWidget(self.doubleSpinBox_23, 9, 3, 1, 1)

        self.label_11 = QLabel(self.tab_4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 4, 1, 1, 1)

        self.doubleSpinBox_19 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_19.setObjectName(u"doubleSpinBox_19")

        self.gridLayout_5.addWidget(self.doubleSpinBox_19, 5, 3, 1, 1)

        self.label_9 = QLabel(self.tab_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 2, 1, 1, 1)

        self.doubleSpinBox_15 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_15.setObjectName(u"doubleSpinBox_15")

        self.gridLayout_5.addWidget(self.doubleSpinBox_15, 8, 2, 1, 1)

        self.radioButton_2 = QRadioButton(self.tab_4)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_5.addWidget(self.radioButton_2, 0, 2, 1, 1)

        self.doubleSpinBox_35 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_35.setObjectName(u"doubleSpinBox_35")

        self.gridLayout_5.addWidget(self.doubleSpinBox_35, 4, 6, 1, 1)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")

        self.gridLayout_5.addWidget(self.doubleSpinBox_7, 2, 3, 1, 1)

        self.label_17 = QLabel(self.tab_4)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 0, 1, 1, 1)

        self.label_14 = QLabel(self.tab_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 7, 1, 1, 1)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.gridLayout_5.addWidget(self.doubleSpinBox_3, 1, 4, 1, 1)

        self.doubleSpinBox_29 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_29.setObjectName(u"doubleSpinBox_29")

        self.gridLayout_5.addWidget(self.doubleSpinBox_29, 5, 4, 1, 1)

        self.doubleSpinBox_42 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_42.setObjectName(u"doubleSpinBox_42")

        self.gridLayout_5.addWidget(self.doubleSpinBox_42, 8, 5, 1, 1)

        self.doubleSpinBox_30 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_30.setObjectName(u"doubleSpinBox_30")

        self.gridLayout_5.addWidget(self.doubleSpinBox_30, 6, 4, 1, 1)

        self.doubleSpinBox_28 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_28.setObjectName(u"doubleSpinBox_28")

        self.gridLayout_5.addWidget(self.doubleSpinBox_28, 4, 4, 1, 1)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")

        self.gridLayout_5.addWidget(self.doubleSpinBox_5, 1, 6, 1, 1)

        self.radioButton_3 = QRadioButton(self.tab_4)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_5.addWidget(self.radioButton_3, 0, 3, 1, 1)

        self.label_16 = QLabel(self.tab_4)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 9, 1, 1, 1)

        self.radioButton_4 = QRadioButton(self.tab_4)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout_5.addWidget(self.radioButton_4, 0, 4, 1, 1)

        self.doubleSpinBox_45 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_45.setObjectName(u"doubleSpinBox_45")

        self.gridLayout_5.addWidget(self.doubleSpinBox_45, 9, 6, 1, 1)

        self.doubleSpinBox_37 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_37.setObjectName(u"doubleSpinBox_37")

        self.gridLayout_5.addWidget(self.doubleSpinBox_37, 5, 5, 1, 1)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")

        self.gridLayout_5.addWidget(self.doubleSpinBox_9, 2, 5, 1, 1)

        self.doubleSpinBox_32 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_32.setObjectName(u"doubleSpinBox_32")

        self.gridLayout_5.addWidget(self.doubleSpinBox_32, 8, 4, 1, 1)

        self.doubleSpinBox_41 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_41.setObjectName(u"doubleSpinBox_41")

        self.gridLayout_5.addWidget(self.doubleSpinBox_41, 7, 6, 1, 1)

        self.label_12 = QLabel(self.tab_4)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 5, 1, 1, 1)

        self.doubleSpinBox_40 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_40.setObjectName(u"doubleSpinBox_40")

        self.gridLayout_5.addWidget(self.doubleSpinBox_40, 7, 5, 1, 1)

        self.doubleSpinBox_22 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_22.setObjectName(u"doubleSpinBox_22")

        self.gridLayout_5.addWidget(self.doubleSpinBox_22, 8, 3, 1, 1)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")

        self.gridLayout_5.addWidget(self.doubleSpinBox_4, 1, 5, 1, 1)

        self.doubleSpinBox_20 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_20.setObjectName(u"doubleSpinBox_20")

        self.gridLayout_5.addWidget(self.doubleSpinBox_20, 6, 3, 1, 1)

        self.doubleSpinBox_14 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_14.setObjectName(u"doubleSpinBox_14")

        self.gridLayout_5.addWidget(self.doubleSpinBox_14, 7, 2, 1, 1)

        self.doubleSpinBox_24 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_24.setObjectName(u"doubleSpinBox_24")

        self.gridLayout_5.addWidget(self.doubleSpinBox_24, 3, 4, 1, 1)

        self.doubleSpinBox_18 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_18.setObjectName(u"doubleSpinBox_18")

        self.gridLayout_5.addWidget(self.doubleSpinBox_18, 4, 3, 1, 1)

        self.doubleSpinBox_33 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_33.setObjectName(u"doubleSpinBox_33")

        self.gridLayout_5.addWidget(self.doubleSpinBox_33, 9, 4, 1, 1)

        self.doubleSpinBox_12 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_12.setObjectName(u"doubleSpinBox_12")

        self.gridLayout_5.addWidget(self.doubleSpinBox_12, 5, 2, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.gridLayout_5.addWidget(self.doubleSpinBox_2, 1, 2, 1, 1)

        self.doubleSpinBox_38 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_38.setObjectName(u"doubleSpinBox_38")

        self.gridLayout_5.addWidget(self.doubleSpinBox_38, 6, 5, 1, 1)

        self.doubleSpinBox_36 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_36.setObjectName(u"doubleSpinBox_36")

        self.gridLayout_5.addWidget(self.doubleSpinBox_36, 5, 6, 1, 1)

        self.doubleSpinBox_44 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_44.setObjectName(u"doubleSpinBox_44")

        self.gridLayout_5.addWidget(self.doubleSpinBox_44, 9, 5, 1, 1)

        self.doubleSpinBox_16 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_16.setObjectName(u"doubleSpinBox_16")

        self.gridLayout_5.addWidget(self.doubleSpinBox_16, 9, 2, 1, 1)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")

        self.gridLayout_5.addWidget(self.doubleSpinBox_6, 2, 2, 1, 1)

        self.doubleSpinBox_34 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_34.setObjectName(u"doubleSpinBox_34")

        self.gridLayout_5.addWidget(self.doubleSpinBox_34, 4, 5, 1, 1)

        self.doubleSpinBox_27 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_27.setObjectName(u"doubleSpinBox_27")

        self.gridLayout_5.addWidget(self.doubleSpinBox_27, 3, 6, 1, 1)

        self.label_13 = QLabel(self.tab_4)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 6, 1, 1, 1)

        self.doubleSpinBox_43 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_43.setObjectName(u"doubleSpinBox_43")

        self.gridLayout_5.addWidget(self.doubleSpinBox_43, 8, 6, 1, 1)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")

        self.gridLayout_5.addWidget(self.doubleSpinBox_8, 2, 4, 1, 1)

        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 3, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.tab_4)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_5.addWidget(self.pushButton_8, 11, 1, 1, 2)

        self.pushButton_9 = QPushButton(self.tab_4)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_5.addWidget(self.pushButton_9, 11, 3, 1, 2)

        self.pushButton_10 = QPushButton(self.tab_4)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_5.addWidget(self.pushButton_10, 11, 5, 1, 2)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 3, 0, 1, 2)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"FTIR", None))
        self.label_6.setText(QCoreApplication.translate("DockWidget", u"P (asymetry) ", None))
        self.pushButton_2.setText(QCoreApplication.translate("DockWidget", u"Sub Plot (dir)", None))
        self.smooth_pb.setText(QCoreApplication.translate("DockWidget", u"Smooth", None))
        self.label_3.setText(QCoreApplication.translate("DockWidget", u"Savitzky\u2013Golay Filter", None))
        self.baseline_pb.setText(QCoreApplication.translate("DockWidget", u"Baseline All", None))
        self.ir_plot_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Sub Plot (dir)", None))
        self.ir_plot_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Plot (dir)", None))
        self.ir_plot_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"Diff Plot (dir)", None))
        self.ir_plot_cb.setItemText(3, QCoreApplication.translate("DockWidget", u"Diff (2)", None))
        self.ir_plot_cb.setItemText(4, QCoreApplication.translate("DockWidget", u"Plot", None))

        self.label_4.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p>\u03bb  (smoothness)</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"Skip Every", None))
        self.pushButton.setText(QCoreApplication.translate("DockWidget", u"Plot or Fit FTIR", None))
        self.label_7.setText(QCoreApplication.translate("DockWidget", u"UNDER WORK", None))
        self.pushButton_5.setText(QCoreApplication.translate("DockWidget", u"Plot", None))
        self.pushButton_3.setText(QCoreApplication.translate("DockWidget", u"Diff Plot (dir)", None))
        self.pushButton_4.setText(QCoreApplication.translate("DockWidget", u"Plot (dir)", None))
        self.pushButton_6.setText(QCoreApplication.translate("DockWidget", u"Diff Plot (2)", None))
        self.pushButton_7.setText(QCoreApplication.translate("DockWidget", u"TBD", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("DockWidget", u"IR Plot", None))
        self.integratemode_rb.setText(QCoreApplication.translate("DockWidget", u"Integrate Mode", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("DockWidget", u"Left Axis", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("DockWidget", u"Right Axis", None))

        self.integrate_pb.setText(QCoreApplication.translate("DockWidget", u"Integrate", None))
        self.textBrowser.setHtml(QCoreApplication.translate("DockWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press integrate mode.  Add the spectra to the top axis then click and hold on one limit and release on the other limit and the integral will show up on the axis below as well as in the table below here,  or manually type in the limits below and press &quot;Integrate&quot;</p></body></html>", None))
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
        self.label_8.setText(QCoreApplication.translate("DockWidget", u"Amp", None))
        self.label_15.setText(QCoreApplication.translate("DockWidget", u"low", None))
        self.radioButton_5.setText(QCoreApplication.translate("DockWidget", u"Peak 4", None))
        self.radioButton_6.setText(QCoreApplication.translate("DockWidget", u"Peak 5", None))
        self.label_11.setText(QCoreApplication.translate("DockWidget", u"Cen", None))
        self.label_9.setText(QCoreApplication.translate("DockWidget", u"low", None))
        self.radioButton_2.setText(QCoreApplication.translate("DockWidget", u"Peak 1", None))
        self.label_17.setText(QCoreApplication.translate("DockWidget", u"Peak #", None))
        self.label_14.setText(QCoreApplication.translate("DockWidget", u"sigma", None))
        self.radioButton_3.setText(QCoreApplication.translate("DockWidget", u"Peak 2", None))
        self.label_16.setText(QCoreApplication.translate("DockWidget", u"high", None))
        self.radioButton_4.setText(QCoreApplication.translate("DockWidget", u"Peak 3", None))
        self.label_12.setText(QCoreApplication.translate("DockWidget", u"low", None))
        self.label_13.setText(QCoreApplication.translate("DockWidget", u"high", None))
        self.label_10.setText(QCoreApplication.translate("DockWidget", u"high", None))
        self.pushButton_8.setText(QCoreApplication.translate("DockWidget", u"Select Data", None))
        self.pushButton_9.setText(QCoreApplication.translate("DockWidget", u"Fit Init", None))
        self.pushButton_10.setText(QCoreApplication.translate("DockWidget", u"Fit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("DockWidget", u"Fitting_2", None))
    # retranslateUi

