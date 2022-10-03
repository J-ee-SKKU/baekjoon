"""
22/07/18 스택
4949번 실버4 균형잡힌세상
"""
while True:
    arr = input()
    if arr == '.':
        break
    stack = []
    flag = True
    for i in arr:
        if i == '(' or i == '[':
            stack.append(i)
        elif i ==')':
            if not stack: #비어있는경우 탈출
                flag = False
                break
            elif stack[-1] == '[':
                flag = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack:  # 비어있는경우
                flag = False
                break
            elif stack[-1] == '(':
                flag = False
                break
            elif stack[-1] == '[':
                stack.pop()
    #stack이 비어있고 flag가 True이어야함
    if flag == True and not stack:
        print('yes')
    else:
        print('no')
