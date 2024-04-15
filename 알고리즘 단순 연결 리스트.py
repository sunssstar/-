# 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

## 변수


## 메인

node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2 #노드 연결 과정

node3 = Node()
node3.data = '쯔위'
node2.link = node3 #노드 연결 과정

node4 = Node()
node4.data = '사나'
node3.link = node4 #노드 연결 과정

node5 = Node()
node5.data = '지효'
node4.link = node5 #노드 연결 과정

#newNode= Node()     #새로운 노드를 추가 
#newNode.data = '재남'
#newNode.link = node2.link   
#node2.link = newNode   # new Node를 2번 링크와 연결되게 만듦

node2.link = node3.link
del(node3)

#print(node1.data, end =' ')
#print(node2.data, end =' ')
#print(node3.data, end =' ')
#print(node4.data, end =' ')
#print(node5.data, end =' ')


#current  활용

current = node1
print(current.data, end= ' ')
while   (current.link != None):
        current = current.link
        print(current.data, end = ' ')
print()


