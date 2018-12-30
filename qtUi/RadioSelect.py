# Contributed by SWAGLORD12

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from rfscreen import *

class RadioSelect(object):
 
    def main():
        app = QtWidgets.QApplication(sys.argv)
        rfscreen = QtWidgets.QMainWindow()
        ui = rfscreen.RFScreen()
        ui.setupUi(rfscreen)
        rfscreen.show()
        sys.exit(app.exec_())
        
    def setupUi(self, Form):
       
        Form.setObjectName("RadioSelect")
        Form.resize(480, 320)

        #Top Buttons 
        self.FM = QtWidgets.QPushButton(Form)
        self.FM.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.FM.setObjectName("FM")
        iconFM = QtGui.QIcon()
        iconFM.addPixmap(QtGui.QPixmap("resources/radio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FM.setIcon(iconFM)
        self.FM.setIconSize(QtCore.QSize(110, 145))
        self.FM.clicked.connect(self.radio_pushed)

        self.Police = QtWidgets.QPushButton(Form)
        self.Police.setGeometry(QtCore.QRect(165, 0, 150, 150))
        self.Police.setObjectName("Police")
        iconPolice = QtGui.QIcon()
        iconPolice.addPixmap(QtGui.QPixmap("resources/POLICE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Police.setIcon(iconPolice)
        self.Police.setIconSize(QtCore.QSize(110, 145))
        
        self.Skywarn = QtWidgets.QPushButton(Form)
        self.Skywarn.setGeometry(QtCore.QRect(330, 0, 150, 150))
        self.Skywarn.setObjectName("Skywarn")
        iconSkywarn = QtGui.QIcon()
        iconSkywarn.addPixmap(QtGui.QPixmap("resources/skywarn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Skywarn.setIcon(iconSkywarn)
        self.Skywarn.setIconSize(QtCore.QSize(110, 145))

        #Bottom Buttons
        self.noaa = QtWidgets.QPushButton(Form)
        self.noaa.setGeometry(QtCore.QRect(0, 170, 150, 150))
        self.noaa.setObjectName("HAM")
        iconNoaa = QtGui.QIcon()
        iconNoaa.addPixmap(QtGui.QPixmap("resources/skywarn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.noaa.setIcon(iconNoaa)
        self.noaa.setIconSize(QtCore.QSize(110, 145))

        self.Ham = QtWidgets.QPushButton(Form)
        self.Ham.setGeometry(QtCore.QRect(165, 170, 150, 150))
        self.Ham.setObjectName("HAM")
        iconHam = QtGui.QIcon()
        iconHam.addPixmap(QtGui.QPixmap("resources/HAMRadio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Ham.setIcon(iconHam)
        self.Ham.setIconSize(QtCore.QSize(110, 145))
        
        self.Home = QtWidgets.QPushButton(Form)
        self.Home.setGeometry(QtCore.QRect(330, 170, 150, 150))
        self.Home.setObjectName("Home")
        iconHome = QtGui.QIcon()
        iconHome.addPixmap(QtGui.QPixmap("resources/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home.setIcon(iconHome)
        self.Home.setIconSize(QtCore.QSize(110, 145))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def radio_pushed(self):
        #radioselect.close()
        main()

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
    radioselect = QtWidgets.QMainWindow()
    ui = RadioSelect()
    ui.setupUi(radioselect)
    radioselect.show()
    sys.exit(app.exec_())



