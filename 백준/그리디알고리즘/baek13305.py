"""
22/07/14 그리디
13305번 실버4 주유소
"""
import sys
input = sys.stdin.readline
N = int(input()) # 도시 개수
km = list(map(int,input().split())) #거리 요소개수 N-1 
oil = list(map(int,input().split())) #기름값 요소개수 N
money = 0
last = oil[0]
for i in range(N-1):
    #print(last,'*',km[i-1])
    if oil[i] < last: #전보다 저렴하면
        last = oil[i]
    money += last*km[i]
print(money)

"""
for i in range(N-1):
    if oil[i] < oil[i+1]:
    money += km[0]*oil[0] #첫도시에서 다음도시로 이동할만큼만 충전 후 이동
"""