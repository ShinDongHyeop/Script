# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_nood1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form_nood1(object):
    def setupUi(self, Form_nood1):
        Form_nood1.setObjectName(_fromUtf8("Form_nood1"))
        Form_nood1.resize(400, 300)
        self.pushButton = QtGui.QPushButton(Form_nood1)
        self.pushButton.setGeometry(QtCore.QRect(210, 160, 161, 61))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Form_nood1)
        self.label.setGeometry(QtCore.QRect(20, 10, 351, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(Form_nood1)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 70, 161, 61))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form_nood1)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 70, 161, 61))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Form_nood1)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 160, 161, 61))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.retranslateUi(Form_nood1)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_nood1.slot1_root)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_nood1.slot1_nood1_1)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_nood1.slot1_nood1_2)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_nood1.slot1_nood1_3)
        QtCore.QMetaObject.connectSlotsByName(Form_nood1)

    def retranslateUi(self, Form_nood1):
        Form_nood1.setWindowTitle(_translate("Form_nood1", "Form", None))
        self.pushButton.setText(_translate("Form_nood1", "처음으로", None))
        self.label.setText(_translate("Form_nood1", "휴게소 시설", None))
        self.pushButton_2.setText(_translate("Form_nood1", "전체 보기", None))
        self.pushButton_3.setText(_translate("Form_nood1", "검색", None))
        self.pushButton_4.setText(_translate("Form_nood1", "추가/수정/삭제", None))

