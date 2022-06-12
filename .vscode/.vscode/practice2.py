for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")#i가 2인 상황에서 j가 바뀌고 i가 3으로 넘어가는 방식이다
    
    
#함수


def sum_many(*args):#인자의 수를 정하지 않고 몇 개든 넣을 수 있음:*args
    sum=0
    for i in args:#이 구문은 인자들의 합을 넣어서 적용하는 것이다
        sum=sum+i
    return sum
print(sum_many(7,4,4,4,4))


def im_iron_man(**kwargs):#이 인자는 들어올 수 있는 자료들을 딕셔너리 형태로 저장한다
    for t in kwargs.keys():
        if t=='name':
            print('당신의 이름은:' +kwargs[t])
print(im_iron_man(name='int 조수', b='2'))


#함수의 결괏괎
def sum_and_mul(a,b):
    return a+b, a*b
print(sum_and_mul(1,2))#a+b와 a*b중 한 개의 결과를 얻고 싶다면 ex)print(sum_and_mul(1,2)[0])으로 순서를 적으면 된다
#결과는(3, 2)같은 형태로 튜플 형태로 출력된다


def asd(name, old, man=True):
    print('니의 이름은 %s 입니다' % name)
    print('나이는 %d살 입니다.' %old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')
asd('자진매', 20, True)#man=True 라고 설정하면 True를 안 넣어도 자동으로man=True이기 때문에 '남자입니다'가 출력 man=true가 없으면 오류true의 자리에 false를 넣게 되면 여자라고 인식한다


#함수의 효력 범위
a=1
def er(a):
    a=a+1
er(a)
print(a)#er이라는 함수를 실행하고 a를 출력했기 때문에 2가 나올 것 같지만 1이 나온다
#그 이유는 a가 함수 안에서의 임시 변수 같은 개념을 가지고 있기 때문인데 a+1이 영향받는 범위는 함수까지이다 함수 밖의 부분에 영향을 줄 수도 있으나 좀 더 다룰 부분으로 남긴다
#a에 영향을 주려면 글로벌이나 리턴을 쓴다
a=1
def hh(a):
    a=a+1
    return a
hh(a)
print(a)


#input
#파일을 쓰기 모드로 열어 출력값 적기    절대주소:처음부분인 C:/부터 작성하는 것  상대주소:작성하고 있는 파일을 기준으로 상대적인 경로를 작성하는 것 이다
f = open('새파일.txt', 'w', encoding='UTF-8')#1='새파일.txt'와 2='C:/Python/새파일.txt'일 떄 1과 2의 차이점은 1은 현재경로에 바로 같이 생성되고, 2는 절대주소에 속한다 1은 현재 폴더에 속해있는 자료를 넣을 떄 사용할 수 있다
for i in range(1,11):         #encoding=='UTF-8'은 한글을 깨지지 않게 출력해주는 역할
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()


#파일을 읽기:readline()함수
f=open('새파일.txt', 'r')
while True:
    line=f.readline()
    if not line: break
    print(line)
f.close()
