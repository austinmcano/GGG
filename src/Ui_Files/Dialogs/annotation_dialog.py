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
        self.frame_cb = QComboBox(Dialog)
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.addItem("")
        self.frame_cb.setObjectName(u"frame_cb")

        self.gridLayout.addWidget(self.frame_cb, 2, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.size_sb = QSpinBox(Dialog)
        self.size_sb.setObjectName(u"size_sb")
        self.size_sb.setValue(18)

        self.gridLayout.addWidget(self.size_sb, 1, 1, 1, 1)

        self.framecolor_cb = QComboBox(Dialog)
        self.framecolor_cb.addItem("")
        self.framecolor_cb.addItem("")
        self.framecolor_cb.addItem("")
        self.framecolor_cb.addItem("")
        self.framecolor_cb.addItem("")
        self.framecolor_cb.addItem("")
        self.framecolor_cb.addItem("")
        self.framecolor_cb.addItem("")
        self.framecolor_cb.setObjectName(u"framecolor_cb")

        self.gridLayout.addWidget(self.framecolor_cb, 3, 1, 1, 1)

        self.framewidth_sb = QDoubleSpinBox(Dialog)
        self.framewidth_sb.setObjectName(u"framewidth_sb")
        self.framewidth_sb.setValue(2.000000000000000)

        self.gridLayout.addWidget(self.framewidth_sb, 4, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 7, 1, 1, 1)

        self.text_le = QLineEdit(Dialog)
        self.text_le.setObjectName(u"text_le")

        self.gridLayout.addWidget(self.text_le, 0, 1, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.framebgcolor_cb = QComboBox(Dialog)
        self.framebgcolor_cb.addItem("")
        self.framebgcolor_cb.addItem("")
        self.framebgcolor_cb.addItem("")
        self.framebgcolor_cb.addItem("")
        self.framebgcolor_cb.addItem("")
        self.framebgcolor_cb.addItem("")
        self.framebgcolor_cb.addItem("")
        self.framebgcolor_cb.setObjectName(u"framebgcolor_cb")

        self.gridLayout.addWidget(self.framebgcolor_cb, 5, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.frame_cb.setItemText(0, QCoreApplication.translate("Dialog", u"No Frame", None))
        self.frame_cb.setItemText(1, QCoreApplication.translate("Dialog", u"darrow", None))
        self.frame_cb.setItemText(2, QCoreApplication.translate("Dialog", u"circle", None))
        self.frame_cb.setItemText(3, QCoreApplication.translate("Dialog", u"larrow", None))
        self.frame_cb.setItemText(4, QCoreApplication.translate("Dialog", u"rarrow", None))
        self.frame_cb.setItemText(5, QCoreApplication.translate("Dialog", u"round", None))
        self.frame_cb.setItemText(6, QCoreApplication.translate("Dialog", u"round4", None))
        self.frame_cb.setItemText(7, QCoreApplication.translate("Dialog", u"roundtooth", None))
        self.frame_cb.setItemText(8, QCoreApplication.translate("Dialog", u"sawtooth", None))
        self.frame_cb.setItemText(9, QCoreApplication.translate("Dialog", u"square", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Size", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Frame Width", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Text", None))
        self.framecolor_cb.setItemText(0, QCoreApplication.translate("Dialog", u"k", None))
        self.framecolor_cb.setItemText(1, QCoreApplication.translate("Dialog", u"r", None))
        self.framecolor_cb.setItemText(2, QCoreApplication.translate("Dialog", u"g", None))
        self.framecolor_cb.setItemText(3, QCoreApplication.translate("Dialog", u"w", None))
        self.framecolor_cb.setItemText(4, QCoreApplication.translate("Dialog", u"c", None))
        self.framecolor_cb.setItemText(5, QCoreApplication.translate("Dialog", u"m", None))
        self.framecolor_cb.setItemText(6, QCoreApplication.translate("Dialog", u"y", None))
        self.framecolor_cb.setItemText(7, QCoreApplication.translate("Dialog", u"b", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"Frame", None))
        self.text_le.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Frame Color", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Frame Background Color", None))
        self.framebgcolor_cb.setItemText(0, QCoreApplication.translate("Dialog", u"white", None))
        self.framebgcolor_cb.setItemText(1, QCoreApplication.translate("Dialog", u"purple", None))
        self.framebgcolor_cb.setItemText(2, QCoreApplication.translate("Dialog", u"green", None))
        self.framebgcolor_cb.setItemText(3, QCoreApplication.translate("Dialog", u"red", None))
        self.framebgcolor_cb.setItemText(4, QCoreApplication.translate("Dialog", u"yellow", None))
        self.framebgcolor_cb.setItemText(5, QCoreApplication.translate("Dialog", u"blue", None))
        self.framebgcolor_cb.setItemText(6, QCoreApplication.translate("Dialog", u"black", None))

    # retranslateUi

