"""
22/08/01 분할정복
1629번 실버1 곱셈
"""
#빡대가리인지 존나 헷갈렸음
#2^32 = (2^16)^2 로 계산하면 계산횟수가 줄어드는 걸 이용하는 문제
a,b,c = map(int,input().split())
def dps(a,n):
    if n==1:
        return a%c
    elif n%2 == 0:
        return ((dps(a,n//2)**2)%c)
    else:
        return ((dps(a,n//2)**2)*a)%c
print(dps(a,b))