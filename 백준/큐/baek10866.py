"""
22/07/22 큐
10866번 실버4 덱
"""
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
deq = deque()
for i in range(N):
    a = input().split()
    if a[0] == 'push_front':
        deq.appendleft(a[1])
    elif a[0] == 'push_back':
        deq.append(a[1])
    elif a[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print('-1')
    elif a[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print('-1')
    elif a[0] == 'size':
        print(len(deq))
    elif a[0] == 'empty':
        if deq:
            print('0')
        else: #비어있을때
            print('1')
    elif a[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print('-1')
    elif a[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print('-1')

