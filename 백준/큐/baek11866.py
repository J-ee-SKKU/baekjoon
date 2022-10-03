"""
22/07/20 큐
11866번 실버5 요세푸스 문제0
"""
from collections import deque
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
que = deque()
ans = []
for i in range(N):
    que.append(i+1)
while len(que):
    que.rotate(-K+1)
    ans.append(que.popleft())
print('<'+", ".join(str(i) for i in ans)+'>')

