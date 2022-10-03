N,M = map(int,input().split())#N<10**6 M<10**3
num = list(map(int,input().split()))
pfs = [0]*(N+1)
cnt = [0]*(M)
for i in range(1,N+1): # 0 1 2 3 4
    pfs[i] = pfs[i-1] + num[i-1]
    cnt[pfs[i]%M] += 1
cnt[0] += 1
res = 0
for i in cnt:
    res += i*(i-1)//2
print(res)
