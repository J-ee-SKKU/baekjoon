"""
22/07/14 그리디
11399번 실버4 ATM
"""
#누적합이랑 같은 듯
import sys
input = sys.stdin.readline
N = int(input()) # 사람 수
time = list(map(int,input().split())) # 각각 걸리는 시간
time = sorted(time)
wait = [0]*N
wait[0] = time[0]
for i in range(1,N):
    wait[i] = time[i] + wait[i-1]
print(sum(wait))
