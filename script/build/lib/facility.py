# -*- conding: [인코딩] -*-

from xml.dom.minidom import parse, parseString # minidom ����� �Ľ� �Լ��� ����Ʈ�մϴ�.
from xml.etree import ElementTree
import urllib.request

##### global
loopFlag = 1
xmlFD = -1

facilitysDoc = None

#### Menu  implementation
def printMenu():
    print("�nWelcome! facility Manager Program (xml version)")
    print("========Menu==========")
    print("Load xml:  l")
    print("Print dom to xml: p")
    print("Quit program:   q")
    print("print facility list: b")
    print("Add new facility: a")
    print("sEarch facility Title: e")
    print("Make html: m")
    print("==================")

def launcherFunction(menu):
    global facilitysDoc
    if menu ==  'l':
        facilitysDoc = LoadURLFromFile()
    elif menu == 'q':
        QuitfacilityMgr()
    elif menu == 'p':
        PrintDOMtoXML()
    elif menu == 'b':
        PrintfacilityList(["batchMenu", ])
    elif menu == 'a':
        batchMenu = str(input ('insert batchMenu :'))
        Addfacility({'list': list, 'batchMenu':batchMenu})
    elif menu == 'e':
        Select = str(input('선택 : '))
        printfacilityList(Search(Select))
    else:
        print ("error : unknow menu key")

def checkDocument():
    global facilitysDoc
    if facilitysDoc == None:
        print("Error : Document is empty")
        return False
    return True

def facilitysFree():
    if checkDocument():
        facilitysDoc.unlink()   # minidom 객체 해제합니다.

def QuitfacilityMgr():
    global loopFlag
    loopFlag = 0
    facilitysFree()

def PrintDOMtoXML():
    if checkDocument():
        print(facilitysDoc.toxml())

def LoadURLFromFile():
    global xmlFD
    try:
        url = "http://data.ex.co.kr/exopenapi/business/serviceAreaRoute?serviceKey=fVnRg9PFJsGQduJvy%2FBg69zEoIB9xNeC5JOxRuIq1xK%2FX0ZV8JIcOz0U3qKHBMEkg1rKbRwb6s5tyfOSccaQjg%3D%3D&type=xml"
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

def PrintfacilityList(tags):
    global facilitysDoc
    if not checkDocument():  # DOM이 None인지 검사합니다.
        return None

    facilitylist = facilitysDoc.childNodes
    facility = facilitylist[0].childNodes
    for item in facility:
        if item.nodeName == "list":  # 엘리먼트를 중 facility인 것을 골라 냅니다.
            subitems = item.childNodes  # facility에 들어 있는 노드들을 가져옵니다.
            for atom in subitems:
                print("%s = "%atom.nodeName, atom.firstChild.nodeValue)
            print("-------------------------------------------")

def PrintTest():
    global facilitysDoc
    if not checkDocument():  # DOM이 None인지 검사합니다.
        return None

    facilitylist = facilitysDoc.childNodes
    facility = facilitylist[0].childNodes
    return facility

def printfacilityList(blist):
    for res in blist:
        print (res)

def Addfacility(facilitydata):
    global facilitysDoc
    if not checkDocument() :
        return None

    # facility 엘리먼트를 만듭니다.
    newfacility = facilitysDoc.createElement('list')
    newfacility.setAttribute('list', facilitydata['list'])
    # Title 엘리먼트를 만듭니다.
    for key in facilitydata.keys() :
        if key != 'list':
            titleEle = facilitysDoc.createElement(key)
    # 텍스트 에릴먼트를 만듭니다.
            titleNode = facilitysDoc.createTextNode(facilitydata[key])
    # 텍스트 노드와 Title 엘리먼트를 연결 시킵니다.
            try:
                titleEle.appendChild(titleNode)
            except Exception:
                print ("append child fail- please,check the parent element & node!!!")
                return None
            else:
                titleEle.appendChild(titleNode)

    # Title를 facility 엘리먼트와 연결 시킵니다.
            newfacility.appendChild(titleEle)
    facilitylist = facilitysDoc.firstChild

    if facilitylist != None:
        facilitylist.appendChild(newfacility)

def Sch(tag, keywoad):
    global facilitysDoc
    global xmlFD

    pass

def Search(keyword, tag):
    global facilitysDoc
    global dom

    retlist = []
    if not checkDocument():
        return None

    try:
        tree = ElementTree.fromstring(str(facilitysDoc.toxml()))
    except Exception:
        print ("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None

    # facility 엘리먼트 리스트를 가져 옵니다.
    facilityElements = tree.getiterator("list")


    for item in facilityElements:
        strTitle = item.find(tag)
        if strTitle != None:
            if (strTitle.text.find(keyword) >=0):
                retlist.append(strTitle.text)
    return retlist
