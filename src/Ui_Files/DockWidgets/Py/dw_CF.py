# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_CF.ui'
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
        DockWidget.resize(476, 527)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.function_cb = QComboBox(self.dockWidgetContents)
        self.function_cb.setObjectName(u"function_cb")

        self.gridLayout.addWidget(self.function_cb, 6, 3, 1, 1)

        self.addx_pb = QPushButton(self.dockWidgetContents)
        self.addx_pb.setObjectName(u"addx_pb")
        self.addx_pb.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.addx_pb, 5, 1, 1, 1)

        self.label_2 = QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 20))

        self.gridLayout.addWidget(self.label_2, 5, 2, 1, 1)

        self.y_sb = QSpinBox(self.dockWidgetContents)
        self.y_sb.setObjectName(u"y_sb")
        self.y_sb.setMaximumSize(QSize(200, 16777215))
        self.y_sb.setMinimum(1)
        self.y_sb.setMaximum(999)

        self.gridLayout.addWidget(self.y_sb, 5, 3, 1, 1)

        self.fit_data_pb = QPushButton(self.dockWidgetContents)
        self.fit_data_pb.setObjectName(u"fit_data_pb")

        self.gridLayout.addWidget(self.fit_data_pb, 6, 2, 1, 1)

        self.plot_pb = QPushButton(self.dockWidgetContents)
        self.plot_pb.setObjectName(u"plot_pb")
        self.plot_pb.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.plot_pb, 6, 1, 1, 1)

        self.function_label = QLabel(self.dockWidgetContents)
        self.function_label.setObjectName(u"function_label")

        self.gridLayout.addWidget(self.function_label, 7, 1, 1, 3)

        self.import_pb = QPushButton(self.dockWidgetContents)
        self.import_pb.setObjectName(u"import_pb")

        self.gridLayout.addWidget(self.import_pb, 6, 0, 1, 1)

        self.tableWidget = QTableWidget(self.dockWidgetContents)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)

        self.gridLayout.addWidget(self.tableWidget, 2, 0, 3, 4)

        self.treeView = QTreeView(self.dockWidgetContents)
        self.treeView.setObjectName(u"treeView")

        self.gridLayout.addWidget(self.treeView, 0, 0, 2, 4)

        self.results_te = QTextEdit(self.dockWidgetContents)
        self.results_te.setObjectName(u"results_te")

        self.gridLayout.addWidget(self.results_te, 10, 0, 1, 4)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"Curve Fitting", None))
        self.addx_pb.setText(QCoreApplication.translate("DockWidget", u"add x values", None))
        self.label_2.setText(QCoreApplication.translate("DockWidget", u"row length", None))
        self.fit_data_pb.setText(QCoreApplication.translate("DockWidget", u"Fit Data", None))
        self.plot_pb.setText(QCoreApplication.translate("DockWidget", u"plot data", None))
        self.function_label.setText("")
        self.import_pb.setText(QCoreApplication.translate("DockWidget", u"Import", None))
    # retranslateUi

