# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spine_color_dialog.ui'
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
        Dialog.resize(338, 300)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rspine_cb = QComboBox(Dialog)
        self.rspine_cb.setObjectName(u"rspine_cb")

        self.gridLayout.addWidget(self.rspine_cb, 3, 1, 1, 1)

        self.lspine_cb = QComboBox(Dialog)
        self.lspine_cb.setObjectName(u"lspine_cb")

        self.gridLayout.addWidget(self.lspine_cb, 2, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.bspine_cb = QComboBox(Dialog)
        self.bspine_cb.setObjectName(u"bspine_cb")

        self.gridLayout.addWidget(self.bspine_cb, 0, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.tspine_cb = QComboBox(Dialog)
        self.tspine_cb.setObjectName(u"tspine_cb")

        self.gridLayout.addWidget(self.tspine_cb, 1, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Top Spine", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Left Spine", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Bottom Spine", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Right Spine", None))
    # retranslateUi

