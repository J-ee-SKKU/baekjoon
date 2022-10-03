"""
22/07/17 스택
10773번 실버4 제로
"""
N = int(input())
stack = []
for i in range(N):
    a = int(input())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))

