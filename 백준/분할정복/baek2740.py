"""
22/08/05 분할정복
2740번 실버5 행렬곱셈
"""
N,M = map(int,input().split())
A = [0 for _ in range(N)]
for i in range(N):
    A[i] = list(map(int,input().split()))
M, K = map(int, input().split())
B = [0 for _ in range(M)]
for i in range(M):
    B[i] = list(map(int, input().split()))
mul = [[0 for _ in range(K)]for _ in range(N)]
for i in range(N):
    for j in range(K):
        for m in range(M):
            mul[i][j] += (A[i][m] * B[m][j])
for i in mul:
    print(*i)
