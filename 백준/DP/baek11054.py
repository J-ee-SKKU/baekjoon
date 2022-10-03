"""
22/07/08 동적 프로그래밍
11054번 골드3 가장 긴 바이토닉 부분 수열
"""
# 바이토닉 수열은 계속 증가하는  부분 + 계속 감소하는 부분으로 이루어진 수열
# 다만 커지다 작아지다 커지는 것은 불가능 증가만 하거나, 감소만 하거나 증가하다가 감소만 하거나
# 세가지만 가능
# 반대쪽에서부터 시작하는 증가하는 수열 찾은 다음에서 서로 더해주고 전부 1씩 빼주면 됨
N = int(input())
seq = list(map(int,input().split()))
fdp = [1]*N
ldp = [1]*N
dp = [1]*N
mindex = seq.index(max(seq))
for i in range(N): # 0 ~ N-1
    for j in range(i): # 0 ~ i-1 증가하는 경우
        if seq[i] > seq[j]: 
            fdp[i] = max(fdp[i],fdp[j]+1)
for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if seq[i] > seq[j]:
            ldp[i] = max(ldp[i],ldp[j]+1)
for i in range(N):
    dp[i] = fdp[i] + ldp[i] - 1
print(max(dp))




