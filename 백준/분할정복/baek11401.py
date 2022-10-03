"""
22/08/04 분할정복
11401번 골드1 이항계수3
"""
#페르마 소정리 사용 
import sys
import time
input = sys.stdin.readline
N ,K = map(int,input().split())
a = 1
b = 1
p = 1000000007
def dps(a, n): #지수가 너무 큰 수를 빨리 계산해줌
    if n == 0:
        return 1
    elif n % 2 == 0:
        return (dps(a, n//2) **2) % p
    else:
        return ((dps(a, n//2) **2) *a) % p
for i in range(1,K+1):
    a = a*(N-i+1)%p
    b = b*i%p
s = time.time()
print((a%p)*(dps(b,p-2)%p)%p)
e = time.time()
print("time : %.5f"%(e-s))