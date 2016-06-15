import sys
import collections

from PyQt4 import QtGui, QtCore

import facility
import food
import local
import traffic
import email_data
from mainUI import *
from UI_Fome import *
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

    def data_edit(self):
        self.mail_data = ''
        datalist = collections.OrderedDict()
        datalist['날짜: '] = ''
        datalist['시간: '] = ''
        datalist['전국교통량: '] = ''
        datalist['서울방향 교통량: '] = ''
        datalist['지방방량 교통량: '] = ''
        datalist['서울->대전: '] = ''
        datalist['서울->대구: '] = ''
        datalist['서울->울산: '] = ''
        datalist['서울->부산: '] = ''
        datalist['서울->광주: '] = ''
        datalist['서울->목포: '] = ''
        datalist['서울->강릉: '] = ''
        datalist['대전->서울: '] = ''
        datalist['대구->서울: '] = ''
        datalist['울산->서울: '] = ''
        datalist['부산->서울: '] = ''
        datalist['광주->서울: '] = ''
        datalist['목포->서울: '] = ''
        datalist['강릉->서울: '] = ''
        
        trafficdata = traffic.PrintTest2()

        for item in trafficdata:
            if item.nodeName == "list":
                subitems = item.childNodes
                for atom in subitems:
                    if atom.nodeName in "sdate":
                        datalist['날짜: '] =  atom.firstChild.nodeValue
                    if atom.nodeName in "stime":
                        datalist['시간: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "cjunkook":
                        datalist['전국교통량: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "cjibangDir":
                        datalist['서울방향 교통량: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "cseoulDir":
                        datalist['지방방량 교통량: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "csudj":
                        datalist['서울->대전: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "csudg":
                        datalist['서울->대구: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "csuus":
                        datalist['서울->울산: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "csubs":
                        datalist['서울->부산: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "csugj":
                        datalist['서울->광주: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "csump":
                        datalist['서울->목포: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "csukr":
                        datalist['서울->강릉: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "cdjsu":
                        datalist['대전->서울: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "cdgsu":
                        datalist['대구->서울: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "cussu":
                        datalist['울산->서울: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "cbssu":
                        datalist['부산->서울: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "cgjsu":
                        datalist['광주->서울: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "cmpsu":
                        datalist['목포->서울: '] = atom.firstChild.nodeValue
                    if atom.nodeName in "ckrsu":
                        datalist['강릉->서울: '] = atom.firstChild.nodeValue

        for key,item in datalist.items():
            self.mail_data = self.mail_data + key + item + '<br>'

        return self.mail_data

    def send_mail(self):
        addr = self.ui.lineEdit.text() + '@' + self.ui.lineEdit_2.text()
        email_data.send('Traffic_data',addr,self.data_edit())
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