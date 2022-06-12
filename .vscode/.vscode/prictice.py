
e=[1,2,2,3,3]
t=list(set(e))#e라는 리스트를 집합화 시킴=중복 제거
print(t)   #파이썬 집합의 특징:순서가 없다, 중복인정이 안된다


#s1=set([1,2,3,4,5,6])
#s2=set([4,5,6,7,8,9])
#print(s1&s2)#교집합

#합집합
#w1=set([1,2,3,4,5,6])
#w2=set([4,5,6,7,8,9])
#print(w1|w2)#합집합

#차집합
#e1=set([1,2,3,4,5,6])
#e2=set([4,5,6,7,8,9])
#print(e1-e2)#차집합

#추가와 감량
#r1=set([1,2,3,4,5,6])
#r1.add(7)#추가 여러 개를 추가할 경우 update([])를 사용
#r1.remove(1)
#print(r1)


#불(참 혹은 거짓) 
from email.mime import message
from math import e


a=True
print(type(a))#클래스:불


#변수
#파이썬에서 사용하는 변수는 객체를 가르키는 것
#a=3  3이라는 값을 가지는 정수 자료형이 자동으로 메모리에 생성
#변수 a는 객체가 저장된 메모리의 위치를 가르키는 레퍼런스
#class를 이용해서 만든 것=객체 객체는 자료형으로 몰 수 있다.
a=[1,2,3]
b=a
a[1]=4
print(id(a))
print(id(b))#id는 주소, 같게 설정하면 주소 역시 같은 곳을 바라보고 있다.
print(a is b)#a=b인지 물어보는 구문, '='대신 쓸 수 있고 본 결과에서는 True가 나온다


A=[1,2,3]#A의 리스트를 그대로 B에게 주려면=B는 변하지 않게 하려면
B=A[:]#[:]은 처음부터 끝까지를 의미, 새로운 것이 생겨서 B로 들어간다
print(id(A))
print(id(B))


v77, v67='python', 'life'#각각 지정하기
print(v77)
print(v67)

#변수의 값을  바꾸는 행위
a=3
b=5
a,b=b,a#변수의 자리를 바꾸는 것이 중요
print(a)
print(b)


#조건문 조건문 if 절에서는 True는 1으로 False는 0으로 축약가능
money=2000
card=1
if False or card:#참 혹은 거짓을 의미
    print('택시를 타고 가라')
else:
    print('걸어가라')


fjk=2000
card=1
if 1 in [1, 2, 3]:#1과 in사이에 not을 넣을 수 있음
    pass#그냥 넘기는 것


#else if =elif
pocket=['paper', 'cellphone']
card=True
if 'money' in pocket:
    print('택시를 타고가라')
elif card:
    print('택시를 타고가라')
else:
    print('걸어가라')
    
    
#조건부 표현식
score=70
message='success' if score>=60 else 'failure'#만약 스코어가 60점 이상이라면 석세스 출력, 아니면 팰리어 출력 으로 해석할 수 있다
print(message)


#반복문
high=0
while high<10:
    high=high+1
    print('나무를 %d번 찍었습니다.' % high)#'' 사이에서 변수를 넣는 버뱌
    if high==10:
        print('나무 넘어가다')

u=10
money=300
while money:
    print('돈을 받았으니 커피를 줍니다')
    u=u-1
    print('남은 커피의 양은 %d개 입니다.' % u)
    if not u:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break#while문을 탈출 아무리 트루여도 탈출
    
    
#continue
a=0
while a<10:
    a=a+1
    if a%2==0:
        continue#while문 안쪽의 문장들을 수행하다가 컨티뉴를 만나게 되면 밑의 부분을 실행하지 않고 다시 while문의 처음으로 돌아간다
    print(a)
    

#for문 
test_list=['one', 'two', 'three']
for f in test_list:
    print(f)

imironman=[(1,2), (3,4), (5,6)]
for (first, last) in imironman:
    print(first)
    print(last)
imironman=1


#for에서의 continue
marks=[90, 25, 67, 45, 80]
number=0
for mark in marks:
    if mark<60: continue
    print(e)
#practice2에서


    