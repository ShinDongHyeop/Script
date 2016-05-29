# -*- conding: [인코딩] -*-

from xml.dom.minidom import parse, parseString # minidom ����� �Ľ� �Լ��� ����Ʈ�մϴ�.
from xml.etree import ElementTree
import urllib.request

##### global
loopFlag = 1
xmlFD = -1

BooksDoc = None

#### Menu  implementation
def printMenu():
    print("Welcome! Book Manager Program (xml version)")
    print("========Menu==========")
    print("Load xml:        l")
    print("print Book list: b")
    print("Search :         s")
    print("Quit program:    q")
    print("==================")

def launcherFunction(menu):
    global BooksDoc
    if menu ==  'l':
        BooksDoc = LoadURLFromFile()
    elif menu == 'q':
        QuitBookMgr()
    elif menu == 'b':
        PrintBookList()
    elif menu == 's':
        SearchMenu()
        Select = str(input ('선택 : '))
        printBookList(Search(Select))
    else:
        print ("error : unknow menu key")


def SearchMenu():
    print("========Menu========")
    print("BatchMenu = 1")
    print("Brand = 2")
    print("Convenience = 3")
    print("Direction = 4")
    print("MainteanaceYn = 5")
    print("ServiceAreaCode = 6")
    print("ServiceAreaName = 7")
    print("TelNo = 8")
    print("TruckSaYn = 9")
    print("========================")

def Search(tag):
    global BooksDoc
    global xmlFD
    retlist = []
    if not checkDocument():
        return None
    
    try:
        tree = ElementTree.fromstring(str(BooksDoc.toxml()))
        keyword = str(input ('input keyword to search :'))
    except Exception:
        print ("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None
    
    # Book 엘리먼트 리스트를 가져 옵니다.
    bookElements = tree.getiterator("list")
    
    if tag == '1':
        for item in bookElements:
            strTitle = item.find("batchMenu")
            if strTitle != None:
                if (strTitle.text.find(keyword) >=0):
                    retlist.append(strTitle.text)
        return retlist
        
    elif tag == '2':
        for item in bookElements:
            strTitle = item.find("brand")
            if strTitle != None:
                if (strTitle.text.find(keyword) >=0):
                    retlist.append(strTitle.text)
        return retlist

    elif tag == '3':
        for item in bookElements:
            strTitle = item.find("convenience")
            if strTitle != None:
                if (strTitle.text.find(keyword) >=0):
                    retlist.append(strTitle.text)
        return retlist

    elif tag == '4':
        for item in bookElements:
            strTitle = item.find("direction")
            if strTitle != None:
                if (strTitle.text.find(keyword) >=0):
                    retlist.append(strTitle.text)
        return retlist
        
    elif tag == '5':
        for item in bookElements:
            strTitle = item.find("maintenanceYn")
            if strTitle != None:
                if (strTitle.text.find(keyword) >=0):
                    retlist.append(strTitle.text)
        return retlist
        
    elif tag == '6':
        for item in bookElements:
            strTitle = item.find("serviceAreaCode")
            if strTitle != None:
                if (strTitle.text.find(keyword) >=0):
                    retlist.append(strTitle.text)
        return retlist
        
    elif tag == '7':
        for item in bookElements:
            strTitle = item.find("serviceAreaName")
            if strTitle != None:
                if (strTitle.text.find(keyword) >=0):
                    retlist.append(strTitle.text)
        return retlist
        
    elif tag == '8':
        for item in bookElements:
            strTitle = item.find("telNo")
            if strTitle != None:
                if (strTitle.text.find(keyword) >=0):
                    retlist.append(strTitle.text)
        return retlist
        
    elif tag == '9':
        for item in bookElements:
            strTitle = item.find("truckSaYn")
            if strTitle != None:
                if (strTitle.text.find(keyword) >=0):
                    retlist.append(strTitle.text)
        return retlist
def checkDocument():
    global BooksDoc
    if BooksDoc == None:
        print("Error : Document is empty")
        return False
    return True

def BooksFree():
    if checkDocument():
        BooksDoc.unlink()   # minidom 객체 해제합니다.

def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()

def PrintDOMtoXML():
    if checkDocument():
        print(BooksDoc.toxml())

def LoadURLFromFile():
    global xmlFD
    try:
        url = "http://data.ex.co.kr/exopenapi/business/conveniServiceArea?serviceKey=fVnRg9PFJsGQduJvy%2FBg69zEoIB9xNeC5JOxRuIq1xK%2FX0ZV8JIcOz0U3qKHBMEkg1rKbRwb6s5tyfOSccaQjg%3D%3D&type=xml"
        request = urllib.request.Request(url)
        xmlFD = urllib.request.urlopen(request)
    except IOError:
        print ("invalid file name or path")
        return None
    else:
        try:
            dom = parse(xmlFD)   # XML ������ �Ľ��մϴ�.
        except Exception:
            print ("loading fail!!!")
        else:
            print ("XML Document loading complete")
            return dom
    return None

def PrintBookList():  
    global BooksDoc  
    if not checkDocument():  # DOM이 None인지 검사합니다.  
        return None  
  
    booklist = BooksDoc.childNodes  
    book = booklist[0].childNodes  
    for item in book:  
        if item.nodeName == "list":  # 엘리먼트를 중 book인 것을 골라 냅니다.  
            subitems = item.childNodes  # book에 들어 있는 노드들을 가져옵니다.  
            for atom in subitems:  
                print("%s = "%atom.nodeName, atom.firstChild.nodeValue)  
            print("-------------------------------------------") 


def printBookList(blist):
    for res in blist:
        print (res)

while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
    
    
else:
    print ("Thank you! Good Bye")
# 수유실 / 강릉 / O / 110 / 강릉 / 061 / O