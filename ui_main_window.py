# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1316, 876)
        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setGeometry(QtCore.QRect(1110, 780, 100, 60))
        self.control_bt.setMinimumSize(QtCore.QSize(100, 60))
        self.control_bt.setMaximumSize(QtCore.QSize(100, 60))
        self.control_bt.setObjectName("control_bt")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(790, 770, 291, 81))
        self.textBrowser.setMaximumSize(QtCore.QSize(500, 100))
        self.textBrowser.setObjectName("textBrowser")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setEnabled(True)
        self.image_label.setGeometry(QtCore.QRect(20, 20, 1280, 720))
        self.image_label.setMinimumSize(QtCore.QSize(1280, 720))
        self.image_label.setMaximumSize(QtCore.QSize(1280, 720))
        self.image_label.setObjectName("image_label")
        self.date_label = QtWidgets.QLabel(Form)
        self.date_label.setGeometry(QtCore.QRect(100, 780, 150, 30))
        self.date_label.setMinimumSize(QtCore.QSize(150, 30))
        self.date_label.setMaximumSize(QtCore.QSize(150, 30))
        self.date_label.setObjectName("date_label")
        self.time_label = QtWidgets.QLabel(Form)
        self.time_label.setGeometry(QtCore.QRect(100, 820, 150, 30))
        self.time_label.setMinimumSize(QtCore.QSize(150, 30))
        self.time_label.setMaximumSize(QtCore.QSize(150, 30))
        self.time_label.setObjectName("time_label")
        self.dead_time = QtWidgets.QTimeEdit(Form)
        self.dead_time.setGeometry(QtCore.QRect(490, 800, 90, 31))
        self.dead_time.setObjectName("dead_time")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(380, 800, 111, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "人脸识别打卡系统"))
        self.control_bt.setText(_translate("Form", "start"))
        self.image_label.setText(_translate("Form", "Cam"))
        self.date_label.setText(_translate("Form", "Date"))
        self.time_label.setText(_translate("Form", "Time"))
        self.dead_time.setDisplayFormat(_translate("Form", "hh:mm:ss"))
        self.label.setText(_translate("Form", "打卡截止时间："))


