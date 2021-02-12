# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seaborn_settings.ui'
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
        Dialog.resize(297, 289)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.style_cb = QComboBox(Dialog)
        self.style_cb.addItem("")
        self.style_cb.addItem("")
        self.style_cb.addItem("")
        self.style_cb.addItem("")
        self.style_cb.addItem("")
        self.style_cb.setObjectName(u"style_cb")

        self.gridLayout.addWidget(self.style_cb, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 7, 1, 1, 1)

        self.palette_cb = QComboBox(Dialog)
        self.palette_cb.setObjectName(u"palette_cb")

        self.gridLayout.addWidget(self.palette_cb, 4, 1, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.context_cb = QComboBox(Dialog)
        self.context_cb.addItem("")
        self.context_cb.addItem("")
        self.context_cb.addItem("")
        self.context_cb.addItem("")
        self.context_cb.setObjectName(u"context_cb")

        self.gridLayout.addWidget(self.context_cb, 1, 1, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.fonts_cb = QComboBox(Dialog)
        self.fonts_cb.setObjectName(u"fonts_cb")

        self.gridLayout.addWidget(self.fonts_cb, 2, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.fontscale_sb = QSpinBox(Dialog)
        self.fontscale_sb.setObjectName(u"fontscale_sb")
        self.fontscale_sb.setMinimum(1)
        self.fontscale_sb.setMaximum(10)

        self.gridLayout.addWidget(self.fontscale_sb, 3, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.axes_facecolor_le = QLineEdit(Dialog)
        self.axes_facecolor_le.setObjectName(u"axes_facecolor_le")

        self.gridLayout.addWidget(self.axes_facecolor_le, 5, 1, 1, 1)

        self.fig_facecolor_le = QLineEdit(Dialog)
        self.fig_facecolor_le.setObjectName(u"fig_facecolor_le")

        self.gridLayout.addWidget(self.fig_facecolor_le, 6, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.style_cb.setItemText(0, QCoreApplication.translate("Dialog", u"white", None))
        self.style_cb.setItemText(1, QCoreApplication.translate("Dialog", u"dark", None))
        self.style_cb.setItemText(2, QCoreApplication.translate("Dialog", u"whitegrid", None))
        self.style_cb.setItemText(3, QCoreApplication.translate("Dialog", u"darkgrid", None))
        self.style_cb.setItemText(4, QCoreApplication.translate("Dialog", u"ticks", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"Palette", None))
        self.context_cb.setItemText(0, QCoreApplication.translate("Dialog", u"notebook", None))
        self.context_cb.setItemText(1, QCoreApplication.translate("Dialog", u"paper", None))
        self.context_cb.setItemText(2, QCoreApplication.translate("Dialog", u"poster", None))
        self.context_cb.setItemText(3, QCoreApplication.translate("Dialog", u"talk", None))

        self.label_6.setText(QCoreApplication.translate("Dialog", u"Axes Facecolor", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Style", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Context", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Font Scale", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Fonts", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Figure Facecolor", None))
    # retranslateUi

