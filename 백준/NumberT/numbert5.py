"""
22/06/03
백준 3036번 실버3 """
import math
N = int(input())
A = list(map(int,input().split()))
for i in range(1,N):
    print(int( A[0]/math.gcd(A[0],A[i]) ),'/',int(A[i]/math.gcd(A[0],A[i])), sep="")
#약분하는 법 분자분모 모두 최대공약수로 나누어준다 