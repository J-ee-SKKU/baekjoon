"""
22/06/12
백준 14889번 스타트와 링크 실버2
"""
#start,link로 나누는 법을 재귀로 한 다음 이중for문으로 계산한 후 최솟값 출력
N = int(input())
stat = [list(map(int,input().split())) for i in range(N)]
for i in range(N):
    for j in range(i,N):
        stat[i][j] + stat[j][i]
start = [0] #start 아니면 link이므로 0있는 쪽을 start로 함으로써 계산 1회줄임
link = []
tmp = 100000
def dfs():
    global tmp
    if len(start) == N//2:
        link = [] #돌때마다 초기화
        for i in range(N): #start아니면 link이므로
            if i not in start:
                link.append(i)
        #print(start,"",link)
        s_sum = 0 # start 능력 합
        l_sum = 0 # link 능력 합
        for i in start: # [k][k] 좌표는 다 0이므로 포함가능
            for j in start:
                s_sum += stat[i][j] 
        for i in link:
            for j in link:
                l_sum += stat[i][j]
        diff = abs(s_sum-l_sum) # 절댓값으로 표시
        if diff < tmp : #최솟값구하기 이므로 작은 경우에만 업데이트
            tmp = diff
        return
    else:
        for i in range(N): 
            if i in start: #start에 중복은 안넣기
                continue
            elif start[-1] > i: #앞에 수보다 큰 경우만 넣기 
                                #ex) [0,1,2] 가능 [0,2,1] 불가 어차피 중복
                continue
            else:
                start.append(i)
                dfs()
                start.pop() #여기로 오는 경우는 꽉찬경우이므로 마지막칸 비운다
dfs()
print(tmp)

            