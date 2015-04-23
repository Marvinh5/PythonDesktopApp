# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/marvin.DGTT/Documents/Interface qt/Auth.ui'
#
# Created: Tue Jan 20 09:07:53 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(403, 137)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 391, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lblMacAddress = QtWidgets.QLabel(Dialog)
        self.lblMacAddress.setGeometry(QtCore.QRect(10, 120, 241, 16))
        self.lblMacAddress.setObjectName("lblMacAddress")
        self.lblIp = QtWidgets.QLabel(Dialog)
        self.lblIp.setGeometry(QtCore.QRect(260, 120, 141, 16))
        self.lblIp.setObjectName("lblIp")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.pushButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Auth"))
        self.label.setText(_translate("Dialog", "Usuario:"))
        self.pushButton.setAccessibleName(_translate("Dialog", "btnLogin"))
        self.pushButton.setText(_translate("Dialog", "Entrar"))
        self.label_2.setText(_translate("Dialog", "Contrasena:"))
        self.lineEdit.setAccessibleName(_translate("Dialog", "txtUsuario"))
        self.lblMacAddress.setText(_translate("Dialog", "Direccion Fisica:"))
        self.lblIp.setText(_translate("Dialog", "IP:"))

