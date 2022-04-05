# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_organizerFile.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(592, 401)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.CaminhoArquivo = QLineEdit(self.frame)
        self.CaminhoArquivo.setObjectName(u"CaminhoArquivo")
        self.CaminhoArquivo.setStyleSheet(u"QLineEdit{background-color:rgb(254, 254, 254);}")
        self.CaminhoArquivo.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.CaminhoArquivo)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{border-top-radius: 15px; background-color:rgb(243, 243, 243);} \n"
"QPushButton:hover{color:#fff; background-color:rgb(135, 202, 0)}")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.btnOrganizer = QPushButton(self.frame)
        self.btnOrganizer.setObjectName(u"btnOrganizer")
        self.btnOrganizer.setEnabled(True)
        self.btnOrganizer.setMinimumSize(QSize(14, 16))
        font = QFont()
        font.setPointSize(12)
        self.btnOrganizer.setFont(font)
        self.btnOrganizer.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnOrganizer.setStyleSheet(u"QPushButton{background-color:rgb(243, 243, 243);border-radius:100px;} \n"
"QPushButton:hover{color:#fff; background-color:rgb(135, 202, 0)}")
        self.btnOrganizer.setIconSize(QSize(15, 15))

        self.horizontalLayout.addWidget(self.btnOrganizer)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#5500ff;\">ORGANIZADOR DE ARQUIVOS</span></p></body></html>", None))
        self.CaminhoArquivo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a Pasta", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar pasta", None))
        self.label_2.setText("")
        self.btnOrganizer.setText(QCoreApplication.translate("MainWindow", u"Organizar", None))
        self.label_3.setText("")
    # retranslateUi

