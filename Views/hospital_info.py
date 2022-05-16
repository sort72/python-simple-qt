# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hospital_info.ui'
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
        Dialog.resize(534, 300)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 0, 291, 51))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.acceptButton = QPushButton(Dialog)
        self.acceptButton.setObjectName(u"acceptButton")
        self.acceptButton.setGeometry(QRect(210, 220, 121, 61))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 50, 49, 16))
        self.hospitalName = QLabel(Dialog)
        self.hospitalName.setObjectName(u"hospitalName")
        self.hospitalName.setGeometry(QRect(120, 50, 151, 16))
        self.hospitalId = QLabel(Dialog)
        self.hospitalId.setObjectName(u"hospitalId")
        self.hospitalId.setGeometry(QRect(120, 70, 191, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 81, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Informaci\u00f3n del hospital", None))
        self.acceptButton.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nombre:", None))
        self.hospitalName.setText(QCoreApplication.translate("Dialog", u"{name}", None))
        self.hospitalId.setText(QCoreApplication.translate("Dialog", u"{id}", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Identificaci\u00f3n:", None))
    # retranslateUi

