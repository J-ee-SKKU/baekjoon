"""
22/06/25 동적 프로그래밍
1932번 실버1 정수삼각형
"""
"""
"""
N = int(input())
arr = [list(map(int, input().split())) for _ in range(1,N+1)]
for i in range(1,N):
    for j in range(i+1):
        if j==0:
            arr[i][j] = arr[i][j] + arr[i-1][0]
        elif j == i:
            arr[i][j] = arr[i][j] + arr[i-1][j-1]
        else:
            arr[i][j] = arr[i][j] + max(arr[i-1][j-1],arr[i-1][j])
print(max(arr[N-1]))