"""
22/06/25 동적 프로그래밍
2579번 실버2 계단오르기
"""
#존나 헷갈림
N = int(input())
arr = [0]
for _ in range(N):
    arr.append(int(input()))
sum = [0]*301
sum[1] = arr[1]
if N == 1:
    print(sum[1])
elif N == 2:
    sum[2] = arr[1] + arr[2]
    print(sum[2])
else:
    sum[2] = arr[1] + arr[2]
    for i in range(3,N+1):
        sum[i] = max(arr[i]+sum[i-2],arr[i]+arr[i-1]+sum[i-3])
    print(sum[N])


