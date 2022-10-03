"""
22/09/11 이분탐색
1300번 골드2 K번째 수
"""
N = int(input()) #N*N 이차원 배열
K = int(input()) #K번째 수를 구해야한다.
low,high = 1,K #high가 왜 K일까
while low <= high: #low가 high+1 이 되면서 빠져나온다.
    mid = (low+high)//2 #mid는 순서 아니고 수 
    cnt = 0 #mid보다 작거나 같은 수가 몇개인지 셀 변수
    for i in range(1,N+1):
        cnt += min(mid//i,N) #i번째 행에 mid보다 작은 수의 개수
        #i번째 행은 모두 i의 배수이므로 mid를 i로 나눈 몫이 개수가 된다. 
        #예를 들어 3번째 행의 숫자들은 3,6,9,12... 일텐데
        #mid가 13이라면 3으로 나눈 몫이 4이고 13보다 작은 수의 개수도 4개이다.
        #min()안에 N이 있는 건 mid//i가 N보다 커도 한 행에 있는 수는 N개이기 때문이다.
    if cnt >= K: #숫자의 개수가 목표치보다 많으면 숫자를 낮춰야한다
        #같은 걸 찾는 거지만 같아져도 끝까지 돌린 후 low값을 출력시킨다.
        high = mid - 1
    else:
        low = mid + 1
print(low)


        

