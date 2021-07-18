# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mass_spec_line_dialog.ui'
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
        Dialog.resize(248, 265)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.m5 = QDoubleSpinBox(Dialog)
        self.m5.setObjectName(u"m5")
        self.m5.setMaximum(1000.000000000000000)

        self.gridLayout.addWidget(self.m5, 5, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.a3 = QDoubleSpinBox(Dialog)
        self.a3.setObjectName(u"a3")
        self.a3.setMaximum(100.000000000000000)

        self.gridLayout.addWidget(self.a3, 3, 2, 1, 1)

        self.a2 = QDoubleSpinBox(Dialog)
        self.a2.setObjectName(u"a2")
        self.a2.setMaximum(100.000000000000000)
        self.a2.setValue(50.000000000000000)

        self.gridLayout.addWidget(self.a2, 2, 2, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.a4 = QDoubleSpinBox(Dialog)
        self.a4.setObjectName(u"a4")
        self.a4.setMaximum(100.000000000000000)

        self.gridLayout.addWidget(self.a4, 4, 2, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.a1 = QDoubleSpinBox(Dialog)
        self.a1.setObjectName(u"a1")
        self.a1.setReadOnly(True)
        self.a1.setMinimum(100.000000000000000)
        self.a1.setMaximum(100.000000000000000)
        self.a1.setValue(100.000000000000000)

        self.gridLayout.addWidget(self.a1, 1, 2, 1, 1)

        self.m4 = QDoubleSpinBox(Dialog)
        self.m4.setObjectName(u"m4")
        self.m4.setMaximum(1000.000000000000000)
        self.m4.setValue(103.000000000000000)

        self.gridLayout.addWidget(self.m4, 4, 1, 1, 1)

        self.m1 = QDoubleSpinBox(Dialog)
        self.m1.setObjectName(u"m1")
        self.m1.setMaximum(1000.000000000000000)
        self.m1.setValue(100.000000000000000)

        self.gridLayout.addWidget(self.m1, 1, 1, 1, 1)

        self.m3 = QDoubleSpinBox(Dialog)
        self.m3.setObjectName(u"m3")
        self.m3.setMaximum(1000.000000000000000)
        self.m3.setValue(102.000000000000000)

        self.gridLayout.addWidget(self.m3, 3, 1, 1, 1)

        self.m2 = QDoubleSpinBox(Dialog)
        self.m2.setObjectName(u"m2")
        self.m2.setMaximum(1000.000000000000000)
        self.m2.setValue(101.000000000000000)

        self.gridLayout.addWidget(self.m2, 2, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 9, 1, 1, 2)

        self.a5 = QDoubleSpinBox(Dialog)
        self.a5.setObjectName(u"a5")
        self.a5.setMaximum(100.000000000000000)

        self.gridLayout.addWidget(self.a5, 5, 2, 1, 1)

        self.a7 = QDoubleSpinBox(Dialog)
        self.a7.setObjectName(u"a7")
        self.a7.setMaximum(100.000000000000000)

        self.gridLayout.addWidget(self.a7, 7, 2, 1, 1)

        self.m6 = QDoubleSpinBox(Dialog)
        self.m6.setObjectName(u"m6")
        self.m6.setMaximum(1000.000000000000000)

        self.gridLayout.addWidget(self.m6, 6, 1, 1, 1)

        self.a6 = QDoubleSpinBox(Dialog)
        self.a6.setObjectName(u"a6")
        self.a6.setMaximum(100.000000000000000)

        self.gridLayout.addWidget(self.a6, 6, 2, 1, 1)

        self.m7 = QDoubleSpinBox(Dialog)
        self.m7.setObjectName(u"m7")
        self.m7.setMaximum(1000.000000000000000)

        self.gridLayout.addWidget(self.m7, 7, 1, 1, 1)

        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)

        self.m8 = QDoubleSpinBox(Dialog)
        self.m8.setObjectName(u"m8")
        self.m8.setMaximum(1000.000000000000000)

        self.gridLayout.addWidget(self.m8, 8, 1, 1, 1)

        self.a8 = QDoubleSpinBox(Dialog)
        self.a8.setObjectName(u"a8")
        self.a8.setMaximum(100.000000000000000)

        self.gridLayout.addWidget(self.a8, 8, 2, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Mass", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"% Abundance", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"8", None))
    # retranslateUi

