def add(a,b):
    return a+b
def aa(a,b):
    return a-b
if __name__=='__main__':
    print(add(1,4))
    print(add(4,2))


#import하려는 자료가 파일 서브폴더에 있을 때
import sys
sys.path.append('c:\\'파일 이름'\\'서브 폴더 이름')#파일 이름ex)python workspace  서브 폴더의 이름 ex).vscode
import mod1#ex)mod1


#패키지, 묘듈을 여럿 모아놓은 것
import .vscode.__pycache__.mod1#이는 가상의 예이다, 이 줄은 .vscoded의 파일안에 __pycache__안의 mod1이라는 파이썬 파일을 도입하려는 것
.vscode.__pycache__.mod1.add(a,b)#mod1의 add(a,b)함수를 스기 위한 과정


#이렇게도 쓸 수 있다
from .vscode.__pucache__.mod1 import add(a,b) as d
d(1, 2)


#__all__
from .vscode.__pycache__ import * # *는 전부를 뜻함
mod1.add(1,2)
#*이 정상작동하게 하려면 __pycache__의 파일 중 하나에 __all__=['as','dfd', ~~~~]의 꼬로 규명하면 작동한다


#예외처리: 오류가 발생했을 때 어떻게 할 지 정하는 것

pt9
