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



#파이썬 클래스의 상속
#클래스의 상속이란 어떤 역할을 하는 클래스를 개선할 때 그 클래스를 그대로 사용하고 보충을 하게되는 것이다
class High(Fg):       
    pass
a=High(4, 2)
print(a.add())
class Ff(Fg):#매서드 추가
    def pow(self):
        result=self.first**self.second
        return result
a=Ff(4, 2)
print(a.pow())


