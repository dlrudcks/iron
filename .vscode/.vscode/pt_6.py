
#클래스
class Calculator:
    def __init__(self):
        self.result=0
    def add(self, num):
        self.result+=num
        return self.result
cal1=Calculator()
cal2=Calculator()
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

#클래스 셋데이터
class Bf:
    def setdata(self, dd, ff):
        self.dd=dd
        self.ff=ff
        
a=Bf()
a.setdata(1,2)#a는 self로 1은 dd로 2는 ff로 들어간다
print(a.dd)
print(a.ff)
#산출: 1, 2


class Fd:
    def setdata(self, first, second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
a=Fd()
a.setdata(4, 2)
print(a.add())
