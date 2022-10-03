"""
22/07/08 누적 합
11659번 실버3 구간 합 구하기
"""
# 이중포문은 시간초과
import sys
input = sys.stdin.readline
N , M = map(int,input().split()) # N은 수열 길이, M은 반복 횟수
# N,M <= 100000
nums = list(map(int,input().split()))

#누적합 수열을 따로 만들어야함
pfs = [0]*(N+1)
for i in range(N):
    pfs[i+1] = nums[i] + pfs[i]
for i in range(M):
    a,b = map(int,input().split())
    res = pfs[b] - pfs[a-1]
    print(res)