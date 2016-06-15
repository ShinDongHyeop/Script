# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'location_view.ui'
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

class Ui_location_view(object):
    def setupUi(self, location_view):
        location_view.setObjectName(_fromUtf8("location_view"))
        location_view.resize(600, 400)
        self.label = QtGui.QLabel(location_view)
        self.label.setGeometry(QtCore.QRect(20, 20, 491, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(location_view)
        self.pushButton.setGeometry(QtCore.QRect(460, 360, 121, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox = QtGui.QGroupBox(location_view)
        self.groupBox.setGeometry(QtCore.QRect(10, 340, 421, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 20, 91, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(15, 25, 56, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(90, 20, 201, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.webView = QtWebKit.QWebView(location_view)
        self.webView.setEnabled(True)
        self.webView.setGeometry(QtCore.QRect(20, 60, 551, 271))
        self.webView.setMouseTracking(True)
        self.webView.setAcceptDrops(True)
        self.webView.setAutoFillBackground(False)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setZoomFactor(1.0)
        self.webView.setObjectName(_fromUtf8("webView"))

        self.retranslateUi(location_view)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), location_view.back)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), location_view.local_serch)
        QtCore.QMetaObject.connectSlotsByName(location_view)

    def retranslateUi(self, location_view):
        location_view.setWindowTitle(_translate("location_view", "Form", None))
        self.label.setText(_translate("location_view", "휴게소 위치 확인", None))
        self.pushButton.setText(_translate("location_view", "뒤로가기", None))
        self.groupBox.setTitle(_translate("location_view", "좌표 검색", None))
        self.pushButton_2.setText(_translate("location_view", "지도 검색하기", None))
        self.label_2.setText(_translate("location_view", "휴게소 명", None))

from PyQt4 import QtWebKit
