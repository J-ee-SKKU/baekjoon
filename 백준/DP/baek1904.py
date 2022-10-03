"""
22/06/21 동적 프로그래밍
1904번 실버3 01타일
"""
import time
N = int(input())
ans = [0]*1000001
ans[1] = 1
ans[2] = 2
def tile(n):
    for i in range(3,n+1):
        ans[i] = (ans[i-1]+ans[i-2])%15746
    return ans[n]
start = time.process_time()
print(tile(N))
end = time.process_time()
print('process time = %.5f' %(end - start))
