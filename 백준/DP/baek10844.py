"""
22/06/28 동적 프로그래밍
10844번 실버1 쉬운 계단수
"""
N = int(input()) #자리수 1<= <=100
dp = [[0]*10 for _ in range(101)]
dp[1] = [0,1,1,1,1,1,1,1,1,1] #N==1 일때
for i in range(2,N+1): #2~N
    for j in range(10):#0~9
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else: # 1~8
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[N])%1000000000)
