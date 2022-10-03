"""
22/06/24 동적 프로그래밍
1149번 실버1 RGB거리
"""
#R G B
#0 1 2
"""
n줄있으면 
첫줄 경우의수 3
n-1줄동안은 두개씩 2**(n-1)
총 경우의수 3*(2**(n-1))
arr[i][0] arr[i][1] arr[i][2]
arr[i+1][0] arr[i+1][1] arr[i+2][2]
여기서 arr[i+1][0] 은 arr[i][1]과 arr[i][2] 중 더 작은 것과 더한 값으로 대체
DP는 했던 걸 또 안하도록 하는 것이 중요 
수행한 결과를 저장하면서 진행해야함!!
"""
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(0,N-1): 
    arr[i+1][0] = arr[i+1][0] + min(arr[i][1], arr[i][2])
    arr[i+1][1] = arr[i+1][1] + min(arr[i][0], arr[i][2])
    arr[i+1][2] = arr[i+1][2] + min(arr[i][0], arr[i][1])
print(min(arr[N-1]))
