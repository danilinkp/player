# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playlist_input_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(328, 115)
        Form.setMinimumSize(QtCore.QSize(328, 115))
        Form.setMaximumSize(QtCore.QSize(328, 115))
        Form.setStyleSheet("background: rgb(40, 40, 40)")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.ok_btn = QtWidgets.QPushButton(Form)
        self.ok_btn.setStyleSheet("color: white\n"
"")
        self.ok_btn.setObjectName("ok_btn")
        self.gridLayout.addWidget(self.ok_btn, 2, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.playlist_name_line = QtWidgets.QLineEdit(Form)
        self.playlist_name_line.setStyleSheet("color: white")
        self.playlist_name_line.setObjectName("playlist_name_line")
        self.gridLayout.addWidget(self.playlist_name_line, 0, 2, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Введите названия плейлиста"))
        self.ok_btn.setText(_translate("Form", "OK"))
        self.label.setText(_translate("Form", "Введите названия плейлиста:"))