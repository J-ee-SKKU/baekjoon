"""
22/07/18 스택
9012번 실버4 괄호
"""
N = int(input())
for i in range(N):
    vps = input()
    stack = []
    war = True
    for p in vps:
        if p == '(':
            stack.append(0)
        elif p ==')':
            if stack: #비어있지않은경우
                stack.pop()
            else: #비어있는경우
                print('NO')
                war = False
                break
    if war == False:
        continue
    if not stack: # 비어있는경우
        print('YES')
    else:
        print('NO')
