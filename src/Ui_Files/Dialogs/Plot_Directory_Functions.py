# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Plot_Directory_Functions.ui'
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
        Dialog.resize(449, 362)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Dir_Functions = QTabWidget(Dialog)
        self.Dir_Functions.setObjectName(u"Dir_Functions")
        self.tab_QCM = QWidget()
        self.tab_QCM.setObjectName(u"tab_QCM")
        self.gridLayout_2 = QGridLayout(self.tab_QCM)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.treeWidget_4 = QTreeWidget(self.tab_QCM)
        self.treeWidget_4.setObjectName(u"treeWidget_4")

        self.gridLayout_2.addWidget(self.treeWidget_4, 0, 1, 1, 1)

        self.treeWidget_5 = QTreeWidget(self.tab_QCM)
        QTreeWidgetItem(self.treeWidget_5)
        QTreeWidgetItem(self.treeWidget_5)
        QTreeWidgetItem(self.treeWidget_5)
        QTreeWidgetItem(self.treeWidget_5)
        QTreeWidgetItem(self.treeWidget_5)
        QTreeWidgetItem(self.treeWidget_5)
        self.treeWidget_5.setObjectName(u"treeWidget_5")

        self.gridLayout_2.addWidget(self.treeWidget_5, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.tab_QCM)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.tab_QCM)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)

        self.Dir_Functions.addTab(self.tab_QCM, "")
        self.tab_FTIR = QWidget()
        self.tab_FTIR.setObjectName(u"tab_FTIR")
        self.gridLayout_3 = QGridLayout(self.tab_FTIR)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.treewidget_list = QTreeWidget(self.tab_FTIR)
        self.treewidget_list.setObjectName(u"treewidget_list")

        self.gridLayout_3.addWidget(self.treewidget_list, 0, 2, 1, 1)

        self.label_3 = QLabel(self.tab_FTIR)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 2, 1, 1)

        self.label_2 = QLabel(self.tab_FTIR)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)

        self.treewidget_functions = QTreeWidget(self.tab_FTIR)
        QTreeWidgetItem(self.treewidget_functions)
        QTreeWidgetItem(self.treewidget_functions)
        QTreeWidgetItem(self.treewidget_functions)
        QTreeWidgetItem(self.treewidget_functions)
        QTreeWidgetItem(self.treewidget_functions)
        self.treewidget_functions.setObjectName(u"treewidget_functions")

        self.gridLayout_3.addWidget(self.treewidget_functions, 0, 0, 1, 1)

        self.label = QLabel(self.tab_FTIR)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.tab_FTIR)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.lineEdit_from = QLineEdit(self.tab_FTIR)
        self.lineEdit_from.setObjectName(u"lineEdit_from")

        self.gridLayout_3.addWidget(self.lineEdit_from, 3, 0, 1, 1)

        self.lineEdit_to = QLineEdit(self.tab_FTIR)
        self.lineEdit_to.setObjectName(u"lineEdit_to")

        self.gridLayout_3.addWidget(self.lineEdit_to, 3, 2, 1, 1)

        self.Dir_Functions.addTab(self.tab_FTIR, "")
        self.tab_SE = QWidget()
        self.tab_SE.setObjectName(u"tab_SE")
        self.verticalLayout_2 = QVBoxLayout(self.tab_SE)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeWidget = QTreeWidget(self.tab_SE)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_2.addWidget(self.treeWidget)

        self.pushButton = QPushButton(self.tab_SE)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.Dir_Functions.addTab(self.tab_SE, "")

        self.verticalLayout.addWidget(self.Dir_Functions)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.Dir_Functions.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtreewidgetitem = self.treeWidget_4.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Dialog", u"Y", None));
        ___qtreewidgetitem1 = self.treeWidget_5.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Dialog", u"QCM", None));

        __sortingEnabled = self.treeWidget_5.isSortingEnabled()
        self.treeWidget_5.setSortingEnabled(False)
        ___qtreewidgetitem2 = self.treeWidget_5.topLevelItem(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Dialog", u"Half Cycle Changes", None));
        ___qtreewidgetitem3 = self.treeWidget_5.topLevelItem(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Dialog", u"Full Cycle Changes", None));
        ___qtreewidgetitem4 = self.treeWidget_5.topLevelItem(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("Dialog", u"Pressure", None));
        ___qtreewidgetitem5 = self.treeWidget_5.topLevelItem(3)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("Dialog", u"QCM Mass", None));
        ___qtreewidgetitem6 = self.treeWidget_5.topLevelItem(4)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("Dialog", u"QCM Mass Sub", None));
        ___qtreewidgetitem7 = self.treeWidget_5.topLevelItem(5)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("Dialog", u"QCM Mass Diff", None));
        self.treeWidget_5.setSortingEnabled(__sortingEnabled)

        self.Dir_Functions.setTabText(self.Dir_Functions.indexOf(self.tab_QCM), QCoreApplication.translate("Dialog", u"QCM", None))
        ___qtreewidgetitem8 = self.treewidget_list.headerItem()
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("Dialog", u"Survey", None));
        self.label_3.setText(QCoreApplication.translate("Dialog", u"To", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"From ", None))
        ___qtreewidgetitem9 = self.treewidget_functions.headerItem()
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("Dialog", u"FTIR", None));

        __sortingEnabled1 = self.treewidget_functions.isSortingEnabled()
        self.treewidget_functions.setSortingEnabled(False)
        ___qtreewidgetitem10 = self.treewidget_functions.topLevelItem(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("Dialog", u"Plot All", None));
        ___qtreewidgetitem11 = self.treewidget_functions.topLevelItem(1)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("Dialog", u"Subtraction", None));
        ___qtreewidgetitem12 = self.treewidget_functions.topLevelItem(2)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("Dialog", u"Difference", None));
        ___qtreewidgetitem13 = self.treewidget_functions.topLevelItem(3)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("Dialog", u"Integration", None));
        ___qtreewidgetitem14 = self.treewidget_functions.topLevelItem(4)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("Dialog", u"Integrations", None));
        self.treewidget_functions.setSortingEnabled(__sortingEnabled1)

        self.label.setText(QCoreApplication.translate("Dialog", u"Skip Plot Every: ", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.lineEdit_from.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.lineEdit_to.setText(QCoreApplication.translate("Dialog", u"9999", None))
        self.Dir_Functions.setTabText(self.Dir_Functions.indexOf(self.tab_FTIR), QCoreApplication.translate("Dialog", u"FTIR", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.Dir_Functions.setTabText(self.Dir_Functions.indexOf(self.tab_SE), QCoreApplication.translate("Dialog", u"SE", None))
    # retranslateUi

