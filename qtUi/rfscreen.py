# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rfscreen.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 318)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(320, 90, 151, 51))
        self.Next.setObjectName("Next")
        self.Prev = QtWidgets.QPushButton(self.centralwidget)
        self.Prev.setGeometry(QtCore.QRect(320, 140, 151, 51))
        self.Prev.setObjectName("Prev")
        self.Freq = QtWidgets.QPushButton(self.centralwidget)
        self.Freq.setGeometry(QtCore.QRect(320, 30, 151, 61))
        self.Freq.setObjectName("Freq")
        self.FullScreen = QtWidgets.QPushButton(self.centralwidget)
        self.FullScreen.setGeometry(QtCore.QRect(0, 240, 121, 51))
        self.FullScreen.setObjectName("FullScreen")
        self.Record = QtWidgets.QPushButton(self.centralwidget)
        self.Record.setGeometry(QtCore.QRect(120, 240, 101, 51))
        self.Record.setObjectName("Record")
        self.Seekpos = QtWidgets.QPushButton(self.centralwidget)
        self.Seekpos.setGeometry(QtCore.QRect(320, 190, 151, 51))
        self.Seekpos.setObjectName("Seekpos")
        self.Seekmin = QtWidgets.QPushButton(self.centralwidget)
        self.Seekmin.setGeometry(QtCore.QRect(320, 240, 151, 51))
        self.Seekmin.setObjectName("Seekmin")
        self.Home = QtWidgets.QPushButton(self.centralwidget)
        self.Home.setGeometry(QtCore.QRect(220, 240, 101, 51))
        self.Home.setObjectName("Home")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 320, 881, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 471, 31))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Next.setText(_translate("MainWindow", "NEXT"))
        self.Prev.setText(_translate("MainWindow", "PREV"))
        self.Freq.setText(_translate("MainWindow", "FREQ"))
        self.FullScreen.setText(_translate("MainWindow", "FULL SCREEN"))
        self.Record.setText(_translate("MainWindow", "RECORD"))
        self.Seekpos.setText(_translate("MainWindow", "SEEK +"))
        self.Seekmin.setText(_translate("MainWindow", "SEEK -"))
        self.Home.setText(_translate("MainWindow", "HOME"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "                                                   TextLabel"))

