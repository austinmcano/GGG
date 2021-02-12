# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'annotation_dialog.ui'
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
        Dialog.resize(404, 301)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 1)

        self.dragable_cb = QComboBox(Dialog)
        self.dragable_cb.addItem("")
        self.dragable_cb.addItem("")
        self.dragable_cb.setObjectName(u"dragable_cb")

        self.gridLayout.addWidget(self.dragable_cb, 3, 1, 1, 1)

        self.size_sb = QSpinBox(Dialog)
        self.size_sb.setObjectName(u"size_sb")

        self.gridLayout.addWidget(self.size_sb, 1, 1, 1, 1)

        self.frame_cb = QComboBox(Dialog)
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.setObjectName(u"frame_cb")

        self.gridLayout.addWidget(self.frame_cb, 2, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.text_le = QLineEdit(Dialog)
        self.text_le.setObjectName(u"text_le")

        self.gridLayout.addWidget(self.text_le, 0, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Frame", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Draggable", None))
        self.dragable_cb.setItemText(0, QCoreApplication.translate("Dialog", u"Yes", None))
        self.dragable_cb.setItemText(1, QCoreApplication.translate("Dialog", u"No", None))

        self.frame_cb.setItemText(0, QCoreApplication.translate("Dialog", u"No Frame", None))
        self.frame_cb.setItemText(1, QCoreApplication.translate("Dialog", u"Box", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Size", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Text", None))
    # retranslateUi

