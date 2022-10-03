"""
22/06/18 집합과 맵
14425번 문자열 집합
"""
N ,M = map(int,input().split())
target = []
test = []
cnt = 0
for _ in range(N):
    target.append(input())
target = set(target)

for _ in range(M):
    k = input()
    if k in target:
        cnt += 1
print(cnt)