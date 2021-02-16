# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'axis_setup_dialog.ui'
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
        Dialog.resize(265, 205)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.axis1_cb = QComboBox(Dialog)
        self.axis1_cb.addItem("")
        self.axis1_cb.setObjectName(u"axis1_cb")

        self.gridLayout.addWidget(self.axis1_cb, 0, 1, 1, 1)

        self.axis2_cb = QComboBox(Dialog)
        self.axis2_cb.addItem("")
        self.axis2_cb.addItem("")
        self.axis2_cb.setObjectName(u"axis2_cb")

        self.gridLayout.addWidget(self.axis2_cb, 1, 1, 1, 1)

        self.axis3_cb = QComboBox(Dialog)
        self.axis3_cb.addItem("")
        self.axis3_cb.addItem("")
        self.axis3_cb.setObjectName(u"axis3_cb")

        self.gridLayout.addWidget(self.axis3_cb, 2, 1, 1, 1)

        self.axis4_cb = QComboBox(Dialog)
        self.axis4_cb.addItem("")
        self.axis4_cb.addItem("")
        self.axis4_cb.setObjectName(u"axis4_cb")

        self.gridLayout.addWidget(self.axis4_cb, 3, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Axis 1", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Axis 2", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Axis 3", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Axis 4", None))
        self.axis1_cb.setItemText(0, QCoreApplication.translate("Dialog", u"ON", None))

        self.axis2_cb.setItemText(0, QCoreApplication.translate("Dialog", u"OFF", None))
        self.axis2_cb.setItemText(1, QCoreApplication.translate("Dialog", u"ON", None))

        self.axis3_cb.setItemText(0, QCoreApplication.translate("Dialog", u"OFF", None))
        self.axis3_cb.setItemText(1, QCoreApplication.translate("Dialog", u"ON", None))

        self.axis4_cb.setItemText(0, QCoreApplication.translate("Dialog", u"OFF", None))
        self.axis4_cb.setItemText(1, QCoreApplication.translate("Dialog", u"ON", None))

    # retranslateUi

