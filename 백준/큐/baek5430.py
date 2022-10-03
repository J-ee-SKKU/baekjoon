"""
22/07/22 큐
5430번 골드5 AC
"""
from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    p = input()
    n = int(input())
    flag = True
    rcnt = 0
    arr = deque(input().rstrip()[1:-1].split(','))
    if n == 0:
        arr = deque()
    for i in p:
        if i == 'D':
            if not arr:
                print('error')
                flag = False
                break
            else:
                if rcnt % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
        elif i == 'R':
            rcnt += 1
    if flag:
        if rcnt % 2 == 0:
            print('['+",".join(list(arr))+']')
        else:
            arr.reverse()
            print('['+",".join(list(arr))+']')


            

