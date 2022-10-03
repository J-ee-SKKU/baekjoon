"""
22/06/19 집합과 맵
1764번 실버4 듣보잡
"""
N,M = map(int,input().split())
nl = { input() for i in range(N)}
ns = { input() for i in range(M)}
ans = []
for i in nl:
    if i in ns:
        ans.append(i)
print(len(ans))
for i in sorted(ans):
    print(i)
