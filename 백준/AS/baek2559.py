"""
22/07/08 누적 합
2559번 실버3 수열
"""
import sys
input = sys.stdin.readline
N , K = map(int,input().split())
#2<=N<100000 1<K<N
nums = list(map(int,input().split()))
pfs = [0]*(N-K+2) #맨앞은 0으로 고정
for i in range(K):
    pfs[1] += nums[i]
for i in range(2,N-K+2):
    pfs[i] = pfs[i-1] - nums[i-2] + nums[i-2+K]
m = max(pfs[1:])