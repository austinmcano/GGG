# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plot_dialog.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(563, 627)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 4, 1, 1, 1)

        self.treeWidget = QTreeWidget(Dialog)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMaximumSize(QSize(16777215, 175))

        self.gridLayout_2.addWidget(self.treeWidget, 1, 0, 1, 1)

        self.treeWidget_2 = QTreeWidget(Dialog)
        self.treeWidget_2.setObjectName(u"treeWidget_2")
        self.treeWidget_2.setMaximumSize(QSize(16777215, 175))

        self.gridLayout_2.addWidget(self.treeWidget_2, 1, 1, 1, 1)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.x_label = QLineEdit(self.tab_2)
        self.x_label.setObjectName(u"x_label")

        self.gridLayout_3.addWidget(self.x_label, 0, 1, 1, 1)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 3, 0, 1, 1)

        self.y_label = QLineEdit(self.tab_2)
        self.y_label.setObjectName(u"y_label")

        self.gridLayout_3.addWidget(self.y_label, 2, 1, 1, 1)

        self.skip_rows_num = QTextEdit(self.tab_2)
        self.skip_rows_num.setObjectName(u"skip_rows_num")
        self.skip_rows_num.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_3.addWidget(self.skip_rows_num, 3, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.From_Time = QLineEdit(self.tab_3)
        self.From_Time.setObjectName(u"From_Time")

        self.gridLayout_4.addWidget(self.From_Time, 6, 1, 1, 1)

        self.Num_A = QLineEdit(self.tab_3)
        self.Num_A.setObjectName(u"Num_A")

        self.gridLayout_4.addWidget(self.Num_A, 2, 1, 1, 1)

        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 6, 0, 1, 1)

        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.treeWidget_QCM = QTreeWidget(self.tab_3)
        QTreeWidgetItem(self.treeWidget_QCM)
        QTreeWidgetItem(self.treeWidget_QCM)
        QTreeWidgetItem(self.treeWidget_QCM)
        QTreeWidgetItem(self.treeWidget_QCM)
        QTreeWidgetItem(self.treeWidget_QCM)
        self.treeWidget_QCM.setObjectName(u"treeWidget_QCM")
        self.treeWidget_QCM.setMaximumSize(QSize(16777215, 125))

        self.gridLayout_4.addWidget(self.treeWidget_QCM, 0, 0, 1, 2)

        self.treeWidget_pressure = QTreeWidget(self.tab_3)
        self.treeWidget_pressure.setObjectName(u"treeWidget_pressure")
        self.treeWidget_pressure.setMaximumSize(QSize(16777215, 125))

        self.gridLayout_4.addWidget(self.treeWidget_pressure, 0, 2, 1, 2)

        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 4, 2, 1, 1)

        self.P_Threshold = QLineEdit(self.tab_3)
        self.P_Threshold.setObjectName(u"P_Threshold")

        self.gridLayout_4.addWidget(self.P_Threshold, 4, 1, 1, 1)

        self.time_through_purge = QLineEdit(self.tab_3)
        self.time_through_purge.setObjectName(u"time_through_purge")

        self.gridLayout_4.addWidget(self.time_through_purge, 4, 3, 1, 1)

        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 6, 2, 1, 1)

        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 4, 0, 1, 1)

        self.To_Time = QLineEdit(self.tab_3)
        self.To_Time.setObjectName(u"To_Time")

        self.gridLayout_4.addWidget(self.To_Time, 6, 3, 1, 1)

        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 2, 2, 1, 1)

        self.Num_B = QLineEdit(self.tab_3)
        self.Num_B.setObjectName(u"Num_B")

        self.gridLayout_4.addWidget(self.Num_B, 2, 3, 1, 1)

        self.wait_LE = QLineEdit(self.tab_3)
        self.wait_LE.setObjectName(u"wait_LE")

        self.gridLayout_4.addWidget(self.wait_LE, 7, 1, 1, 1)

        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 7, 0, 1, 1)

        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 7, 2, 1, 1)

        self.lineEdit = QLineEdit(self.tab_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 7, 3, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 1)

        self.horizontalSlider_3 = QSlider(self.tab)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_3, 6, 1, 1, 2)

        self.horizontalSlider_2 = QSlider(self.tab)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_2, 5, 1, 1, 2)

        self.label_16 = QLabel(self.tab)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 5, 3, 1, 1)

        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)

        self.horizontalSlider = QSlider(self.tab)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider, 4, 1, 1, 2)

        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)

        self.radioButton_3 = QRadioButton(self.tab)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout.addWidget(self.radioButton_3, 1, 2, 1, 1)

        self.label_15 = QLabel(self.tab)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 6, 3, 1, 1)

        self.label_18 = QLabel(self.tab)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 50))

        self.gridLayout.addWidget(self.label_18, 7, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.tab)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 1, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lineEdit_2, 8, 0, 1, 1)

        self.label_19 = QLabel(self.tab)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 7, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lineEdit_3, 8, 1, 1, 1)

        self.radioButton = QRadioButton(self.tab)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)

        self.label_17 = QLabel(self.tab)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 4, 3, 1, 1)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 4, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")

        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 2, 2)

        self.QP_pushbutton = QPushButton(Dialog)
        self.QP_pushbutton.setObjectName(u"QP_pushbutton")

        self.gridLayout_2.addWidget(self.QP_pushbutton, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Dialog", u"X Axes", None));
        ___qtreewidgetitem1 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Dialog", u"Y Axes", None));
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Plot", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"QCM", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"XPS", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"X Axis Label", None))
        self.x_label.setText(QCoreApplication.translate("Dialog", u"Wavenumber (cm$^{-1}$)", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Y Axis Label", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Skip Rows Number", None))
        self.y_label.setText(QCoreApplication.translate("Dialog", u"Absorbance", None))
        self.skip_rows_num.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.SF NS Text'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Plot", None))
        self.From_Time.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.Num_A.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"From Time", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"# of A Exposures", None))
        ___qtreewidgetitem2 = self.treeWidget_QCM.headerItem()
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Dialog", u"QCM Functions", None));

        __sortingEnabled = self.treeWidget_QCM.isSortingEnabled()
        self.treeWidget_QCM.setSortingEnabled(False)
        ___qtreewidgetitem3 = self.treeWidget_QCM.topLevelItem(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Dialog", u"Half Cycle Change", None));
        ___qtreewidgetitem4 = self.treeWidget_QCM.topLevelItem(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("Dialog", u"Full Cycle Change", None));
        ___qtreewidgetitem5 = self.treeWidget_QCM.topLevelItem(2)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("Dialog", u"QCM Mass Subtract From First", None));
        ___qtreewidgetitem6 = self.treeWidget_QCM.topLevelItem(3)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("Dialog", u"Plot Mass+Pressure", None));
        ___qtreewidgetitem7 = self.treeWidget_QCM.topLevelItem(4)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("Dialog", u"Density-Half Cycle", None));
        self.treeWidget_QCM.setSortingEnabled(__sortingEnabled)

        ___qtreewidgetitem8 = self.treeWidget_pressure.headerItem()
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("Dialog", u"Pressure (Time is X and Mass is Y)", None));
        self.label_5.setText(QCoreApplication.translate("Dialog", u"% Time through Purge", None))
        self.P_Threshold.setText(QCoreApplication.translate("Dialog", u"0.05", None))
        self.time_through_purge.setText(QCoreApplication.translate("Dialog", u".88", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"To Time", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"P. Threshold ", None))
        self.To_Time.setText(QCoreApplication.translate("Dialog", u"9999999", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"# of B Exposures", None))
        self.Num_B.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.wait_LE.setText(QCoreApplication.translate("Dialog", u"29", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Wait Time", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Density (g/cm3)", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"QCM", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Peak Position", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"FWHM", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Amplitude", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Peak 3", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Fit From", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Peak 2", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Dialog", u"270", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Fit To", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Dialog", u"295", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Peak 1", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Try Fit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"XPS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Dialog", u"SE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Dialog", u"QMS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Dialog", u"FTIR", None))
        self.QP_pushbutton.setText(QCoreApplication.translate("Dialog", u"Quick Plot", None))
    # retranslateUi

