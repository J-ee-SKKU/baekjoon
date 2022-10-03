"""
22/06/17 집합과 맵
10815번 실버5 숫자카드
"""
N = int(input())
num1 = list(map(int,input().split()))
M = int(input())
num2 = list(map(int,input().split()))
can = {} # 숫자 : 개수로 이루어진 dic
ans = [] # 개수만 담고 있는 list
for i in num1: #상근이가 갖고 있는 카드들 순회
    if i in can: #그게 dic에 있다면 cnt추가
        can[i] += 1
    else: # 중복되지않으면 1로 초기화
        can[i] = 1 
for i in num2:
    if i in can:
        ans.append(can[i])
    else:
        ans.append(0)
print(*ans)