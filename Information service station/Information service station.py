import sys

from PyQt4 import QtGui, QtCore

import facility
import food
import local
import traffic
from mainUI import *
from facility_eidt_UI import *
from facility_serch_UI import *
from facility_view_UI import *
from food_edit_UI import *
from food_serch_UI import *
from food_view_UI import *
from Traffic_view_UI import *
from location_view_UI import *
from email_UI import *

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        facility.launcherFunction('l')
        food.launcherFunction2('L')
        local.launcherFunction2()
        traffic.launcherFunction2()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def facility_view(self):
        self.nood1 = facility_view_class()
        self.nood1.show()
        self.close()
        return

    def facility_serch(self):
        self.nood2 = facility_serch_class()
        self.nood2.show()
        self.close()
        return

    def facility_edit(self):
        self.nood3 = facility_edit_class()
        self.nood3.show()
        self.close()
        return

    def food_view(self):
        self.nood4 = food_view_class()
        self.nood4.show()
        self.close()
        return

    def food_serch(self):
        self.nood2 = food_serch_class()
        self.nood2.show()
        self.close()
        return

    def food_edit(self):
        self.nood3 = food_edit_class()
        self.nood3.show()
        self.close()
        return

    def location_view(self):
        self.location = location_view_class()
        self.location.show()
        self.close()
        return


    def traffic_view(self):
        self.traffic = traffic_view_class()
        self.traffic.show()
        self.close()
        return

    def email_send(self):
        self.email = email_send_class()
        self.email.show()
        self.close()
        return

