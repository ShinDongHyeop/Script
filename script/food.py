# -*- conding: [인코딩] -*-

from xml.dom.minidom import parse, parseString # minidom ����� �Ľ� �Լ��� ����Ʈ�մϴ�.
from xml.etree import ElementTree
import urllib.request

##### global
loopFlag = 1
xmlFD = -1

BooksDoc2 = None

#### Menu  implementation
def printMenu():
    print("�nWelcome! Book Manager Program (xml version)")
    print("========Menu==========")
    print("Load xml:  L")
    print("==================")

def launcherFunction2(menu):
    global BooksDoc2
    if menu ==  'L':
        BooksDoc2 = LoadURLFromFile()
    else:
        print ("error : unknow menu key")

def checkDocument():
    global BooksDoc2
    if BooksDoc2 == None:
        print("Error : Document is empty")
        return False
    return True

def BooksFree():
    if checkDocument():
        BooksDoc2.unlink()   # minidom 객체 해제합니다.

def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()

def PrintDOMtoXML():
    if checkDocument():
        print(BooksDoc2.toxml())

def LoadURLFromFile():
    global xmlFD
    try:
        url = "http://data.ex.co.kr/exopenapi/business/representFoodServiceArea?serviceKey=fVnRg9PFJsGQduJvy%2FBg69zEoIB9xNeC5JOxRuIq1xK%2FX0ZV8JIcOz0U3qKHBMEkg1rKbRwb6s5tyfOSccaQjg%3D%3D&type=xml"
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

def PrintTest2():
    global BooksDoc2
    if not checkDocument():  # DOM이 None인지 검사합니다.
        return None

    booklist = BooksDoc2.childNodes
    book = booklist[0].childNodes
    return book
    
def printBookList(blist):
    for res in blist:
        print (res)
