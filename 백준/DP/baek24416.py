"""
22/06/21 동적 프로그래밍
24416번 브론즈1 알고리즘 수업
"""
def dfs_fib(n):
    global dfs_cnt 
    if n==1 or n==2:
        dfs_cnt += 1
        return 1
    return dfs_fib(n-1)+dfs_fib(n-2)
def dp_fib(n):
    global dp_cnt
    fib = [0 for _ in range(100)]
    fib[1]=1
    fib[2]=1
    for i in range(3,n+1):
        dp_cnt += 1
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
dfs_cnt = 0
dp_cnt = 0
N = int(input())
dfs_fib(N)
dp_fib(N)
print(dfs_cnt,dp_cnt)
