"""
22/06/24 동적 프로그래밍
1912번 실버2 연속합
"""
N = int(input())
arr = list(map(int,input().split()))
def seq():
    for i in range(1,N):
        if arr[i] < arr[i-1] + arr[i]:
            arr[i] = arr[i-1] + arr[i]
    return max(arr)
print(seq())