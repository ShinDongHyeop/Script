# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Traffic_view.ui'
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

class Ui_Traffic_view(object):
    def setupUi(self, Traffic_view):
        Traffic_view.setObjectName(_fromUtf8("Traffic_view"))
        Traffic_view.resize(600, 400)
        self.pushButton = QtGui.QPushButton(Traffic_view)
        self.pushButton.setGeometry(QtCore.QRect(440, 350, 121, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Traffic_view)
        self.label.setGeometry(QtCore.QRect(20, 10, 491, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtGui.QGroupBox(Traffic_view)
        self.groupBox.setGeometry(QtCore.QRect(10, 160, 181, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tableWidget = QtGui.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 161, 111))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.groupBox_2 = QtGui.QGroupBox(Traffic_view)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 181, 71))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.textEdit = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 161, 41))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.groupBox_3 = QtGui.QGroupBox(Traffic_view)
        self.groupBox_3.setGeometry(QtCore.QRect(210, 70, 161, 261))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.tableWidget_3 = QtGui.QTableWidget(self.groupBox_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 20, 141, 231))
        self.tableWidget_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(7)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, item)
        self.groupBox_4 = QtGui.QGroupBox(Traffic_view)
        self.groupBox_4.setGeometry(QtCore.QRect(400, 70, 161, 261))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.tableWidget_4 = QtGui.QTableWidget(self.groupBox_4)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 20, 141, 231))
        self.tableWidget_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.setRowCount(7)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 0, item)

        self.retranslateUi(Traffic_view)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Traffic_view.back)
        QtCore.QMetaObject.connectSlotsByName(Traffic_view)

    def retranslateUi(self, Traffic_view):
        Traffic_view.setWindowTitle(_translate("Traffic_view", "Form", None))
        self.pushButton.setText(_translate("Traffic_view", "뒤로가기", None))
        self.label.setText(_translate("Traffic_view", "고속도로 교통 상황(서울-지방) 전체보기", None))
        self.groupBox.setTitle(_translate("Traffic_view", "교통량 정보", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Traffic_view", "전국", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Traffic_view", "서울방향", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Traffic_view", "지방방향", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Traffic_view", "교통량", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_2.setTitle(_translate("Traffic_view", "조회 날짜/시간", None))
        self.textEdit.setHtml(_translate("Traffic_view", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">날짜 : </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">시간 : </p></body></html>", None))
        self.groupBox_3.setTitle(_translate("Traffic_view", "서울->지방", None))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("Traffic_view", "서울->대전", None))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("Traffic_view", "서울->대구", None))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("Traffic_view", "서울->울산", None))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("Traffic_view", "서울->부산", None))
        item = self.tableWidget_3.verticalHeaderItem(4)
        item.setText(_translate("Traffic_view", "서울->광주", None))
        item = self.tableWidget_3.verticalHeaderItem(5)
        item.setText(_translate("Traffic_view", "서울->목포", None))
        item = self.tableWidget_3.verticalHeaderItem(6)
        item.setText(_translate("Traffic_view", "서울->강릉", None))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Traffic_view", "소요 시간", None))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.groupBox_4.setTitle(_translate("Traffic_view", "지방->서울", None))
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("Traffic_view", "대전->서울", None))
        item = self.tableWidget_4.verticalHeaderItem(1)
        item.setText(_translate("Traffic_view", "대구->서울", None))
        item = self.tableWidget_4.verticalHeaderItem(2)
        item.setText(_translate("Traffic_view", "울산->서울", None))
        item = self.tableWidget_4.verticalHeaderItem(3)
        item.setText(_translate("Traffic_view", "부산->서울", None))
        item = self.tableWidget_4.verticalHeaderItem(4)
        item.setText(_translate("Traffic_view", "광주->서울", None))
        item = self.tableWidget_4.verticalHeaderItem(5)
        item.setText(_translate("Traffic_view", "목포->서울", None))
        item = self.tableWidget_4.verticalHeaderItem(6)
        item.setText(_translate("Traffic_view", "강릉->서울", None))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Traffic_view", "소요 시간", None))
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)
