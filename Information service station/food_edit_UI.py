# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'food_edit.ui'
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
        Form_nood2_3.resize(600, 400)
        self.label = QtGui.QLabel(Form_nood2_3)
        self.label.setGeometry(QtCore.QRect(20, 10, 491, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Form_nood2_3)
        self.pushButton.setGeometry(QtCore.QRect(460, 360, 121, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tabWidget = QtGui.QTabWidget(Form_nood2_3)
        self.tabWidget.setGeometry(QtCore.QRect(20, 50, 561, 291))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.add = QtGui.QWidget()
        self.add.setObjectName(_fromUtf8("add"))
        self.groupBox = QtGui.QGroupBox(self.add)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 511, 221))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(20, 90, 65, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.textEdit_10 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_10.setGeometry(QtCore.QRect(140, 120, 340, 16))
        self.textEdit_10.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_10.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_10.setObjectName(_fromUtf8("textEdit_10"))
        self.textEdit_14 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_14.setGeometry(QtCore.QRect(140, 30, 340, 16))
        self.textEdit_14.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_14.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_14.setObjectName(_fromUtf8("textEdit_14"))
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(20, 30, 61, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.textEdit_15 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_15.setGeometry(QtCore.QRect(140, 90, 340, 16))
        self.textEdit_15.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_15.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_15.setObjectName(_fromUtf8("textEdit_15"))
        self.label_16 = QtGui.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(20, 60, 56, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.textEdit_17 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_17.setGeometry(QtCore.QRect(140, 150, 340, 16))
        self.textEdit_17.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_17.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_17.setObjectName(_fromUtf8("textEdit_17"))
        self.textEdit_18 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_18.setGeometry(QtCore.QRect(140, 60, 340, 16))
        self.textEdit_18.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_18.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_18.setObjectName(_fromUtf8("textEdit_18"))
        self.label_18 = QtGui.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(20, 150, 81, 20))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(20, 120, 65, 20))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 180, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabWidget.addTab(self.add, _fromUtf8(""))
        self.change = QtGui.QWidget()
        self.change.setObjectName(_fromUtf8("change"))
        self.groupBox_2 = QtGui.QGroupBox(self.change)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 511, 221))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(20, 90, 65, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.textEdit_11 = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit_11.setGeometry(QtCore.QRect(140, 120, 340, 16))
        self.textEdit_11.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_11.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_11.setObjectName(_fromUtf8("textEdit_11"))
        self.textEdit_16 = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit_16.setGeometry(QtCore.QRect(140, 30, 340, 16))
        self.textEdit_16.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_16.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_16.setObjectName(_fromUtf8("textEdit_16"))
        self.textEdit_19 = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit_19.setGeometry(QtCore.QRect(140, 90, 340, 16))
        self.textEdit_19.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_19.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_19.setObjectName(_fromUtf8("textEdit_19"))
        self.label_17 = QtGui.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(20, 60, 56, 20))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.textEdit_21 = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit_21.setGeometry(QtCore.QRect(140, 150, 340, 16))
        self.textEdit_21.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_21.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_21.setObjectName(_fromUtf8("textEdit_21"))
        self.textEdit_22 = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit_22.setGeometry(QtCore.QRect(140, 60, 340, 16))
        self.textEdit_22.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_22.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_22.setObjectName(_fromUtf8("textEdit_22"))
        self.label_20 = QtGui.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(20, 150, 81, 20))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(20, 120, 65, 20))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 180, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(20, 30, 61, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.tabWidget.addTab(self.change, _fromUtf8(""))
        self.delete_2 = QtGui.QWidget()
        self.delete_2.setObjectName(_fromUtf8("delete_2"))
        self.pushButton_4 = QtGui.QPushButton(self.delete_2)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 230, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.tableWidget = QtGui.QTableWidget(self.delete_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 531, 171))
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
        self.textEdit = QtGui.QTextEdit(self.delete_2)
        self.textEdit.setGeometry(QtCore.QRect(90, 10, 401, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.comboBox = QtGui.QComboBox(self.delete_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton_5 = QtGui.QPushButton(self.delete_2)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 10, 41, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.tabWidget.addTab(self.delete_2, _fromUtf8(""))

        self.retranslateUi(Form_nood2_3)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_nood2_3.dialog_add)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_nood2_3.dialog_chang)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_nood2_3.dialog_delete)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_nood2_3.slot1_nood2)
        QtCore.QMetaObject.connectSlotsByName(Form_nood2_3)

    def retranslateUi(self, Form_nood2_3):
        Form_nood2_3.setWindowTitle(_translate("Form_nood2_3", "Form", None))
        self.label.setText(_translate("Form_nood2_3", "휴게소 음식 정보(추가, 수정, 삭제)", None))
        self.pushButton.setText(_translate("Form_nood2_3", "뒤로가기", None))
        self.groupBox.setTitle(_translate("Form_nood2_3", "정보 입력", None))
        self.label_11.setText(_translate("Form_nood2_3", "휴게소명", None))
        self.label_14.setText(_translate("Form_nood2_3", "고속도로명", None))
        self.label_16.setText(_translate("Form_nood2_3", "방향", None))
        self.label_18.setText(_translate("Form_nood2_3", "판매가격", None))
        self.label_19.setText(_translate("Form_nood2_3", "대표음식", None))
        self.pushButton_2.setText(_translate("Form_nood2_3", "추가", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add), _translate("Form_nood2_3", "추가", None))
        self.groupBox_2.setTitle(_translate("Form_nood2_3", "정보 입력", None))
        self.label_12.setText(_translate("Form_nood2_3", "휴게소명", None))
        self.label_17.setText(_translate("Form_nood2_3", "방향", None))
        self.label_20.setText(_translate("Form_nood2_3", "판매가격", None))
        self.label_21.setText(_translate("Form_nood2_3", "대표음식", None))
        self.pushButton_3.setText(_translate("Form_nood2_3", "수정", None))
        self.label_15.setText(_translate("Form_nood2_3", "고속도로명", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.change), _translate("Form_nood2_3", "수정", None))
        self.pushButton_4.setText(_translate("Form_nood2_3", "삭제", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form_nood2_3", "휴게소명", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form_nood2_3", "고속도로명", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form_nood2_3", "방향", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form_nood2_3", "대표음식", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form_nood2_3", "판매가격", None))
        self.comboBox.setItemText(0, _translate("Form_nood2_3", "휴게소명", None))
        self.comboBox.setItemText(1, _translate("Form_nood2_3", "고속도로명", None))
        self.pushButton_5.setText(_translate("Form_nood2_3", "검색", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.delete_2), _translate("Form_nood2_3", "삭제", None))

