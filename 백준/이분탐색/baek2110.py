"""
22/09/08-10 이분탐색
2110번 골드4 공유기설치
"""
import sys
input = sys.stdin.readline
N,C = map(int, input().split()) #집의 수, 공유기 개수
home = [int(input()) for _ in range(N)] #집의 좌표
home = sorted(home)
low,high = 1,home[-1]-home[0]
#집과 집사이의 최소거리와 최대거리 최소거리는 그냥 1로 설정
t = 0
while low<=high:
    cnt = 1 #설치한 공유기 개수세는 변수 시작점엔 무조건 설치하니까 1
    mid = (low+high)//2
    s = home[0] #공유기를 설치한 지점 중 가장 뒤에 있는 곳 (기준점)
    for i in home:
        if i >= (s+mid):
            cnt += 1
            s = i
    t += 1
    #반복문 다 돌았을 때 공유기 개수가 설치해야하는 개수보다 
    #같거나 많으면 거리늘리고 적으면 거리 줄임
    if cnt >= C:
        low = mid + 1
    else:
        high = mid - 1
print(high)