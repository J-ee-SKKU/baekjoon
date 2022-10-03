"""
22/07/18 스택
1874번 실버2 스택 수열
"""
N = int(input())
num = [int(input()) for _ in range(N)]
stack = []
ans = []
flag = True
a = 0
for i in range(N): 
    t = num[i] # 타겟넘버 이 수를 찾아간다고 생각
    while a < t: 
        a += 1
        stack.append(a)
        ans.append('+')
    if stack[-1] == t:
        stack.pop()
        ans.append('-')
    elif stack[-1] > t: # 남아있는 스택의 마지막 숫자가 현재 목표 숫자보다 클 경우 불가능
        flag = False
        break
if flag == False:
    print('NO')
else:
    for i in ans:
        print(i)


