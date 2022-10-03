"""
22/06/21 동적 프로그래밍
9184번 실버2 신나는 함수 실행
"""
"""
시간재는법
import time
start = time.process_time()
end = time.process_time()
end - start
"""

dp = [[[0]*21 for _ in range(21)] for _ in range(21)] #결과값저장할 3차원 배열
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:  # 비어있다면 0이 들어있을테니 false가 된다. 값이 있다면 재귀할 필요없이 바로 리턴
        return dp[a][b][c] #들어있는 값 반환
    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]
while True:
    a,b,c = map(int, input().split())
    if [a,b,c] == [-1,-1,-1]:
        break
    print("w(%d, %d, %d) = %d" %(a, b, c, w(a,b,c)))



