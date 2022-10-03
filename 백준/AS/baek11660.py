"""
22/07/13 누적 합
11660 실버1 구간 합 구하기5
"""
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
table = [list(map(int,input().split())) for _ in range(N)]
pfs = [[0]*(N+1) for _ in range(N+1)]
ans = []
for i in range(1,N+1):
    for j in range(1,N+1):
        pfs[i][j] = pfs[i][j-1] + pfs[i-1][j] - pfs[i-1][j-1] + table[i-1][j-1]
for i in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    res = pfs[x2][y2] - pfs[x1-1][y2] - pfs[x2][y1-1] + pfs[x1-1][y1-1]
    ans.append(res)
#print(" ".join(str(i) for i in ans))
for i in ans:
    print(i)
