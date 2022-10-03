"""
22/07/19 큐
18258번 실버4 큐2
"""
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
que = deque()
for i in range(N):
    a = input().split()
    if a[0] == 'push':
        que.append(a[1])
    elif a[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(que))
    elif a[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
