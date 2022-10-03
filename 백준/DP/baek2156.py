"""
22/06/28 동적 프로그래밍
2156번 실버1 포도주 시식
"""
n = int(input())
t = [0] + [int(input()) for _ in range(n)]
res = [0]*(n+1)

if n == 1:
    print(t[1])
elif n == 2:
    print(t[1]+t[2])
elif n == 3:
    print(max(t[1]+t[2],t[1]+t[3],t[2]+t[3]))
else:
    res[1:4] = t[1], t[1]+t[2], max(t[1]+t[2], t[1]+t[3], t[2]+t[3])
    for i in range(4,n+1):
        res[i] = max(res[i-1],res[i-2]+t[i],res[i-3]+t[i]+t[i-1])
        # 안먹는경우, 바로전 안먹고 이번에 먹는 경우, 두번 안먹고 먹는 경우
    print(res[n])
