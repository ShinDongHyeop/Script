# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 400)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 191, 131))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("main.png")))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 451, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(230, 70, 361, 281))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 30, 301, 70))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_1)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 140, 301, 70))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 140, 301, 70))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_8 = QtGui.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(30, 30, 301, 70))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.pushButton_11 = QtGui.QPushButton(self.tab_3)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 30, 301, 70))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton = QtGui.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(20, 140, 301, 71))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_5)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 40, 301, 71))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 191, 131))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("main_2.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.facility_view)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.facility_serch)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.food_view)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.food_serch)
        QtCore.QObject.connect(self.pushButton_11, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.location_view)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.email_send)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.traffic_view)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "휴게소 정보 프로그램", None))
        self.pushButton_2.setText(_translate("MainWindow", "전체 보기", None))
        self.pushButton_3.setText(_translate("MainWindow", "검색", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "시설", None))
        self.pushButton_6.setText(_translate("MainWindow", "검색", None))
        self.pushButton_8.setText(_translate("MainWindow", "전체 보기", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "대표 음식", None))
        self.pushButton_11.setText(_translate("MainWindow", "국내 휴게소 위치 찾기", None))
        self.pushButton.setText(_translate("MainWindow", "서울-지방 간 교통상황 보기", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "위치", None))
        self.pushButton_4.setText(_translate("MainWindow", "데이터 이메일로 보내기", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "기타", None))

