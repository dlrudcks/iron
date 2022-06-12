try:
    4/0
except ZeroDivisionError as e:
    print(e)
    
print('하동호')#오류 구문에서 안 멈추고 실행됨


try:
    f= open('none', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data=f.read()
    print(data)
    f.close()


o=open('foo.txt', 'w')
try:
    data=o.read()
    print(data)
except Exception as e:#Exception은 최상위의 거름망, 모든 것이 다 잡힘
    print(e)
finally:
    o.close()
    
    
try:
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다')
except IndexError:
    print('인덱싱 할 수 없습니다')
#10부터는 라이브러리 예제
    
    