class facility_view_class(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood1_1()
        self.ui.setupUi(self)

        book = facility.PrintTest()
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
                    if atom.nodeName in "routeName":
                        data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                        self.ui.tableWidget.setItem(widget, 1, data)
                    if atom.nodeName in "direction":
                        data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                        self.ui.tableWidget.setItem(widget, 2, data)
                    if atom.nodeName in "convenience":
                        data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                        self.ui.tableWidget.setItem(widget, 3, data)
                    if atom.nodeName in "telNo":
                        data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                        self.ui.tableWidget.setItem(widget, 4, data)

                widget += 1

    def slot1_nood1(self):
        global myapp
        myapp.show()
        self.close()
        return

class facility_serch_class(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood1_2()
        self.ui.setupUi(self)

    def slot1_nood1(self):
        global myapp
        myapp.show()
        self.close()
        return

    def slot1_serch(self):
        self.ui.tableWidget.clear()
        book = facility.PrintTest()
        tag = self.ui.comboBox.currentText()
        if tag == '휴게소명':
            tag = "serviceAreaName"
        else:
            tag = "routeName"
        keyword = self.ui.textEdit.toPlainText()
        self.show()
        itemlist = facility.Search(keyword, tag)
        size = 0
        if itemlist != None :
            size = len(itemlist)
        self.ui.tableWidget.setRowCount(size)
        widget = 0

        if size > 0 :
            for item in book:
                if item.nodeName == "list":  # 엘리먼트를 중 book인 것을 골라 냅니다.
                    subitems = item.childNodes  # book에 들어 있는 노드들을 가져옵니다.
                    for atom in subitems:
                        if ((atom.firstChild.nodeValue == itemlist[widget%size]) and (atom.nodeName in tag) and widget < size):
                            for Item in subitems:
                                if Item.nodeName in "serviceAreaName":
                                    data = QtGui.QTableWidgetItem(Item.firstChild.nodeValue)
                                    self.ui.tableWidget.setItem(widget, 0, data)
                                if Item.nodeName in "routeName":
                                    data = QtGui.QTableWidgetItem(Item.firstChild.nodeValue)
                                    self.ui.tableWidget.setItem(widget, 1, data)
                                if Item.nodeName in "direction":
                                    data = QtGui.QTableWidgetItem(Item.firstChild.nodeValue)
                                    self.ui.tableWidget.setItem(widget, 2, data)
                                if Item.nodeName in "convenience":
                                    data = QtGui.QTableWidgetItem(Item.firstChild.nodeValue)
                                    self.ui.tableWidget.setItem(widget, 3, data)
                                if Item.nodeName in "telNo":
                                    data = QtGui.QTableWidgetItem(Item.firstChild.nodeValue)
                                    self.ui.tableWidget.setItem(widget, 4, data)
                            widget += 1

        self.show()
        return

class facility_edit_class(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood1_3()
        self.ui.setupUi(self)

    def slot1_nood1(self):
        global myapp
        myapp.show()
        self.close()
        return

    def dialog_add(self):
        Adddata = {'list' : list }
        text = self.ui.textEdit.toPlainText()
        if text:
            Adddata['routeName'] = text
        else :
            Adddata['routeName'] = ' '
        text = self.ui.textEdit_2.toPlainText()
        if text:
            Adddata['direction'] = text
        else:
            Adddata['direction'] = ' '
        text = self.ui.textEdit_3.toPlainText()
        if text:
            Adddata['serviceAreaName'] = text
        else:
            Adddata['serviceAreaName'] = ' '
        text = self.ui.textEdit_4.toPlainText()
        if text:
            Adddata['telNo'] = text
        else:
            Adddata['telNo'] = ' '
        text = self.ui.textEdit_6.toPlainText()
        if text:
            Adddata['convenience'] = text
        else:
            Adddata['convenience'] = ' '
        text = self.ui.textEdit_5.toPlainText()
        if text:
            Adddata['brand'] = text
        else:
            Adddata['brand'] = ' '
        text = self.ui.textEdit_9.toPlainText()
        if text:
            Adddata['batchMenu'] = text
        else:
            Adddata['batchMenu'] = ' '

        check= self.ui.buttonGroup.checkedButton()
        if check == self.ui.radioButton :
            Adddata['maintenanceYn'] = 'O'
        elif check == self.ui.radioButton_2 :
            Adddata['maintenanceYn'] = 'X'

        check = self.ui.buttonGroup_2.checkedButton()
        if check == self.ui.radioButton_4:
            Adddata['truckSaYn'] = 'O'
        elif check == self.ui.radioButton_3:
            Adddata['truckSaYn'] = 'X'

        facility.Addfacility(Adddata)

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

class food_view_class(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood2_1()
        self.ui.setupUi(self)

        book = food.PrintTest2()
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
                    if atom.nodeName in "routeName":
                        data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                        self.ui.tableWidget.setItem(widget, 1, data)
                    if atom.nodeName in "direction":
                        data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                        self.ui.tableWidget.setItem(widget, 2, data)
                    if atom.nodeName in "batchMenu": # 메뉴
                        data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                        self.ui.tableWidget.setItem(widget, 3, data)
                    if atom.nodeName in "salePrice": # 가격
                        data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                        self.ui.tableWidget.setItem(widget, 4, data)
                widget += 1

    def slot1_nood2(self):
        global myapp
        myapp.show()
        self.close()
        return

class food_serch_class(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood2_2()
        self.ui.setupUi(self)

    def slot1_nood2(self):
        global myapp
        myapp.show()
        self.close()
        return

    def slot1_serch(self):
        self.ui.tableWidget.clear()
        book = food.PrintTest2()

        tag = self.ui.comboBox.currentText()
        if tag == '고속도로명':
            tag = "routeName"
        else:
            tag = "direction"
        keyword = self.ui.textEdit.toPlainText()
        itemlist = facility.Search(keyword, tag)
        size = 0
        if itemlist != None:
            size = len(itemlist)
        self.ui.tableWidget.setRowCount(size)
        widget = 0

        for item in book:
            if item.nodeName == "list":  # 엘리먼트를 중 book인 것을 골라 냅니다.
                subitems = item.childNodes  # book에 들어 있는 노드들을 가져옵니다.
                for atom in subitems:
                    if ((atom.firstChild.nodeValue in itemlist[widget%size]) and (atom.nodeName in tag) and widget < size):
                        for Item in subitems:
                            if Item.nodeName in "serviceAreaName":
                                data = QtGui.QTableWidgetItem(Item.firstChild.nodeValue)
                                self.ui.tableWidget.setItem(widget, 0, data)
                            if Item.nodeName in "routeName":
                                data = QtGui.QTableWidgetItem(Item.firstChild.nodeValue)
                                self.ui.tableWidget.setItem(widget, 1, data)
                            if Item.nodeName in "direction":
                                data = QtGui.QTableWidgetItem(Item.firstChild.nodeValue)
                                self.ui.tableWidget.setItem(widget, 2, data)
                            if Item.nodeName in "batchMenu":
                                data = QtGui.QTableWidgetItem(Item.firstChild.nodeValue)
                                self.ui.tableWidget.setItem(widget, 3, data)
                            if Item.nodeName in "salePrice":
                                data = QtGui.QTableWidgetItem(Item.firstChild.nodeValue)
                                self.ui.tableWidget.setItem(widget, 4, data)
                        widget += 1

        self.show()
        return

class food_edit_class(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form_nood2_3()
        self.ui.setupUi(self)

    def slot1_nood2(self):
        global myapp
        myapp.show()
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

class traffic_view_class(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Traffic_view()
        self.ui.setupUi(self)

        trafficdata = traffic.PrintTest2()

        DayData = '날짜: '
        TimeData = '시간: '

        for item in trafficdata:
            if item.nodeName == "list":
                subitems = item.childNodes
                for atom in subitems:
                        if atom.nodeName in "sdate":
                            DayData = DayData + atom.firstChild.nodeValue
                        if atom.nodeName in "stime":
                            TimeData = TimeData + atom.firstChild.nodeValue
                        if atom.nodeName in "cjunkook":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget.setItem(0, 0, data)
                        if atom.nodeName in "cjibangDir":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget.setItem(1, 0, data)
                        if atom.nodeName in "cseoulDir":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget.setItem(2, 0, data)
                        if atom.nodeName in "csudj":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget_3.setItem(0, 0, data)
                        if atom.nodeName in "csudg":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget_3.setItem(1, 0, data)
                        if atom.nodeName in "csuus":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget_3.setItem(2, 0, data)
                        if atom.nodeName in "csubs":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget_3.setItem(3, 0, data)
                        if atom.nodeName in "csugj":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget_3.setItem(4, 0, data)
                        if atom.nodeName in "csump":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget_3.setItem(5, 0, data)
                        if atom.nodeName in "csukr":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget_3.setItem(6, 0, data)
                        if atom.nodeName in "cdjsu":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget_4.setItem(0, 0, data)
                        if atom.nodeName in "cdgsu":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget_4.setItem(1, 0, data)
                        if atom.nodeName in "cussu":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget_4.setItem(2, 0, data)
                        if atom.nodeName in "cbssu":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget_4.setItem(3, 0, data)
                        if atom.nodeName in "cgjsu":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget_4.setItem(4, 0, data)
                        if atom.nodeName in "cmpsu":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget_4.setItem(5, 0, data)
                        if atom.nodeName in "ckrsu":
                            data = QtGui.QTableWidgetItem(atom.firstChild.nodeValue)
                            self.ui.tableWidget_4.setItem(6, 0, data)

        self.ui.textEdit.setText(DayData + "\n" + TimeData)

    def back(self):
        global myapp
        myapp.show()
        self.close()
        return

class location_view_class(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_location_view()
        self.ui.setupUi(self)
        itemlist = local.GetItem()
        self.ui.comboBox.addItems(itemlist)

    def local_serch(self):
        localdata = local.PrintTest2()
        lox, loy = '',''
        keywoard = self.ui.comboBox.currentText()

        for item in localdata:
            if item.nodeName == "list":  # 엘리먼트를 중 book인 것을 골라 냅니다.
                subitems = item.childNodes  # book에 들어 있는 노드들을 가져옵니다.
                for atom in subitems:
                    if atom.firstChild.nodeValue in keywoard:
                        for Item in subitems:
                            if Item.nodeName in "xValue":
                                lox = Item.firstChild.nodeValue
                            if Item.nodeName in "yValue":
                                loy = Item.firstChild.nodeValue

        self.ui.webView.setUrl(QtCore.QUrl("https://maps.google.co.kr/maps/@" + loy + "," + lox + ",19z"))
        self.show()
        return

    def back(self):
        global myapp
        myapp.show()
        self.close()
        return

class email_send_class(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_email()
        self.ui.setupUi(self)

    def send_mail(self):
        return

    def back(self):
        global myapp
        myapp.show()
        self.close()
        return

myapp = None

def main():
    global myapp
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    app.exec_()

if __name__ == '__main__':
    main()