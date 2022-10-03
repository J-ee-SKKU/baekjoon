"""
22/06/29 동적 프로그래밍
11053번 실버2 가장 긴 증가하는 수열
"""
N = int(input()) #1~1000 이중포문해도 ㄱㅊ
pro =list(map(int,input().split()))
dp = [1]*N #i번째에 i번까지의 수열의 길이
for i in range(N): #0~(N-1)
    for j in range(i):#0~(i-1)
        if pro[i] > pro[j]:
            dp[i] = max(dp[i],dp[j]+1) 
            # 바로앞에거에 +1을 하거나 바로 앞보다 자기가 클 경우엔 자기꺼 그대로 씀
            # 이중포문이라 존나 헷갈림
print(max(dp))
