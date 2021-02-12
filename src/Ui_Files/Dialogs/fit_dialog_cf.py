# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fit_dialog_cf.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(262, 246)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.a_le = QLineEdit(Dialog)
        self.a_le.setObjectName(u"a_le")

        self.gridLayout.addWidget(self.a_le, 0, 1, 1, 1)

        self.d_le = QLineEdit(Dialog)
        self.d_le.setObjectName(u"d_le")

        self.gridLayout.addWidget(self.d_le, 3, 1, 1, 1)

        self.c_le = QLineEdit(Dialog)
        self.c_le.setObjectName(u"c_le")

        self.gridLayout.addWidget(self.c_le, 2, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)

        self.b_le = QLineEdit(Dialog)
        self.b_le.setObjectName(u"b_le")

        self.gridLayout.addWidget(self.b_le, 1, 1, 1, 1)

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


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.a_le.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.d_le.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.c_le.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.b_le.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"b", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"c (if nec)", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"d (if nec)", None))
    # retranslateUi

