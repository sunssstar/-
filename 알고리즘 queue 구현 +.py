##함수
def isQueueFull():
    global SIZE,queue,front,rear
    if(rear== SIZE-1):
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE,queue,front,rear
    if (isQueueFull()):
        print('큐 꽉찼음')
        return
    rear += 1
    queue[rear] = data
    


## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

##메인
enQueue('화사')
enQueue('솔라')
#enQueue('문별')
#enQueue('휘인')
#enQueue('선미')
print('출구<---',queue,'<---입구')

#nQueue('재남')
#print('출구<---',queue,'<---입구')
