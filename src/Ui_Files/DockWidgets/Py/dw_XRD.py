# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_XRD.ui'
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
        DockWidget.resize(504, 551)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tw_x = QTreeWidget(self.tab)
        self.tw_x.setObjectName(u"tw_x")

        self.gridLayout_2.addWidget(self.tw_x, 1, 0, 1, 1)

        self.tw_y = QTreeWidget(self.tab)
        self.tw_y.setObjectName(u"tw_y")

        self.gridLayout_2.addWidget(self.tw_y, 1, 1, 1, 1)

        self.treeView = QTreeView(self.tab)
        self.treeView.setObjectName(u"treeView")

        self.gridLayout_2.addWidget(self.treeView, 0, 0, 1, 2)

        self.fillcols_pb = QPushButton(self.tab)
        self.fillcols_pb.setObjectName(u"fillcols_pb")

        self.gridLayout_2.addWidget(self.fillcols_pb, 2, 0, 1, 1)

        self.plot_pb = QPushButton(self.tab)
        self.plot_pb.setObjectName(u"plot_pb")

        self.gridLayout_2.addWidget(self.plot_pb, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radioButton_2 = QRadioButton(self.tab_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_3.addWidget(self.radioButton_2, 4, 0, 1, 1)

        self.line_2 = QFrame(self.tab_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 5, 0, 1, 2)

        self.listView = QListView(self.tab_2)
        self.listView.setObjectName(u"listView")

        self.gridLayout_3.addWidget(self.listView, 7, 0, 1, 2)

        self.line = QFrame(self.tab_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 3, 0, 1, 2)

        self.radioButton_3 = QRadioButton(self.tab_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setChecked(True)

        self.gridLayout_3.addWidget(self.radioButton_3, 4, 1, 1, 1)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 1, 1, 1, 1)

        self.horizontalSlider = QSlider(self.tab_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.tab_2)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_3.addWidget(self.checkBox, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lambda_sb = QSpinBox(self.tab_4)
        self.lambda_sb.setObjectName(u"lambda_sb")
        self.lambda_sb.setMaximum(999999999)
        self.lambda_sb.setSingleStep(1000)
        self.lambda_sb.setValue(1000)

        self.gridLayout_5.addWidget(self.lambda_sb, 0, 1, 1, 1)

        self.baseline_pb = QPushButton(self.tab_4)
        self.baseline_pb.setObjectName(u"baseline_pb")

        self.gridLayout_5.addWidget(self.baseline_pb, 2, 1, 1, 1)

        self.fittype_cb = QComboBox(self.tab_4)
        self.fittype_cb.addItem("")
        self.fittype_cb.addItem("")
        self.fittype_cb.addItem("")
        self.fittype_cb.setObjectName(u"fittype_cb")

        self.gridLayout_5.addWidget(self.fittype_cb, 4, 0, 1, 1)

        self.label_9 = QLabel(self.tab_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)

        self.p_sb = QDoubleSpinBox(self.tab_4)
        self.p_sb.setObjectName(u"p_sb")
        self.p_sb.setDecimals(5)
        self.p_sb.setMaximum(1.000000000000000)
        self.p_sb.setSingleStep(0.005000000000000)
        self.p_sb.setValue(0.010000000000000)

        self.gridLayout_5.addWidget(self.p_sb, 1, 1, 1, 1)

        self.tw_fit_params = QTableWidget(self.tab_4)
        if (self.tw_fit_params.columnCount() < 3):
            self.tw_fit_params.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_fit_params.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_fit_params.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_fit_params.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tw_fit_params.rowCount() < 2):
            self.tw_fit_params.setRowCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_fit_params.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_fit_params.setVerticalHeaderItem(1, __qtablewidgetitem4)
        self.tw_fit_params.setObjectName(u"tw_fit_params")
        self.tw_fit_params.setMaximumSize(QSize(400, 120))
        self.tw_fit_params.setRowCount(2)
        self.tw_fit_params.setColumnCount(3)

        self.gridLayout_5.addWidget(self.tw_fit_params, 5, 0, 1, 2)

        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 1, 0, 1, 1)

        self.fit_pb = QPushButton(self.tab_4)
        self.fit_pb.setObjectName(u"fit_pb")

        self.gridLayout_5.addWidget(self.fit_pb, 7, 1, 1, 1)

        self.line_5 = QFrame(self.tab_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_5, 3, 0, 1, 2)

        self.fit_init_pb = QPushButton(self.tab_4)
        self.fit_init_pb.setObjectName(u"fit_init_pb")

        self.gridLayout_5.addWidget(self.fit_init_pb, 7, 0, 1, 1)

        self.fit_results_te = QTextEdit(self.tab_4)
        self.fit_results_te.setObjectName(u"fit_results_te")

        self.gridLayout_5.addWidget(self.fit_results_te, 8, 0, 1, 2)

        self.num_peaks_sb = QSpinBox(self.tab_4)
        self.num_peaks_sb.setObjectName(u"num_peaks_sb")
        self.num_peaks_sb.setMinimum(1)
        self.num_peaks_sb.setMaximum(2)

        self.gridLayout_5.addWidget(self.num_peaks_sb, 4, 1, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 11, 0, 1, 1)

        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 6, 0, 1, 1)

        self.go_pb = QPushButton(self.tab_3)
        self.go_pb.setObjectName(u"go_pb")

        self.gridLayout_4.addWidget(self.go_pb, 9, 0, 1, 1)

        self.fwhm_sb = QDoubleSpinBox(self.tab_3)
        self.fwhm_sb.setObjectName(u"fwhm_sb")
        self.fwhm_sb.setDecimals(7)
        self.fwhm_sb.setMaximum(99.000000000000000)
        self.fwhm_sb.setSingleStep(0.100000000000000)
        self.fwhm_sb.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.fwhm_sb, 7, 1, 1, 2)

        self.c_size_label = QLabel(self.tab_3)
        self.c_size_label.setObjectName(u"c_size_label")
        self.c_size_label.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_4.addWidget(self.c_size_label, 11, 1, 1, 1)

        self.theta_sb = QDoubleSpinBox(self.tab_3)
        self.theta_sb.setObjectName(u"theta_sb")
        self.theta_sb.setValue(30.000000000000000)

        self.gridLayout_4.addWidget(self.theta_sb, 6, 1, 1, 2)

        self.k_sb = QDoubleSpinBox(self.tab_3)
        self.k_sb.setObjectName(u"k_sb")
        self.k_sb.setMaximum(2.000000000000000)
        self.k_sb.setSingleStep(0.050000000000000)
        self.k_sb.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.k_sb, 4, 1, 1, 2)

        self.line_4 = QFrame(self.tab_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_4, 3, 0, 1, 3)

        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 7, 0, 1, 1)

        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 11, 2, 1, 1)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 4, 0, 1, 1)

        self.line_3 = QFrame(self.tab_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 9, 1, 1, 2)

        self.lambda_sb_2 = QDoubleSpinBox(self.tab_3)
        self.lambda_sb_2.setObjectName(u"lambda_sb_2")
        self.lambda_sb_2.setDecimals(3)
        self.lambda_sb_2.setValue(0.154000000000000)

        self.gridLayout_4.addWidget(self.lambda_sb_2, 5, 1, 1, 2)

        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))
        self.label_4.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_4.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_12 = QLabel(self.tab_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"Views", None))
        ___qtreewidgetitem = self.tw_x.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("DockWidget", u"X (select x data)", None));
        ___qtreewidgetitem1 = self.tw_y.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("DockWidget", u"Y (select y data)", None));
        self.fillcols_pb.setText(QCoreApplication.translate("DockWidget", u"Fill Cols (do this before plot)", None))
        self.plot_pb.setText(QCoreApplication.translate("DockWidget", u"Plot (do after fill cols)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("DockWidget", u"XRD Plotting", None))
        self.radioButton_2.setText(QCoreApplication.translate("DockWidget", u"Log ", None))
        self.radioButton_3.setText(QCoreApplication.translate("DockWidget", u"Linear", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"Threshold", None))
        self.label_11.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.checkBox.setText(QCoreApplication.translate("DockWidget", u"On", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("DockWidget", u"Peak Finder", None))
        self.baseline_pb.setText(QCoreApplication.translate("DockWidget", u"Baseline", None))
        self.fittype_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Gaussian", None))
        self.fittype_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Pseudo-Voigt", None))
        self.fittype_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"Lorentz", None))

        self.label_9.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p>\u03bb  (smoothness)</p></body></html>", None))
        ___qtablewidgetitem = self.tw_fit_params.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DockWidget", u"Amplitude", None));
        ___qtablewidgetitem1 = self.tw_fit_params.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DockWidget", u"Peak Position", None));
        ___qtablewidgetitem2 = self.tw_fit_params.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DockWidget", u"Sigma", None));
        ___qtablewidgetitem3 = self.tw_fit_params.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DockWidget", u"Peak 1", None));
        ___qtablewidgetitem4 = self.tw_fit_params.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DockWidget", u"Peak 2", None));
        self.label_10.setText(QCoreApplication.translate("DockWidget", u"P (asymetry) ", None))
        self.fit_pb.setText(QCoreApplication.translate("DockWidget", u"Fit", None))
        self.fit_init_pb.setText(QCoreApplication.translate("DockWidget", u"Fit Init", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("DockWidget", u"Peak Fit", None))
        self.label_7.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p>crystal size (in units of &lambda;)</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p>&theta;  (peak is at 2&theta;) </p></body></html>", None))
        self.go_pb.setText(QCoreApplication.translate("DockWidget", u"Go", None))
        self.c_size_label.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label_6.setText(QCoreApplication.translate("DockWidget", u"FWHM (in Rad.)", None))
        self.label_3.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p>&lambda;  (x-ray wavelength) nm </p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("DockWidget", u"nm", None))
        self.label_2.setText(QCoreApplication.translate("DockWidget", u"k (shape factor)", None))
        self.label_4.setText(QCoreApplication.translate("DockWidget", u"<p>Size =  (k*&lambda;)/(cos(&theta;)*FWHM)</p>", None))
        self.label_12.setText(QCoreApplication.translate("DockWidget", u"<p>Gaussian FWHM: 2.3548&sigma;</p>\n"
"<p>Lorentz FWHM: 2&sigma; </p>\n"
"<p>Voigt FWHM: 3.6013&sigma;</p>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("DockWidget", u"Scherrer", None))
    # retranslateUi

