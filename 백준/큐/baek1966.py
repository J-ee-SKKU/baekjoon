"""
22/07/20 큐
1966번 실버3 프린터 큐
"""
from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    plist = deque(map(int,input().split()))
    idx = deque(range(len(plist)))
    idx[M] = 'target' #타겟값지정을 따로 하는 이유는 같은 수가 있을때 구분하기위해
    cnt = 0
    while True:
        if plist[0] == max(plist): #지금 출력되는수가 최댓값인가
            cnt += 1
            if idx[0] == 'target': #출력되는 수가 최댓값이면서 타겟인가
                print(cnt)
                break
            else: #최댓값인데 타겟은 아닐때
                plist.popleft()
                idx.popleft()
        else: #최댓값이 아니면
            plist.rotate(-1)
            idx.rotate(-1)
