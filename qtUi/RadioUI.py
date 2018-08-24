# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RadioUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
# Contributed by SWAGLORD12

from PyQt5 import QtCore, QtGui, QtWidgets
#from rtlsdr import RtlSdr
import sys
import functools
import threading
import time
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Starting Radio UI')
            
class Ui_Form(object):
    
    def setupUi(self, Form):
        
        Form.setObjectName("Form")
        Form.resize(800, 480)
        
        self.freqNum = QtWidgets.QLCDNumber(Form)
        self.freqNum.setGeometry(QtCore.QRect(110, 0, 571, 71))
        self.freqNum.setObjectName("freqNum")
        self.freqNum.setDigitCount(12)
        
        #self.waveLength = QtQuickWidgets.QQuickWidget(Form)
        #self.waveLength.setGeometry(QtCore.QRect(20, 80, 751, 231))
        #self.waveLength.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        #self.waveLength.setObjectName("waveLength")
        
        self.UpButton = QtWidgets.QPushButton(Form)
        self.UpButton.setGeometry(QtCore.QRect(20, 340, 81, 121))
        self.UpButton.setObjectName("UpButton")
        self.UpButton.clicked.connect(self.RangeUp)
        
        self.downButton = QtWidgets.QPushButton(Form)
        self.downButton.setGeometry(QtCore.QRect(130, 340, 81, 121))
        self.downButton.setObjectName("downButton")
        self.UpButton.clicked.connect(self.RangeDown)
        
        self.scanButton = QtWidgets.QPushButton(Form)
        self.scanButton.setGeometry(QtCore.QRect(240, 340, 81, 121))
        self.scanButton.setObjectName("scanButton")
        
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 340, 81, 121))
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.Exit = QtWidgets.QPushButton(Form)
        self.Exit.setGeometry(QtCore.QRect(700, 0, 81, 71))
        self.Exit.setObjectName("Exit")
        
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 340, 81, 121))
        self.pushButton_5.setObjectName("pushButton_5")
        
        self.Home = QtWidgets.QPushButton(Form)
        self.Home.setGeometry(QtCore.QRect(10, 0, 81, 71))
        self.Home.setObjectName("Home")
        
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(570, 340, 211, 121))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        setfreq = threading.Thread(target=self.setFreqLCD)
        setfreq.start()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.UpButton.setText(_translate("Form", "up"))
        self.downButton.setText(_translate("Form", "Down"))
        self.scanButton.setText(_translate("Form", "Scan"))
        self.pushButton_4.setText(_translate("Form", "PushButton"))
        self.Exit.setText(_translate("Form", "Exit"))
        self.pushButton_5.setText(_translate("Form", "PushButton"))
        self.Home.setText(_translate("Form", "Home"))
        self.pushButton_6.setText(_translate("Form", "PushButton"))

    self.freq = 0
    
    def setFreqLCD(self):
        while True:

            #sdr = RtlSdr()
            
            #self.__freq = 101.1
            #tup  = Quantity(i,'FM')
            #tup = '{:8.1f}'.format(i)
            print (freq)
            #sdr.sample_rate = i
            
            logger.info('Setting LCD')
            self.freqNum.display(freq)
           
            time.sleep(1)

    def RangeUp(self):
        self.freq += 10
        print (self.freq)
        return self.freq


    def RangeDown(self):
        self.__freq -= 10
            
    def home(self):
        time.sleep(1)
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    RadioUI = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(RadioUI)
    RadioUI.show()
    sys.exit(app.exec_())

        
