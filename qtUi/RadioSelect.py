# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RadioSelect.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
# Contributed by SWAGLORD12

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("RadioSelect")
        Form.resize(480, 320)
        
        self.Skywarn = QtWidgets.QPushButton(Form)
        self.Skywarn.setGeometry(QtCore.QRect(0, 0, 115, 150))
        self.Skywarn.setObjectName("Skywarn")
        iconSkywarn = QtGui.QIcon()
        iconSkywarn.addPixmap(QtGui.QPixmap("resources/skywarn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Skywarn.setIcon(iconSkywarn)
        self.Skywarn.setIconSize(QtCore.QSize(110, 145))
        
        self.Police = QtWidgets.QPushButton(Form)
        self.Police.setGeometry(QtCore.QRect(120, 0, 115, 150))
        self.Police.setObjectName("Police")
        iconPolice = QtGui.QIcon()
        iconPolice.addPixmap(QtGui.QPixmap("resources/POLICE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Police.setIcon(iconPolice)
        self.Police.setIconSize(QtCore.QSize(110, 145))
        
        self.Ham = QtWidgets.QPushButton(Form)
        self.Ham.setGeometry(QtCore.QRect(240, 0, 115, 150))
        self.Ham.setObjectName("HAM")
        iconHam = QtGui.QIcon()
        iconHam.addPixmap(QtGui.QPixmap("resources/HAMRadio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Ham.setIcon(iconHam)
        self.Ham.setIconSize(QtCore.QSize(110, 145))
        
        self.FM = QtWidgets.QPushButton(Form)
        self.FM.setGeometry(QtCore.QRect(360, 0, 115, 150))
        self.FM.setObjectName("FM")
        iconFM = QtGui.QIcon()
        iconFM.addPixmap(QtGui.QPixmap("resources/radio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FM.setIcon(iconFM)
        self.FM.setIconSize(QtCore.QSize(110, 145))
        
        self.Home = QtWidgets.QPushButton(Form)
        self.Home.setGeometry(QtCore.QRect(140, 180, 200, 120))
        self.Home.setObjectName("Home")
        iconHome = QtGui.QIcon()
        iconHome.addPixmap(QtGui.QPixmap("resources/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home.setIcon(iconHome)
        self.Home.setIconSize(QtCore.QSize(110, 145))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RadioSelect"))
        self.Skywarn.setText(_translate("Form", ""))  
        self.Police.setText(_translate("Form", ""))     
        self.Ham.setText(_translate("Form", ""))    
        self.FM.setText(_translate("Form", ""))
        self.Home.setText(_translate("Form", ""))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    TempService = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(TempService)
    TempService.show()
    sys.exit(app.exec_())



