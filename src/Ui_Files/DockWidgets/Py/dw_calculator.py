# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_calculator.ui'
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


class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(329, 248)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb5 = QPushButton(self.dockWidgetContents)
        self.pb5.setObjectName(u"pb5")

        self.gridLayout.addWidget(self.pb5, 3, 1, 1, 1)

        self.pb6 = QPushButton(self.dockWidgetContents)
        self.pb6.setObjectName(u"pb6")

        self.gridLayout.addWidget(self.pb6, 3, 2, 1, 1)

        self.pb3 = QPushButton(self.dockWidgetContents)
        self.pb3.setObjectName(u"pb3")

        self.gridLayout.addWidget(self.pb3, 2, 2, 1, 1)

        self.lineEdit = QLineEdit(self.dockWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 4)

        self.pb9 = QPushButton(self.dockWidgetContents)
        self.pb9.setObjectName(u"pb9")

        self.gridLayout.addWidget(self.pb9, 4, 2, 1, 1)

        self.pb_point = QPushButton(self.dockWidgetContents)
        self.pb_point.setObjectName(u"pb_point")

        self.gridLayout.addWidget(self.pb_point, 5, 2, 1, 1)

        self.pb8 = QPushButton(self.dockWidgetContents)
        self.pb8.setObjectName(u"pb8")

        self.gridLayout.addWidget(self.pb8, 4, 1, 1, 1)

        self.pb7 = QPushButton(self.dockWidgetContents)
        self.pb7.setObjectName(u"pb7")

        self.gridLayout.addWidget(self.pb7, 4, 0, 1, 1)

        self.pb0 = QPushButton(self.dockWidgetContents)
        self.pb0.setObjectName(u"pb0")

        self.gridLayout.addWidget(self.pb0, 5, 1, 1, 1)

        self.pb1 = QPushButton(self.dockWidgetContents)
        self.pb1.setObjectName(u"pb1")

        self.gridLayout.addWidget(self.pb1, 2, 0, 1, 1)

        self.pb_pos_neg = QPushButton(self.dockWidgetContents)
        self.pb_pos_neg.setObjectName(u"pb_pos_neg")

        self.gridLayout.addWidget(self.pb_pos_neg, 5, 0, 1, 1)

        self.pb2 = QPushButton(self.dockWidgetContents)
        self.pb2.setObjectName(u"pb2")

        self.gridLayout.addWidget(self.pb2, 2, 1, 1, 1)

        self.pb4 = QPushButton(self.dockWidgetContents)
        self.pb4.setObjectName(u"pb4")

        self.gridLayout.addWidget(self.pb4, 3, 0, 1, 1)

        self.pb_clear = QPushButton(self.dockWidgetContents)
        self.pb_clear.setObjectName(u"pb_clear")

        self.gridLayout.addWidget(self.pb_clear, 1, 0, 1, 1)

        self.pb_delete = QPushButton(self.dockWidgetContents)
        self.pb_delete.setObjectName(u"pb_delete")

        self.gridLayout.addWidget(self.pb_delete, 1, 1, 1, 1)

        self.pb_times = QPushButton(self.dockWidgetContents)
        self.pb_times.setObjectName(u"pb_times")

        self.gridLayout.addWidget(self.pb_times, 1, 3, 1, 1)

        self.pb_divide = QPushButton(self.dockWidgetContents)
        self.pb_divide.setObjectName(u"pb_divide")

        self.gridLayout.addWidget(self.pb_divide, 2, 3, 1, 1)

        self.pb_minus = QPushButton(self.dockWidgetContents)
        self.pb_minus.setObjectName(u"pb_minus")

        self.gridLayout.addWidget(self.pb_minus, 3, 3, 1, 1)

        self.pb_plus = QPushButton(self.dockWidgetContents)
        self.pb_plus.setObjectName(u"pb_plus")

        self.gridLayout.addWidget(self.pb_plus, 4, 3, 1, 1)

        self.pb_equal = QPushButton(self.dockWidgetContents)
        self.pb_equal.setObjectName(u"pb_equal")

        self.gridLayout.addWidget(self.pb_equal, 5, 3, 1, 1)

        self.pb_square = QPushButton(self.dockWidgetContents)
        self.pb_square.setObjectName(u"pb_square")

        self.gridLayout.addWidget(self.pb_square, 1, 2, 1, 1)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"DockWidget", None))
        self.pb5.setText(QCoreApplication.translate("DockWidget", u"5", None))
        self.pb6.setText(QCoreApplication.translate("DockWidget", u"6", None))
        self.pb3.setText(QCoreApplication.translate("DockWidget", u"3", None))
        self.pb9.setText(QCoreApplication.translate("DockWidget", u"9", None))
        self.pb_point.setText(QCoreApplication.translate("DockWidget", u".", None))
        self.pb8.setText(QCoreApplication.translate("DockWidget", u"8", None))
        self.pb7.setText(QCoreApplication.translate("DockWidget", u"7", None))
        self.pb0.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.pb1.setText(QCoreApplication.translate("DockWidget", u"1", None))
        self.pb_pos_neg.setText(QCoreApplication.translate("DockWidget", u"+/-", None))
        self.pb2.setText(QCoreApplication.translate("DockWidget", u"2", None))
        self.pb4.setText(QCoreApplication.translate("DockWidget", u"4", None))
        self.pb_clear.setText(QCoreApplication.translate("DockWidget", u"Clear", None))
        self.pb_delete.setText(QCoreApplication.translate("DockWidget", u"Delete", None))
        self.pb_times.setText(QCoreApplication.translate("DockWidget", u"*", None))
        self.pb_divide.setText(QCoreApplication.translate("DockWidget", u"/", None))
        self.pb_minus.setText(QCoreApplication.translate("DockWidget", u"-", None))
        self.pb_plus.setText(QCoreApplication.translate("DockWidget", u"+", None))
        self.pb_equal.setText(QCoreApplication.translate("DockWidget", u"=", None))
        self.pb_square.setText(QCoreApplication.translate("DockWidget", u"x^2", None))
    # retranslateUi

