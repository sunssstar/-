## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, pre, current
    # Case 1 : 하필 머리 앞에 삽입하기 (다현, 화사)
    if (findData == head.data) :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)  # 안 중요! (생략 가능)
        return
    # Case 2 : 중간 노드 앞에 삽입(사나, 솔라)
    current = head                    #pre = current  문장과 같이 다님
    while (current.link != None) :
        pre = current                 # current = head와 함께 다님
        current = current.link
        if (current.data == findData) :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)  # 안 중요! (생략 가능)
            return
    # Case 3 : 없는 노드 앞에 삽입 == 마지막에 추가 (재남, 문별)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)  # 안 중요! (생략 가능)
    return
def deleteNode(deleteData):             #head 노드 삭제
    global memory, head, pre, current
    if (deleteData == head.data):
        current = head
        head = head.link
        del(current)
        return
    current = head                      #중간 노드 삭제
    while (current.link !=None):
        pre=current
        current = current.link
        if(current.data == deleteData):
            pre.link =current.link
            del(current)
            return
    return                              # 없는 노드 삭제
                                        # (위의 head, 중간 노드에 없다는 뜻)
## 변수
memory = []  # 안 중요!
head, pre, current = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효'] # 여러분 데이터!

## 메인
node = Node()
node.data = dataArray[0]
head = node
memory.append(node) # 안 중요! (생략 가능)

for data in dataArray[1:] : # ['정연', '쯔위', ...
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)  # 안 중요! (생략 가능)
printNodes(head)

insertNode('다현', '화사')  #head
printNodes(head)
insertNode('사나', '솔라')   # 중간
printNodes(head)
insertNode('재남', '문별')   #마지막
printNodes(head)
deleteNode('다현')
printNodes(head)
deleteNode('쯔위')
printNodes(head)
deleteNode('재남')
printNodes(head)
