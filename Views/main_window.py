# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class AdministrationForm(object):
    def setupUi(self, AdministrationForm):
        if not AdministrationForm.objectName():
            AdministrationForm.setObjectName(u"AdministrationForm")
        AdministrationForm.resize(1000, 700)
        self.ownerFrame = QFrame(AdministrationForm)
        self.ownerFrame.setObjectName(u"ownerFrame")
        self.ownerFrame.setGeometry(QRect(20, 20, 961, 151))
        self.ownerFrame.setFrameShape(QFrame.StyledPanel)
        self.ownerFrame.setFrameShadow(QFrame.Raised)
        self.dniDoctorEdit = QLineEdit(self.ownerFrame)
        self.dniDoctorEdit.setObjectName(u"dniDoctorEdit")
        self.dniDoctorEdit.setGeometry(QRect(220, 30, 250, 40))
        self.label_dni = QLabel(self.ownerFrame)
        self.label_dni.setObjectName(u"label_dni")
        self.label_dni.setGeometry(QRect(20, 30, 191, 40))
        self.label_owner = QLabel(self.ownerFrame)
        self.label_owner.setObjectName(u"label_owner")
        self.label_owner.setGeometry(QRect(10, 0, 151, 20))
        self.searchDoctorButton = QPushButton(self.ownerFrame)
        self.searchDoctorButton.setObjectName(u"searchDoctorButton")
        self.searchDoctorButton.setGeometry(QRect(340, 90, 251, 41))
        self.searchDoctorButton.setStyleSheet(u"QPushButton {\n"
"    height: 2em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0069c0;\n"
"    color: white;\n"
"}")
        icon = QIcon()
        icon.addFile(u"./assets/icons/searchDoctor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchDoctorButton.setIcon(icon)
        self.searchDoctorButton.setFlat(False)
        self.farmFrame = QFrame(AdministrationForm)
        self.farmFrame.setObjectName(u"farmFrame")
        self.farmFrame.setGeometry(QRect(20, 190, 961, 191))
        self.farmFrame.setFrameShape(QFrame.StyledPanel)
        self.farmFrame.setFrameShadow(QFrame.Raised)
        self.lineEdit_2 = QLineEdit(self.farmFrame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(1372, 260, 150, 16))
        self.label_RC = QLabel(self.farmFrame)
        self.label_RC.setObjectName(u"label_RC")
        self.label_RC.setGeometry(QRect(10, 60, 121, 40))
        self.searchHospitalButton = QPushButton(self.farmFrame)
        self.searchHospitalButton.setObjectName(u"searchHospitalButton")
        self.searchHospitalButton.setGeometry(QRect(360, 120, 181, 41))
        self.searchHospitalButton.setStyleSheet(u"QPushButton {\n"
"    height: 2em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0069c0;\n"
"    color: white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/searchHospital.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchHospitalButton.setIcon(icon1)
        self.searchHospitalButton.setIconSize(QSize(30, 30))
        self.label_farm = QLabel(self.farmFrame)
        self.label_farm.setObjectName(u"label_farm")
        self.label_farm.setGeometry(QRect(10, 10, 91, 20))
        self.hospitalNameEdit = QLineEdit(self.farmFrame)
        self.hospitalNameEdit.setObjectName(u"hospitalNameEdit")
        self.hospitalNameEdit.setGeometry(QRect(80, 60, 250, 40))

        self.retranslateUi(AdministrationForm)

        QMetaObject.connectSlotsByName(AdministrationForm)
    # setupUi

    def retranslateUi(self, AdministrationForm):
        AdministrationForm.setWindowTitle(QCoreApplication.translate("AdministrationForm", u"Hospitales", None))
        self.label_dni.setText(QCoreApplication.translate("AdministrationForm", u"Documento de identificaci\u00f3n", None))
        self.label_owner.setText(QCoreApplication.translate("AdministrationForm", u"Doctores", None))
        self.searchDoctorButton.setText(QCoreApplication.translate("AdministrationForm", u"Buscar doctor", None))
        self.label_RC.setText(QCoreApplication.translate("AdministrationForm", u"Nombre", None))
        self.searchHospitalButton.setText(QCoreApplication.translate("AdministrationForm", u"Buscar hospital", None))
        self.label_farm.setText(QCoreApplication.translate("AdministrationForm", u"Hospitales", None))
    # retranslateUi

