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