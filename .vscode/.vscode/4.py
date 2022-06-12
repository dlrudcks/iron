


#lines이용
f=open('새파일.txt', 'r', encoding='UTF-8')
lines=f.readlines()
for line in lines:
    print(line)
f.close()


#간격을 없애려면
ff=open('새파일.txt','r', encoding='UTF-8')
liness=ff.readlines()
for line in liness:
    print(line, end="")#한 줄로 정렬하려면 print(line.strip('\n'), end="")로 사용하면 가능
f.close()
    
    
#read() 함수를 이용하기read는 자료를 통채로 읽는다
F=open('새파일.txt', 'r', encoding='UTF-8')
data=F.read()
print(data)
F.close()


#with문
with open('foo.txt', 'w') as f:
    f.write('life is too short.')


#자료형 immutable과mutable
#immutable(변하지 않음)은 정수, 실수, 문자열, 자료형, 튜플의 변하지 않는 자료형을 지칭한다
#mutable(변함)은 리스트 딕셔너리 집합을 나타낸다
#pt.5