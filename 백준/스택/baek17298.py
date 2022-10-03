"""
22/07/18 스택
17298번 골드2 오큰수
"""
import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
stack = [] #숫자의 인덱스를 넣고 비교할 스택
oks = [-1]*N #오큰수를 넣어놓을 리스트
ans = []
for i in range(N): 
    while stack and num[stack[-1]] < num[i]:
        oks[stack[-1]] = num[i]
        stack.pop()
    stack.append(i)
print(*oks)