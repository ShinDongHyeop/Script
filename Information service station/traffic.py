from xml.dom.minidom import parse, parseString # minidom ����� �Ľ� �Լ��� ����Ʈ�մϴ�.
from xml.etree import ElementTree
import urllib.request

loopFlag = 1
xmlFD = -1

Traffic = None

def launcherFunction2():
    global Traffic
    Traffic = LoadURLFromFile()

def LoadURLFromFile():
    global xmlFD
    try:
        url = "http://data.ex.co.kr/exopenapi/safeDriving/forecast?serviceKey=fVnRg9PFJsGQduJvy%2FBg69zEoIB9xNeC5JOxRuIq1xK%2FX0ZV8JIcOz0U3qKHBMEkg1rKbRwb6s5tyfOSccaQjg%3D%3D&type=xml"
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

def checkDocument():
    global Traffic
    if Traffic == None:
        print("Error : Document is empty")
        return False
    return True

def PrintTest2():
    global Traffic
    if not checkDocument():  # DOM이 None인지 검사합니다.
        return None

    Trafficlist = Traffic.childNodes
    Traffic = Trafficlist[0].childNodes
    return Traffic

def GetItem():
    Trafficlist = PrintTest2()
    Itemlist = []

    for item in Trafficlist:
        if item.nodeName == "list":  # 엘리먼트를 중 book인 것을 골라 냅니다.
            subitems = item.childNodes  # book에 들어 있는 노드들을 가져옵니다.
            for atom in subitems:
                if atom.nodeName in "unitName":
                    Itemlist.append(atom.firstChild.nodeValue)

    return Itemlist
