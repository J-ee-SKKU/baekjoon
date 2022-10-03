"""
22/09/08 이분탐색
2805번 실버2 나무자르기
"""
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
tree = list(map(int,input().split()))
low, high = 0,max(tree) #최소 길이를 0으로 설정안해서 틀렸었음 
res = []
while low <= high :
    mid = (low + high)//2
    hap = 0
    for i in tree:
        if i > mid:
            hap += (i - mid)
    if hap == m:
        res.append(mid)
        break
    elif hap > m: # 남은 길이의 합이 더 긴 경우는 높이를 더 높여서 잘라야 합이 작아진다
        res.append(mid)
        low = mid + 1
    else:
        high = mid - 1
print(max(res))
