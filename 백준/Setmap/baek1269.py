"""
22/06/20 집합과 맵
1269번 실버3 대칭차집합
"""
N,M = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sA = set(A)
sB = set(B)
print(len(sA-sB)+len(sB-sA))