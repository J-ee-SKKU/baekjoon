"""
22/09/12 이분탐색
12015번 골드2 가장 긴 증가하는 부분수열 2
"""
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
res = [0]
for i in A:
    if i > res[-1]:
        res.append(i)
    else:
        #A[i]가 res 내 제일 큰 수보다 작은 경우 자기보다 큰 수 중 제일 작은 수와 대치
        low = 0
        high = len(res)
        while low < high:
            mid = (low+high)//2
            if res[mid] < i:
                low = mid + 1
            else:
                high = mid
        res[high] = i
print(len(res)-1)

