# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_XPS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
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
        DockWidget.resize(414, 550)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_7 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.error_log = QLineEdit(self.dockWidgetContents)
        self.error_log.setObjectName(u"error_log")

        self.gridLayout_7.addWidget(self.error_log, 2, 0, 1, 1)

        self.plot_pb = QPushButton(self.dockWidgetContents)
        self.plot_pb.setObjectName(u"plot_pb")

        self.gridLayout_7.addWidget(self.plot_pb, 2, 1, 1, 1)

        self.tabWidget = QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_8 = QGridLayout(self.tab_13)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_40 = QLabel(self.tab_13)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_8.addWidget(self.label_40, 3, 3, 1, 1)

        self.sigma_low = QLineEdit(self.tab_13)
        self.sigma_low.setObjectName(u"sigma_low")
        self.sigma_low.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.sigma_low, 7, 2, 1, 1)

        self.amp_LE = QLineEdit(self.tab_13)
        self.amp_LE.setObjectName(u"amp_LE")
        self.amp_LE.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.amp_LE, 5, 1, 1, 1)

        self.fwhm_label = QLabel(self.tab_13)
        self.fwhm_label.setObjectName(u"fwhm_label")

        self.gridLayout_8.addWidget(self.fwhm_label, 7, 0, 1, 1)

        self.sigma_LE = QLineEdit(self.tab_13)
        self.sigma_LE.setObjectName(u"sigma_LE")
        self.sigma_LE.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.sigma_LE, 7, 1, 1, 1)

        self.cen_LE = QLineEdit(self.tab_13)
        self.cen_LE.setObjectName(u"cen_LE")
        self.cen_LE.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.cen_LE, 6, 1, 1, 1)

        self.label_39 = QLabel(self.tab_13)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_8.addWidget(self.label_39, 3, 2, 1, 1)

        self.amp_high = QLineEdit(self.tab_13)
        self.amp_high.setObjectName(u"amp_high")
        self.amp_high.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.amp_high, 5, 3, 1, 1)

        self.amp_label = QLabel(self.tab_13)
        self.amp_label.setObjectName(u"amp_label")

        self.gridLayout_8.addWidget(self.amp_label, 5, 0, 1, 1)

        self.peak_label = QLabel(self.tab_13)
        self.peak_label.setObjectName(u"peak_label")

        self.gridLayout_8.addWidget(self.peak_label, 6, 0, 1, 1)

        self.cen_high = QLineEdit(self.tab_13)
        self.cen_high.setObjectName(u"cen_high")
        self.cen_high.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.cen_high, 6, 3, 1, 1)

        self.amp_low = QLineEdit(self.tab_13)
        self.amp_low.setObjectName(u"amp_low")
        self.amp_low.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.amp_low, 5, 2, 1, 1)

        self.cen_low = QLineEdit(self.tab_13)
        self.cen_low.setObjectName(u"cen_low")
        self.cen_low.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.cen_low, 6, 2, 1, 1)

        self.sigma_high = QLineEdit(self.tab_13)
        self.sigma_high.setObjectName(u"sigma_high")
        self.sigma_high.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.sigma_high, 7, 3, 1, 1)

        self.XPS_treeView = QTreeView(self.tab_13)
        self.XPS_treeView.setObjectName(u"XPS_treeView")
        self.XPS_treeView.setMaximumSize(QSize(1000, 16777215))

        self.gridLayout_8.addWidget(self.XPS_treeView, 0, 0, 1, 4)

        self.shirley_pb = QPushButton(self.tab_13)
        self.shirley_pb.setObjectName(u"shirley_pb")
        self.shirley_pb.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.shirley_pb, 2, 2, 1, 1)

        self.plot_curr_pb = QPushButton(self.tab_13)
        self.plot_curr_pb.setObjectName(u"plot_curr_pb")
        self.plot_curr_pb.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.plot_curr_pb, 2, 3, 1, 1)

        self.fit_pb = QPushButton(self.tab_13)
        self.fit_pb.setObjectName(u"fit_pb")
        self.fit_pb.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.fit_pb, 9, 3, 1, 1)

        self.peak_num_cb = QComboBox(self.tab_13)
        self.peak_num_cb.addItem("")
        self.peak_num_cb.setObjectName(u"peak_num_cb")
        self.peak_num_cb.setMaximumSize(QSize(80, 100))
        self.peak_num_cb.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_8.addWidget(self.peak_num_cb, 3, 0, 1, 1)

        self.fit_shape_cb = QComboBox(self.tab_13)
        self.fit_shape_cb.addItem("")
        self.fit_shape_cb.addItem("")
        self.fit_shape_cb.addItem("")
        self.fit_shape_cb.setObjectName(u"fit_shape_cb")

        self.gridLayout_8.addWidget(self.fit_shape_cb, 3, 1, 1, 1)

        self.num_peaks_sb = QSpinBox(self.tab_13)
        self.num_peaks_sb.setObjectName(u"num_peaks_sb")
        self.num_peaks_sb.setMaximumSize(QSize(80, 16777215))
        self.num_peaks_sb.setMinimum(1)

        self.gridLayout_8.addWidget(self.num_peaks_sb, 2, 1, 1, 1)

        self.label_44 = QLabel(self.tab_13)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_8.addWidget(self.label_44, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_13, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.gridLayout_9 = QGridLayout(self.tab_15)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.fit_report_TE = QTextEdit(self.tab_15)
        self.fit_report_TE.setObjectName(u"fit_report_TE")

        self.gridLayout_9.addWidget(self.fit_report_TE, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_15, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.gridLayout_10 = QGridLayout(self.tab_14)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_47 = QLabel(self.tab_14)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.label_47, 4, 0, 1, 1)

        self.graphicsView = QGraphicsView(self.tab_14)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_10.addWidget(self.graphicsView, 0, 0, 1, 6)

        self.lineEdit_9 = QLineEdit(self.tab_14)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.lineEdit_9, 2, 2, 1, 1)

        self.lineEdit_8 = QLineEdit(self.tab_14)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.lineEdit_8, 2, 3, 1, 1)

        self.label_49 = QLabel(self.tab_14)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.label_49, 1, 5, 1, 1)

        self.lineEdit_7 = QLineEdit(self.tab_14)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.lineEdit_7, 2, 1, 1, 1)

        self.lineEdit_16 = QLineEdit(self.tab_14)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.lineEdit_16, 4, 2, 1, 1)

        self.label_42 = QLabel(self.tab_14)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.label_42, 2, 0, 1, 1)

        self.lineEdit_21 = QLineEdit(self.tab_14)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.lineEdit_21, 4, 5, 1, 1)

        self.label_48 = QLabel(self.tab_14)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.label_48, 1, 4, 1, 1)

        self.lineEdit_15 = QLineEdit(self.tab_14)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.lineEdit_15, 4, 1, 1, 1)

        self.lineEdit_13 = QLineEdit(self.tab_14)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.lineEdit_13, 2, 4, 1, 1)

        self.lineEdit_17 = QLineEdit(self.tab_14)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.lineEdit_17, 4, 3, 1, 1)

        self.lineEdit_11 = QLineEdit(self.tab_14)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.lineEdit_11, 3, 3, 1, 1)

        self.label_41 = QLabel(self.tab_14)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.label_41, 1, 1, 1, 1)

        self.lineEdit_18 = QLineEdit(self.tab_14)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.lineEdit_18, 4, 4, 1, 1)

        self.lineEdit_19 = QLineEdit(self.tab_14)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.lineEdit_19, 2, 5, 1, 1)

        self.lineEdit_14 = QLineEdit(self.tab_14)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.lineEdit_14, 3, 4, 1, 1)

        self.lineEdit_20 = QLineEdit(self.tab_14)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.lineEdit_20, 3, 5, 1, 1)

        self.lineEdit_10 = QLineEdit(self.tab_14)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.lineEdit_10, 3, 1, 1, 1)

        self.label_45 = QLabel(self.tab_14)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.label_45, 1, 3, 1, 1)

        self.lineEdit_12 = QLineEdit(self.tab_14)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.lineEdit_12, 3, 2, 1, 1)

        self.label_43 = QLabel(self.tab_14)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.label_43, 1, 2, 1, 1)

        self.label_46 = QLabel(self.tab_14)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_10.addWidget(self.label_46, 3, 0, 1, 1)

        self.textEdit = QTextEdit(self.tab_14)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_10.addWidget(self.textEdit, 5, 0, 1, 6)

        self.tabWidget.addTab(self.tab_14, "")

        self.gridLayout_7.addWidget(self.tabWidget, 1, 0, 1, 2)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"XPS", None))
        self.error_log.setText(QCoreApplication.translate("DockWidget", u"Error Log", None))
        self.plot_pb.setText(QCoreApplication.translate("DockWidget", u"Plot", None))
        self.label_40.setText(QCoreApplication.translate("DockWidget", u"High", None))
        self.sigma_low.setText("")
        self.amp_LE.setText("")
        self.fwhm_label.setText(QCoreApplication.translate("DockWidget", u"Sigma", None))
        self.sigma_LE.setText("")
        self.cen_LE.setText("")
        self.label_39.setText(QCoreApplication.translate("DockWidget", u"Low", None))
        self.amp_high.setText("")
        self.amp_label.setText(QCoreApplication.translate("DockWidget", u"Amp", None))
        self.peak_label.setText(QCoreApplication.translate("DockWidget", u"Cen.", None))
        self.cen_high.setText("")
        self.amp_low.setText("")
        self.cen_low.setText("")
        self.sigma_high.setText("")
        self.shirley_pb.setText(QCoreApplication.translate("DockWidget", u"Shirley", None))
        self.plot_curr_pb.setText(QCoreApplication.translate("DockWidget", u"Plot Curr", None))
        self.fit_pb.setText(QCoreApplication.translate("DockWidget", u"Fit", None))
        self.peak_num_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"1", None))

        self.fit_shape_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Gaussian", None))
        self.fit_shape_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Lorentz", None))
        self.fit_shape_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"Voigt", None))

        self.label_44.setText(QCoreApplication.translate("DockWidget", u"Num of Peaks", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("DockWidget", u"Fitting", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_15), QCoreApplication.translate("DockWidget", u"Output", None))
        self.label_47.setText(QCoreApplication.translate("DockWidget", u"S Layer", None))
        self.label_49.setText(QCoreApplication.translate("DockWidget", u"R.S.F.", None))
        self.label_42.setText(QCoreApplication.translate("DockWidget", u"C Layer", None))
        self.label_48.setText(QCoreApplication.translate("DockWidget", u"K.E.", None))
        self.label_41.setText(QCoreApplication.translate("DockWidget", u"Intensity", None))
        self.label_45.setText(QCoreApplication.translate("DockWidget", u"Density", None))
        self.label_43.setText(QCoreApplication.translate("DockWidget", u"EMFP", None))
        self.label_46.setText(QCoreApplication.translate("DockWidget", u"O Layer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("DockWidget", u"Thickogram", None))
    # retranslateUi

