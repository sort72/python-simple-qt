# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'not_found.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(538, 300)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 161, 161))
        self.label.setPixmap(QPixmap(u"./assets/icons/warning.png"))
        self.label.setScaledContents(True)
        self.acceptButton = QPushButton(Dialog)
        self.acceptButton.setObjectName(u"acceptButton")
        self.acceptButton.setGeometry(QRect(270, 220, 121, 41))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 90, 231, 61))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.acceptButton.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"No se encontraron resultados.", None))
    # retranslateUi

