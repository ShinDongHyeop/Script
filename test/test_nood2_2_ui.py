# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_nood2_2.ui'
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

class Ui_Form_nood2_2(object):
    def setupUi(self, Form_nood2_2):
        Form_nood2_2.setObjectName(_fromUtf8("Form_nood2_2"))
        Form_nood2_2.resize(538, 343)
        self.label = QtGui.QLabel(Form_nood2_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 351, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(Form_nood2_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 71, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(Form_nood2_2)
        self.pushButton.setGeometry(QtCore.QRect(400, 310, 121, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form_nood2_2)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 50, 41, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.textEdit = QtGui.QTextEdit(Form_nood2_2)
        self.textEdit.setGeometry(QtCore.QRect(100, 50, 371, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.tableWidget = QtGui.QTableWidget(Form_nood2_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 501, 211))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        self.retranslateUi(Form_nood2_2)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_nood2_2.slot1_nood2)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_nood2_2.slot1_serch)
        QtCore.QMetaObject.connectSlotsByName(Form_nood2_2)

    def retranslateUi(self, Form_nood2_2):
        Form_nood2_2.setWindowTitle(_translate("Form_nood2_2", "Form", None))
        self.label.setText(_translate("Form_nood2_2", "휴게소 대표 음식 현황(검색)", None))
        self.comboBox.setItemText(0, _translate("Form_nood2_2", "휴게소명", None))
        self.comboBox.setItemText(1, _translate("Form_nood2_2", "노선명", None))
        self.pushButton.setText(_translate("Form_nood2_2", "뒤로가기", None))
        self.pushButton_2.setText(_translate("Form_nood2_2", "검색", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form_nood2_2", "휴게소명", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form_nood2_2", "노선명", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form_nood2_2", "방향", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form_nood2_2", "대표음식", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form_nood2_2", "판매가격", None))

