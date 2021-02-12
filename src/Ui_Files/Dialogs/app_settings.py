# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(636, 505)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 11, 0, 1, 3)

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_3.addWidget(self.textBrowser, 1, 1, 1, 1)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)

        self.spinBox = QSpinBox(self.tab_2)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_3.addWidget(self.spinBox, 2, 1, 1, 1)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.tab_2)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 8, 0, 1, 1)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 7, 0, 1, 1)

        self.change_figpath_pb = QPushButton(self.tab)
        self.change_figpath_pb.setObjectName(u"change_figpath_pb")

        self.gridLayout_2.addWidget(self.change_figpath_pb, 3, 2, 1, 1)

        self.change_qcm_pb = QPushButton(self.tab)
        self.change_qcm_pb.setObjectName(u"change_qcm_pb")

        self.gridLayout_2.addWidget(self.change_qcm_pb, 5, 2, 1, 1)

        self.change_cf_pb = QPushButton(self.tab)
        self.change_cf_pb.setObjectName(u"change_cf_pb")

        self.gridLayout_2.addWidget(self.change_cf_pb, 8, 2, 1, 1)

        self.xps_path_label = QLabel(self.tab)
        self.xps_path_label.setObjectName(u"xps_path_label")

        self.gridLayout_2.addWidget(self.xps_path_label, 7, 1, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.se_path_label = QLabel(self.tab)
        self.se_path_label.setObjectName(u"se_path_label")

        self.gridLayout_2.addWidget(self.se_path_label, 6, 1, 1, 1)

        self.change_se_pb = QPushButton(self.tab)
        self.change_se_pb.setObjectName(u"change_se_pb")

        self.gridLayout_2.addWidget(self.change_se_pb, 6, 2, 1, 1)

        self.changesavepath_pb = QPushButton(self.tab)
        self.changesavepath_pb.setObjectName(u"changesavepath_pb")

        self.gridLayout_2.addWidget(self.changesavepath_pb, 2, 2, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)

        self.changeprojectpath_pb = QPushButton(self.tab)
        self.changeprojectpath_pb.setObjectName(u"changeprojectpath_pb")

        self.gridLayout_2.addWidget(self.changeprojectpath_pb, 0, 2, 1, 1)

        self.change_ir_pb = QPushButton(self.tab)
        self.change_ir_pb.setObjectName(u"change_ir_pb")

        self.gridLayout_2.addWidget(self.change_ir_pb, 4, 2, 1, 1)

        self.changedatapath_pb = QPushButton(self.tab)
        self.changedatapath_pb.setObjectName(u"changedatapath_pb")

        self.gridLayout_2.addWidget(self.changedatapath_pb, 1, 2, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.datapath_le = QLabel(self.tab)
        self.datapath_le.setObjectName(u"datapath_le")

        self.gridLayout_2.addWidget(self.datapath_le, 1, 1, 1, 1)

        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)

        self.fig_path_label = QLabel(self.tab)
        self.fig_path_label.setObjectName(u"fig_path_label")

        self.gridLayout_2.addWidget(self.fig_path_label, 3, 1, 1, 1)

        self.projectpath_le = QLabel(self.tab)
        self.projectpath_le.setObjectName(u"projectpath_le")

        self.gridLayout_2.addWidget(self.projectpath_le, 0, 1, 1, 1)

        self.qcm_path_label = QLabel(self.tab)
        self.qcm_path_label.setObjectName(u"qcm_path_label")

        self.gridLayout_2.addWidget(self.qcm_path_label, 5, 1, 1, 1)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.savepath_le = QLabel(self.tab)
        self.savepath_le.setObjectName(u"savepath_le")

        self.gridLayout_2.addWidget(self.savepath_le, 2, 1, 1, 1)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)

        self.cf_path_label = QLabel(self.tab)
        self.cf_path_label.setObjectName(u"cf_path_label")

        self.gridLayout_2.addWidget(self.cf_path_label, 8, 1, 1, 1)

        self.change_xps_pb = QPushButton(self.tab)
        self.change_xps_pb.setObjectName(u"change_xps_pb")

        self.gridLayout_2.addWidget(self.change_xps_pb, 7, 2, 1, 1)

        self.ftir_path_label = QLabel(self.tab)
        self.ftir_path_label.setObjectName(u"ftir_path_label")

        self.gridLayout_2.addWidget(self.ftir_path_label, 4, 1, 1, 1)

        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 9, 0, 1, 1)

        self.xrd_path_label = QLabel(self.tab)
        self.xrd_path_label.setObjectName(u"xrd_path_label")

        self.gridLayout_2.addWidget(self.xrd_path_label, 9, 1, 1, 1)

        self.changexrdpath_pb = QPushButton(self.tab)
        self.changexrdpath_pb.setObjectName(u"changexrdpath_pb")

        self.gridLayout_2.addWidget(self.changexrdpath_pb, 9, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 3)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.SF NS Text'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">Warning</span>: Changing the App Style will instantly restart the app. </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Only do this if you are prepared to lose anything curing going on</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in the program right now.</p></body><"
                        "/html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Maker Size", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"App Style", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"App Settings", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Curve Fit Path", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"XPS Path", None))
        self.change_figpath_pb.setText(QCoreApplication.translate("Dialog", u"Change", None))
        self.change_qcm_pb.setText(QCoreApplication.translate("Dialog", u"Change", None))
        self.change_cf_pb.setText(QCoreApplication.translate("Dialog", u"Change", None))
        self.xps_path_label.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"ProjectPath", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"DataPath", None))
        self.se_path_label.setText("")
        self.change_se_pb.setText(QCoreApplication.translate("Dialog", u"Change", None))
        self.changesavepath_pb.setText(QCoreApplication.translate("Dialog", u"Change", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"QCM Path", None))
        self.changeprojectpath_pb.setText(QCoreApplication.translate("Dialog", u"Change", None))
        self.change_ir_pb.setText(QCoreApplication.translate("Dialog", u"Change", None))
        self.changedatapath_pb.setText(QCoreApplication.translate("Dialog", u"Change", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"FTIR Path", None))
        self.datapath_le.setText("")
        self.label_11.setText(QCoreApplication.translate("Dialog", u"FigPath", None))
        self.fig_path_label.setText("")
        self.projectpath_le.setText("")
        self.qcm_path_label.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"SavePath", None))
        self.savepath_le.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"SE Path", None))
        self.cf_path_label.setText("")
        self.change_xps_pb.setText(QCoreApplication.translate("Dialog", u"Change", None))
        self.ftir_path_label.setText("")
        self.label_12.setText(QCoreApplication.translate("Dialog", u"XRD Path", None))
        self.xrd_path_label.setText("")
        self.changexrdpath_pb.setText(QCoreApplication.translate("Dialog", u"Change", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Change Paths", None))
    # retranslateUi

