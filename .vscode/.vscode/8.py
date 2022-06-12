class Fg:
    def __init__(self, first, second):#__init__함수는 클래스 내에서 가장 먼저 실행되는 특별한 함수이다
        self.first=first
        self.second=second
    def setdata(self, first, second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first + self.second
        return result
    def mul(self):
        result=self.first * self.second
        return result
    def sub(self):
        result=self.first - self.second
        return result
    def div(self):
        result= self.first/self.second
        return result
class Gf(Fg):
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second

#클래스,객체변수
#클래스 변수란 클래스에 미리 선언한 변수이다
class Family:
    lastname='김'
Family.lastname='박'#Family라는 설계도의 lastname 변수를 지정하서 설계도 자체를 변경
print(Family.lastname)
a=Family()
b=Family()
print(a.lastname)
print(b.lastname)
#모듈=미리 만들어 놓은 파이썬 파일(함수, 변수, 클래스)
#mod1 사용
#mod1:
#def add(a,b):
#    a+b


import mod1
print(mod1.add(1,2))


#mod2에서 원하는 것을 가져오기
from mod2 import add