# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'annotation_dialog.ui'
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
        Dialog.resize(404, 301)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ha_cb = QComboBox(Dialog)
        self.ha_cb.addItem("")
        self.ha_cb.addItem("")
        self.ha_cb.addItem("")
        self.ha_cb.setObjectName(u"ha_cb")

        self.gridLayout.addWidget(self.ha_cb, 8, 3, 1, 1)

        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 8, 2, 1, 1)

        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)

        self.text_3 = QLineEdit(Dialog)
        self.text_3.setObjectName(u"text_3")

        self.gridLayout.addWidget(self.text_3, 2, 1, 1, 3)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.size = QSpinBox(Dialog)
        self.size.setObjectName(u"size")
        self.size.setValue(22)

        self.gridLayout.addWidget(self.size, 3, 1, 1, 1)

        self.alpha = QDoubleSpinBox(Dialog)
        self.alpha.setObjectName(u"alpha")
        self.alpha.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.alpha, 3, 3, 1, 1)

        self.fontstyle = QComboBox(Dialog)
        self.fontstyle.addItem("")
        self.fontstyle.addItem("")
        self.fontstyle.addItem("")
        self.fontstyle.setObjectName(u"fontstyle")

        self.gridLayout.addWidget(self.fontstyle, 8, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.frame = QComboBox(Dialog)
        self.frame.addItem("")
        self.frame.addItem("")
        self.frame.addItem("")
        self.frame.addItem("")
        self.frame.addItem("")
        self.frame.addItem("")
        self.frame.addItem("")
        self.frame.addItem("")
        self.frame.addItem("")
        self.frame.addItem("")
        self.frame.setObjectName(u"frame")

        self.gridLayout.addWidget(self.frame, 5, 3, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.framewidth_sb = QDoubleSpinBox(Dialog)
        self.framewidth_sb.setObjectName(u"framewidth_sb")
        self.framewidth_sb.setValue(2.000000000000000)

        self.gridLayout.addWidget(self.framewidth_sb, 6, 1, 1, 1)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)

        self.color = QComboBox(Dialog)
        self.color.setObjectName(u"color")

        self.gridLayout.addWidget(self.color, 4, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 5, 2, 1, 1)

        self.text = QLineEdit(Dialog)
        self.text.setObjectName(u"text")

        self.gridLayout.addWidget(self.text, 0, 1, 1, 3)

        self.framecolor = QComboBox(Dialog)
        self.framecolor.setObjectName(u"framecolor")

        self.gridLayout.addWidget(self.framecolor, 5, 1, 1, 1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 2, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.rotation = QDoubleSpinBox(Dialog)
        self.rotation.setObjectName(u"rotation")
        self.rotation.setMaximum(360.000000000000000)
        self.rotation.setSingleStep(45.000000000000000)

        self.gridLayout.addWidget(self.rotation, 6, 3, 1, 1)

        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 6, 2, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 2, 1, 1)

        self.bgcolor = QComboBox(Dialog)
        self.bgcolor.setObjectName(u"bgcolor")

        self.gridLayout.addWidget(self.bgcolor, 4, 3, 1, 1)

        self.text_2 = QLineEdit(Dialog)
        self.text_2.setObjectName(u"text_2")

        self.gridLayout.addWidget(self.text_2, 1, 1, 1, 3)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 10, 2, 1, 2)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 10, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.ha_cb.setItemText(0, QCoreApplication.translate("Dialog", u"center", None))
        self.ha_cb.setItemText(1, QCoreApplication.translate("Dialog", u"left", None))
        self.ha_cb.setItemText(2, QCoreApplication.translate("Dialog", u"right", None))

        self.label_13.setText(QCoreApplication.translate("Dialog", u"Horz. Align", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Text Line 3", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Size", None))
        self.fontstyle.setItemText(0, QCoreApplication.translate("Dialog", u"normal", None))
        self.fontstyle.setItemText(1, QCoreApplication.translate("Dialog", u"italic", None))
        self.fontstyle.setItemText(2, QCoreApplication.translate("Dialog", u"oblique", None))

        self.label_3.setText(QCoreApplication.translate("Dialog", u"Text Line 1", None))
        self.frame.setItemText(0, QCoreApplication.translate("Dialog", u"none", None))
        self.frame.setItemText(1, QCoreApplication.translate("Dialog", u"darrow", None))
        self.frame.setItemText(2, QCoreApplication.translate("Dialog", u"circle", None))
        self.frame.setItemText(3, QCoreApplication.translate("Dialog", u"larrow", None))
        self.frame.setItemText(4, QCoreApplication.translate("Dialog", u"rarrow", None))
        self.frame.setItemText(5, QCoreApplication.translate("Dialog", u"round", None))
        self.frame.setItemText(6, QCoreApplication.translate("Dialog", u"round4", None))
        self.frame.setItemText(7, QCoreApplication.translate("Dialog", u"roundtooth", None))
        self.frame.setItemText(8, QCoreApplication.translate("Dialog", u"sawtooth", None))
        self.frame.setItemText(9, QCoreApplication.translate("Dialog", u"square", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"Frame Width", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Font Style", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Color", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Frame", None))
        self.text.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Alpha", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Frame Edge Color", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Rotation", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"BG color", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Text Line 2", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"\u00b0C", None))
    # retranslateUi

