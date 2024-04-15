## 함수
def add_data(friend) :
    # 1단계 : 빈칸 추가
    katok.append(None)
    kLen = len(katok) # 선형 리스트의 길이를 파악!
    # 2단계 : 마지막 칸에 데이터 입력
    katok[kLen-1] = friend

## 변수
katok = []

## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)




def insert_data(position,friend):
     katok1.append(None)                 # 빈칸 추가
     Klen=len(katok1)                    # 마지막 친구부터, 삽일할 위치까지 위치 추가
     for i in range(Klen-1,position-1):  # 어려움
        katok1[i] = katok1[i-1]
        katok1[i-1] = None
     katok1[position] = friend

## 변수
katok1 = []

## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok1)
add_data('모모')
print(katok1)




## 함수
def add_data(friend) :
    # 1단계 : 빈칸 추가
    katok.append(None)
    kLen = len(katok) # 선형 리스트의 길이를 파악!
    # 2단계 : 마지막 칸에 데이터 입력
    katok[kLen-1] = friend

def insert_data(position, friend) :
    # 1단계 : 빈칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 마지막 친구부터, 삽입할 위치까지 한칸씩 뒤로 이동
    for i in range(kLen-1, position, -1) : # 어려움!!!!
        katok[i] = katok[i-1]
        katok[i-1] = None
    # 3단계 : 위치에 친구 입력
    katok[position] = friend


## 변수
katok = []

## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)

insert_data(3, '미나')
print(katok)


