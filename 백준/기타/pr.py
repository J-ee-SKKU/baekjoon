#리스트 괄호없이 숫자만 출력하는 법
print(*list)
#시간재는법
#시작할때 끝날때 하나씩 선언하고 빼주면 됨
import time
time.process_time()

#출력결과저장하는법
import sys
sys.stdout = open('파일명','w') #쓰기전용
#print 한 것들 파일에 써짐
sys.stdout.close()
#input().rstrip() : 입력받은 것 중 제일 뒤 있는거 없애줌

# 9/2 = 4.5 9//2 = 4 //사용하면 소수점 아래 버린다