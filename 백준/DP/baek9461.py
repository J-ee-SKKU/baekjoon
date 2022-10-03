"""
22/06/22 동적 프로그래밍
9461번 실버3 파도반수열 
"""
N = int(input())
a = [input() for _ in range(N)]
p = [0] * 101
p[1:5] = 1,1,1,2,2
def padovan(n):
    for i in range(6,n+1):
        p[i] = p[i-1] + p[i-5]
    return p[n]
for i in a:
    print(padovan(int(i)))