# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'food_view.ui'
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

class Ui_Form_nood2_1(object):
    def setupUi(self, Form_nood2_1):
        Form_nood2_1.setObjectName(_fromUtf8("Form_nood2_1"))
        Form_nood2_1.resize(600, 400)
        self.pushButton = QtGui.QPushButton(Form_nood2_1)
        self.pushButton.setGeometry(QtCore.QRect(450, 360, 121, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Form_nood2_1)
        self.label.setGeometry(QtCore.QRect(20, 10, 481, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.tableWidget = QtGui.QTableWidget(Form_nood2_1)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 561, 281))
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

        self.retranslateUi(Form_nood2_1)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_nood2_1.slot1_nood2)
        QtCore.QMetaObject.connectSlotsByName(Form_nood2_1)

    def retranslateUi(self, Form_nood2_1):
        Form_nood2_1.setWindowTitle(_translate("Form_nood2_1", "Form", None))
        self.pushButton.setText(_translate("Form_nood2_1", "뒤로가기", None))
        self.label.setText(_translate("Form_nood2_1", "휴게소 대표 음식 현황(전체)", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form_nood2_1", "휴게소명", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form_nood2_1", "고속도로명", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form_nood2_1", "방향", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form_nood2_1", "대표음식", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form_nood2_1", "판매가격", None))

