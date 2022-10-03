"""
22/07/11 누적합
16139번 실버1 인간-컴퓨터 상호작용
"""

S = input()
q = int(input())
arr = [[0]*26 for _ in range(len(S))]
for i in range(len(S)):
    if i >= 1:
        arr[i][:] = arr[i-1][:]
    arr[i][ord(S[i])-97] += 1
"""
for k in range(len(S)):
    print(arr[k])
"""
for i in range(q): #반복횟수
    a,l,r = input().split()
    l = int(l)
    r = int(r)
    if l == 0:
        print(arr[r][ord(a)-97])
    else:
        print(arr[r][ord(a)-97] - arr[l-1][ord(a)-97])



    
    