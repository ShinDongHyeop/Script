# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_nood2_3.ui'
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

class Ui_Form_nood2_3(object):
    def setupUi(self, Form_nood2_3):
        Form_nood2_3.setObjectName(_fromUtf8("Form_nood2_3"))
        Form_nood2_3.resize(452, 403)
        self.label = QtGui.QLabel(Form_nood2_3)
        self.label.setGeometry(QtCore.QRect(20, 10, 421, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_4 = QtGui.QPushButton(Form_nood2_3)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 370, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_2 = QtGui.QPushButton(Form_nood2_3)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 370, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(Form_nood2_3)
        self.pushButton.setGeometry(QtCore.QRect(320, 370, 121, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(Form_nood2_3)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 370, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.groupBox = QtGui.QGroupBox(Form_nood2_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 431, 211))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 100, 56, 12))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.textEdit_10 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_10.setGeometry(QtCore.QRect(130, 140, 291, 16))
        self.textEdit_10.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_10.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_10.setObjectName(_fromUtf8("textEdit_10"))
        self.textEdit_14 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_14.setGeometry(QtCore.QRect(130, 20, 291, 16))
        self.textEdit_14.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_14.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_14.setObjectName(_fromUtf8("textEdit_14"))
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(10, 20, 56, 12))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.textEdit_15 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_15.setGeometry(QtCore.QRect(130, 100, 291, 16))
        self.textEdit_15.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_15.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_15.setObjectName(_fromUtf8("textEdit_15"))
        self.label_16 = QtGui.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(10, 60, 56, 12))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.textEdit_17 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_17.setGeometry(QtCore.QRect(130, 180, 291, 16))
        self.textEdit_17.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_17.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_17.setObjectName(_fromUtf8("textEdit_17"))
        self.textEdit_18 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_18.setGeometry(QtCore.QRect(130, 60, 291, 16))
        self.textEdit_18.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_18.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_18.setObjectName(_fromUtf8("textEdit_18"))
        self.label_18 = QtGui.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(10, 180, 81, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(10, 140, 56, 12))
        self.label_19.setObjectName(_fromUtf8("label_19"))

        self.retranslateUi(Form_nood2_3)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_nood2_3.dialog_add)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_nood2_3.dialog_chang)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_nood2_3.dialog_delete)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_nood2_3.slot1_nood2)
        QtCore.QMetaObject.connectSlotsByName(Form_nood2_3)

    def retranslateUi(self, Form_nood2_3):
        Form_nood2_3.setWindowTitle(_translate("Form_nood2_3", "Form", None))
        self.label.setText(_translate("Form_nood2_3", "휴게소 음식 정보(추가, 수정, 삭제)", None))
        self.pushButton_4.setText(_translate("Form_nood2_3", "삭제", None))
        self.pushButton_2.setText(_translate("Form_nood2_3", "추가", None))
        self.pushButton.setText(_translate("Form_nood2_3", "뒤로가기", None))
        self.pushButton_3.setText(_translate("Form_nood2_3", "수정", None))
        self.groupBox.setTitle(_translate("Form_nood2_3", "정보 입력", None))
        self.label_11.setText(_translate("Form_nood2_3", "휴게소명", None))
        self.label_14.setText(_translate("Form_nood2_3", "노선명", None))
        self.label_16.setText(_translate("Form_nood2_3", "방향", None))
        self.label_18.setText(_translate("Form_nood2_3", "판매가격", None))
        self.label_19.setText(_translate("Form_nood2_3", "대표음식", None))

