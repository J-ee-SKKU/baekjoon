"""
22/06/03
11050 브론즈1 이항계수 """
n,k = map(int,input().split())
def dps(a):
    if a == 1:
        return 1
    return  a * dps(a-1)
if k==0:
    print(1)
elif n == k:
    print(1)
else:
    print(int(dps(n)/(dps(k)*dps(n-k))))
