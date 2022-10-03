"""
22/08/11 분할정복
11444번 골드2 피보나치 수 6
"""
import sys
import time
input = sys.stdin.readline
N = int(input())
start = [[1,1],[1,0]]
def square(a,b):# 행렬 a와 b의 곱
    fibo = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                fibo[i][j] += a[i][k]*b[k][j]
            fibo[i][j] = fibo[i][j]%1000000007
    return fibo
def exp(l,n):#행렬의 l의 n제곱
    if n==1:
        return l
    tmp = exp(l,n//2)
    if n%2 == 0:
        return square(tmp,tmp)
    elif n%2 == 1:
        return square(square(tmp,tmp),start)
if N<3:
    print(1)
else:
    res = exp(start,N-1)[0][0]
    print(res%1000000007)
