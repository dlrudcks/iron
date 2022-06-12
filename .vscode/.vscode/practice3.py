#f=open('새파일.txt', 'w')#f라는 변수를 오픈하고 새파일.txt라는 파일을 만들고 'w'는 write을 의미한다 그러니 우리가 실행하면 옆 탐색기에 새파일.txt가 생긴다'
#f.close()
#파일열기 모드:r=읽기 모드 파일을 읽기만 할 때 사용 w=쓰기 모드 파일에 내용을 쓸 때 사용한다 a=추가모드  파일의 마지막에 새로운 내용을 추가 시킬 때 사용


f= open("새파일.txt", 'w', encoding='UTF-8')#한국어가 정상 출력되게 한다:UTF-8
for i in range(1, 11):
    data="%d번쨰 줄입니다.\n" % i
    f.write(data)
f.close()


#읽기 모드  한 줄만 보기
f= open('새파일.txt', 'r', encoding='UTF-8')
line=f.readline()
print(line)
f.close()
