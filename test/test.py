import sys

from PyQt4 import QtGui, QtCore

from data import *
from test_root_ui import *
from test_nood1_ui import *
from test_nood1_1_ui import *
from test_nood1_2_ui import *
from test_nood1_3_ui import *
from test_nood2_ui import *
from test_nood2_1_ui import *
from test_nood2_2_ui import *
from test_nood2_3_ui import *
from test_nood3_ui import *
from test_nood4_ui import *


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def slot1_nood1(self):
        launcherFunction('l')
        self.nood1 = Nood1Form()
        self.nood1.show()
        self.close()
        return

    def slot1_nood2(self):
        self.nood2 = Nood2Form()
        self.nood2.show()
        self.close()
        return

    def slot1_nood3(self):
        self.nood3 = Nood3Form()
        self.nood3.show()
        self.close()
        return

    def slot1_nood4(self):
        self.nood4 = Nood4Form()
        self.nood4.show()
        self.close()
        return

class Nood1Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood1()
        self.ui.setupUi(self)

    def slot1_root(self):
        self.root = MyForm()
        self.root.show()
        self.close()
        return

    def slot1_nood1_1(self):
        self.nood1 = Nood1_1Form()
        self.nood1.show()
        self.close()
        return

    def slot1_nood1_2(self):
        self.nood2 = Nood1_2Form()
        self.nood2.show()
        self.close()
        return

    def slot1_nood1_3(self):
        self.nood3 = Nood1_3Form()
        self.nood3.show()
        self.close()
        return

class Nood1_1Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood1_1()
        self.ui.setupUi(self)

        book = PrintTest()
        size = 0
        for item in book:
            if item.nodeName in "list":
                size += 1
        self.ui.tableWidget.setRowCount(size)
        widget = 0
        for item in book:
            if item.nodeName == "list":  # 엘리먼트를 중 book인 것을 골라 냅니다.
                subitems = item.childNodes  # book에 들어 있는 노드들을 가져옵니다.
                for atom in subitems:
                    if atom.nodeName in "serviceAreaName":
                        data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                        self.ui.tableWidget.setItem(widget, 0, data)
                    if atom.nodeName in "direction":
                        data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                        self.ui.tableWidget.setItem(widget, 1, data)
                    if atom.nodeName in "convenience":
                        data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                        self.ui.tableWidget.setItem(widget, 2, data)
                    if atom.nodeName in "telNo":
                        data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                        self.ui.tableWidget.setItem(widget, 3, data)

                widget += 1

    def slot1_nood1(self):
        self.nood = Nood1Form()
        self.nood.show()
        self.close()
        return

class Nood1_2Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood1_2()
        self.ui.setupUi(self)

    def slot1_nood1(self):
        self.nood = Nood1Form()
        self.nood.show()
        self.close()
        return

    def slot1_serch(self):
        self.ui.tableWidget.clear()
        book = PrintTest()
        tag = self.ui.comboBox.currentText()
        if tag == '휴게소명':
            tag = "serviceAreaName"
        else:
            tag = "direction"
        keyword = self.ui.textEdit.toPlainText()
        size = 0
        for item in book:
            if item.nodeName in "list":
                subitems = item.childNodes  # book에 들어 있는 노드들을 가져옵니다.
                for atom in subitems:
                    if ((atom.firstChild.nodeValue in keyword) and (atom.nodeName in tag)):
                        size += 1
        self.ui.tableWidget.setRowCount(size)
        widget = 0
        for item in book:
            if item.nodeName == "list":  # 엘리먼트를 중 book인 것을 골라 냅니다.
                subitems = item.childNodes  # book에 들어 있는 노드들을 가져옵니다.
                for atom in subitems:
                    if ((atom.firstChild.nodeValue in keyword) and (atom.nodeName in tag)):
                        for Item in subitems:
                            if Item.nodeName in "serviceAreaName":
                                data = QtGui.QTableWidgetItem(Item.firstChild.nodeValue)
                                self.ui.tableWidget.setItem(widget, 0, data)
                            if Item.nodeName in "direction":
                                data = QtGui.QTableWidgetItem(Item.firstChild.nodeValue)
                                self.ui.tableWidget.setItem(widget, 1, data)
                            if Item.nodeName in "convenience":
                                data = QtGui.QTableWidgetItem(Item.firstChild.nodeValue)
                                self.ui.tableWidget.setItem(widget, 2, data)
                            if Item.nodeName in "telNo":
                                data = QtGui.QTableWidgetItem(Item.firstChild.nodeValue)
                                self.ui.tableWidget.setItem(widget, 3, data)
                        widget += 1

class Nood1_3Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood1_3()
        self.ui.setupUi(self)

    def slot1_nood1(self):
        self.nood = Nood1Form()
        self.nood.show()
        self.close()
        return

    def dialog_add(self):
        d = QtGui.QDialog()
        b1 = QtGui.QPushButton("성공!", d)
        b1.move(50, 50)
        d.setWindowTitle("추가하기")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()

    def dialog_chang(self):
        d = QtGui.QDialog()
        b1 = QtGui.QPushButton("성공!", d)
        b1.move(50, 50)
        d.setWindowTitle("변경하기")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()

    def dialog_delete(self):
        d = QtGui.QDialog()
        b1 = QtGui.QPushButton("성공!", d)
        b1.move(50, 50)
        d.setWindowTitle("삭제하기")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()

class Nood2Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood2()
        self.ui.setupUi(self)

    def slot1_root(self):
        self.root = MyForm()
        self.root.show()
        self.close()
        return
    def slot1_nood2_1(self):
        self.nood1 = Nood2_1Form()
        self.nood1.show()
        self.close()
        return

    def slot1_nood2_2(self):
        self.nood2 = Nood2_2Form()
        self.nood2.show()
        self.close()
        return

    def slot1_nood2_3(self):
        self.nood3 = Nood2_3Form()
        self.nood3.show()
        self.close()
        return

class Nood2_1Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood2_1()
        self.ui.setupUi(self)

    def slot1_nood2(self):
        self.nood = Nood2Form()
        self.nood.show()
        self.close()
        return

class Nood2_2Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood2_2()
        self.ui.setupUi(self)

    def slot1_nood2(self):
        self.nood = Nood2Form()
        self.nood.show()
        self.close()
        return

    def slot1_serch(self):
        return

class Nood2_3Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood2_3()
        self.ui.setupUi(self)

    def slot1_nood2(self):
        self.nood = Nood2Form()
        self.nood.show()
        self.close()
        return

    def dialog_add(self):
        d = QtGui.QDialog()
        b1 = QtGui.QPushButton("성공!", d)
        b1.move(50, 50)
        d.setWindowTitle("추가하기")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()

    def dialog_chang(self):
        d = QtGui.QDialog()
        b1 = QtGui.QPushButton("성공!", d)
        b1.move(50, 50)
        d.setWindowTitle("변경하기")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()

    def dialog_delete(self):
        d = QtGui.QDialog()
        b1 = QtGui.QPushButton("성공!", d)
        b1.move(50, 50)
        d.setWindowTitle("삭제하기")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()

class Nood3Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood3()
        self.ui.setupUi(self)

    def slot1_root(self):
        self.root = MyForm()
        self.root.show()
        self.close()
        return

class Nood4Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood4()
        self.ui.setupUi(self)

    def slot1_root(self):
        self.root = MyForm()
        self.root.show()
        self.close()
        return

app = QtGui.QApplication(sys.argv)
myapp = MyForm()
myapp.show()
app.exec_()