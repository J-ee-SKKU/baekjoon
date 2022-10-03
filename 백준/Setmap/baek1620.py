"""
22/06/18 집합과 맵
1620번 포켓몬 마스터 실버4
"""
#isalpha, isdigit은 자료형이 str 일때 사용가능
N,M = map(int,input().split())
po = {} #숫자가 key, 이름이 value
po_n = {} #이름이 key, 숫자가 value
for i in range(1,N+1): # 도감
    po[i] = input()
    po_n[po[i]] = i

que = [input() for _ in range(M)]

for i in que:
    if i .isdigit(): #키가 숫자면
        print(po[int(i)])
    else: #키가 이름이면
        print(po_n[i])