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
    print("�nWelcome! Book Manager Program (xml version)")
    print("========Menu==========")
    print("Load xml:  l")
    print("Print dom to xml: p")
    print("Quit program:   q")
    print("print Book list: b")
    print("Add new book: a")
    print("sEarch Book Title: e")
    print("Make html: m")
    print("==================")

def launcherFunction(menu):
    global BooksDoc
    if menu ==  'l':
        BooksDoc = LoadURLFromFile()
    elif menu == 'q':
        QuitBookMgr()
    elif menu == 'p':
        PrintDOMtoXML()
    elif menu == 'b':
        PrintBookList(["batchMenu", ])
    elif menu == 'a':
        batchMenu = str(input ('insert batchMenu :'))
        AddBook({'list': list, 'batchMenu':batchMenu})
    elif menu == 'e':
        Select = str(input('선택 : '))
        printBookList(Search(Select))
    else:
        print ("error : unknow menu key")

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

def PrintBookList(tags):
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

def PrintTest():
    global BooksDoc
    if not checkDocument():  # DOM이 None인지 검사합니다.
        return None

    booklist = BooksDoc.childNodes
    book = booklist[0].childNodes
    return book

def printBookList(blist):
    for res in blist:
        print (res)

def AddBook(bookdata):
    global BooksDoc
    if not checkDocument() :
        return None

    # Book 엘리먼트를 만듭니다.
    newBook = BooksDoc.createElement('list')
    newBook.setAttribute('list', bookdata['list'])
    # Title 엘리먼트를 만듭니다.
    titleEle = BooksDoc.createElement('batchMenu')
    # 텍스트 에릴먼트를 만듭니다.
    titleNode = BooksDoc.createTextNode(bookdata['batchMenu'])
    # 텍스트 노드와 Title 엘리먼트를 연결 시킵니다.
    try:
        titleEle.appendChild(titleNode)
    except Exception:
        print ("append child fail- please,check the parent element & node!!!")
        return None
    else:
        titleEle.appendChild(titleNode)

    # Title를 book 엘리먼트와 연결 시킵니다.
    try:
        newBook.appendChild(titleEle)
        booklist = BooksDoc.firstChild
    except Exception:
        print ("append child fail- please,check the parent element & node!!!")
        return None
    else:
        if booklist != None:
            booklist.appendChild(newBook)

def Sch(tag, keywoad):
    global BooksDoc
    global xmlFD

    pass

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

    if tag == '3':
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
