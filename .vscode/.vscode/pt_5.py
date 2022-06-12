#immutable
a=1
def min(a):
    a=a+1
min(a)
print(a)


#mutable
b=[1,2,3]
def min2(b):
    b=b.append(4)
min2(b)
print(b)


#클래스:반복되는 변수와 함수를 미리 정해 놓은 틀(설계도)
result=0
def add(num):
    global result
    result+=num
    return result
print(add(3))
print(add(4))

#두 개의 계산기
result1=0
result2=0
def add1(num):
    global result1
    result1+=num
    return result1
def add2(num):
    global result2
    result2+=num
    return result2
print(add1(3))
print(add1(4))
print(add2(7))
print(add2(7))

