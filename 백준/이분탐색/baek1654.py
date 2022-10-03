"""
22/08/30 이분탐색
1654번 실버2 랜선자르기
"""
import sys
input = sys.stdin.readline
"""
범위를 특정짓고 좁혀나가야함.
이미 갖고 있는 개수이상의 랜선이 필요하다.
후보중 제일 긴 랜선과 1사이로 범위가 설정 되어야함
"""
K , N = map(int,input().split())
arr = [int(input()) for _ in range(K)]

start, end = 1,max(arr)
while start <= end: #이분탐색 도중에 원하는 값이 나와도 멈추지 않고 끝까지 한다
    mid = (start+end)//2
    cnt = 0
    for i in arr:
        cnt += i//mid
    
    if cnt >= N: #원하는 개수보다 많이 나왔을 경우에는 길이를 늘린다
        #원하는 개수가 나와도 반복한다. 원하는 개수가 나온 값을 start로 두고 더 큰 방향으로 반복
        start = mid + 1
    else: #원하는 개수보다 적게 나왔을 경우에는 길이를 줄인다
        end = mid - 1
print(end)





            

