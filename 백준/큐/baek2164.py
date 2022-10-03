"""
22/07/19 큐
2164번 실버4 카드2
"""
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
que = deque()
for i in range(N):
    que.append(i+1)
while len(que) > 1:
    que.popleft()
    que.rotate(-1)
print(*que)
