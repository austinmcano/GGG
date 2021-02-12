# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bargraph_dialog.ui'
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
        Dialog.resize(389, 228)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.num_sb = QSpinBox(Dialog)
        self.num_sb.setObjectName(u"num_sb")

        self.gridLayout.addWidget(self.num_sb, 0, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.y2_list = QLineEdit(Dialog)
        self.y2_list.setObjectName(u"y2_list")

        self.gridLayout.addWidget(self.y2_list, 3, 1, 1, 1)

        self.y1_list = QLineEdit(Dialog)
        self.y1_list.setObjectName(u"y1_list")

        self.gridLayout.addWidget(self.y1_list, 2, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.width_le = QLineEdit(Dialog)
        self.width_le.setObjectName(u"width_le")

        self.gridLayout.addWidget(self.width_le, 0, 3, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 4)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)

        self.label1_le = QLineEdit(Dialog)
        self.label1_le.setObjectName(u"label1_le")

        self.gridLayout.addWidget(self.label1_le, 2, 3, 1, 1)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)

        self.label2_le = QLineEdit(Dialog)
        self.label2_le.setObjectName(u"label2_le")

        self.gridLayout.addWidget(self.label2_le, 3, 3, 1, 1)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 4, 2, 1, 1)

        self.label3_le = QLineEdit(Dialog)
        self.label3_le.setObjectName(u"label3_le")

        self.gridLayout.addWidget(self.label3_le, 4, 3, 1, 1)

        self.y3_list = QLineEdit(Dialog)
        self.y3_list.setObjectName(u"y3_list")

        self.gridLayout.addWidget(self.y3_list, 4, 1, 1, 1)

        self.x_list = QLineEdit(Dialog)
        self.x_list.setObjectName(u"x_list")

        self.gridLayout.addWidget(self.x_list, 1, 1, 1, 3)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"y1", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"y3 (if nesc.)", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Number ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"X separated by \" \"", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"y2 (if nesc.)", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"width (float)", None))
        self.width_le.setText(QCoreApplication.translate("Dialog", u"0.35", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"label 1", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"label 2", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"label 3", None))
    # retranslateUi

