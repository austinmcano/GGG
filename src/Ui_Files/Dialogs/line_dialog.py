# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'line_dialog.ui'
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
        Dialog.resize(400, 300)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_width_sb = QDoubleSpinBox(Dialog)
        self.line_width_sb.setObjectName(u"line_width_sb")
        self.line_width_sb.setSingleStep(0.100000000000000)
        self.line_width_sb.setValue(0.800000000000000)

        self.gridLayout.addWidget(self.line_width_sb, 2, 1, 1, 1)

        self.line_pos_sb = QDoubleSpinBox(Dialog)
        self.line_pos_sb.setObjectName(u"line_pos_sb")
        self.line_pos_sb.setMaximum(99999999.000000000000000)
        self.line_pos_sb.setValue(75.000000000000000)

        self.gridLayout.addWidget(self.line_pos_sb, 1, 1, 1, 1)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.color_cb = QComboBox(Dialog)
        self.color_cb.addItem("")
        self.color_cb.addItem("")
        self.color_cb.addItem("")
        self.color_cb.addItem("")
        self.color_cb.addItem("")
        self.color_cb.addItem("")
        self.color_cb.addItem("")
        self.color_cb.setObjectName(u"color_cb")

        self.gridLayout.addWidget(self.color_cb, 3, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Verticle Line", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Horizontal Line", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"Line Width", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Line At", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Line Color", None))
        self.color_cb.setItemText(0, QCoreApplication.translate("Dialog", u"black", None))
        self.color_cb.setItemText(1, QCoreApplication.translate("Dialog", u"red", None))
        self.color_cb.setItemText(2, QCoreApplication.translate("Dialog", u"blue", None))
        self.color_cb.setItemText(3, QCoreApplication.translate("Dialog", u"yellow", None))
        self.color_cb.setItemText(4, QCoreApplication.translate("Dialog", u"purple", None))
        self.color_cb.setItemText(5, QCoreApplication.translate("Dialog", u"orange", None))
        self.color_cb.setItemText(6, QCoreApplication.translate("Dialog", u"white", None))

    # retranslateUi

