"""
22/07/02 동적 프로그래밍
12865번 골드5 평범한 배낭
"""
N , K = map(int,input().split())
inven =[list(map(int,input().split())) for _ in range(N)]
bag = [[0 for _ in range(K+1)] for _ in range(N+1)] 
#행x열 (물건개수)x(최대무게)
#각 무게마다의 최고가치를 기록한다. 
for i in range(1,N+1):
    for j in range(1,K+1):
        w = inven[i-1][0] #넣을 물건의 무게
        v = inven[i-1][1] #넣을 물건의 가치
        if j < w: #검사하는 무게가 물건무게보다 가벼우면 이전 기록을 그대로 가져옴
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(v+bag[i-1][j-w],bag[i-1][j])
        #가방에서 현재 물건의 무게만큼 뺐을 때의 가치에 물건을 더하는 것(이 물건을 가방에 넣는 것)
        #이 물건을 넣는 것보다 기존의 가치가 더 높은 경우
print(bag[N][K])





        



