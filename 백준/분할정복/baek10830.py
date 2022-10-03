"""
22/08/06 분할정복
10830번 골드4 행렬제곱
"""
import sys
input = sys.stdin.readline
N , B = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
#두 행렬을 곱하는 함수
def pro(a,b): #행렬 a와 b의 곱을 계산 row column
    """
    ar = len(a)
    ac = len(a[0])
    br = len(b)
    #ac와 br의 길이는 무조건 같음
    bc = len(b[0])
    """
    # 정사각형 크기의 행렬이므로
    n = len(a) 
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += a[i][k] * b[k][j]
            C[i][j] = C[i][j]%1000
    return C
#제곱 낮춰주는 함수
def exp(l,n): #l은 행렬, n은 제곱
    if n==1:
        for i in range(len(l)):
            for j in range(len(l)):
                l[i][j] = l[i][j]%1000
        return l
    tmp = exp(l,n//2) #이거 안해서 시간초과났음 큰차이가 
    if n%2 == 0:
        return pro(tmp,tmp)
    else:
        return pro(pro(tmp,tmp),l)
res = exp(A,B)
for i in range(N):
    print(*res[i])