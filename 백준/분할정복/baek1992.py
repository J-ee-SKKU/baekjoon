"""
22/07/27
1992번 실버1 쿼드트리
"""
import sys
input = sys.stdin.readline
N = int(input())
square = [list(map(int, input().rstrip())) for _ in range(N)]
arr = []
def dps(x, y, n):  # 검사를 시작하는 좌표와 몇칸짜리 정사각형을 검사할지
    color = square[x][y]  # 처음 좌표의 색 0 or 1
    for i in range(x, x+n):  # x좌표
        for j in range(y, y+n):  # y좌표
            if square[i][j] != color:
                arr.append('(')#다른색만나서 사각형 쪼갤때 괄호추가
                nn = n//2
                dps(x, y, nn)
                dps(x, y+nn, nn)
                dps(x+nn, y, nn)
                dps(x+nn, y+nn, nn)
                arr.append(')') #끝나면 괄호닫기
                return
    arr.append(color)
dps(0,0,N)
print(''.join(map(str,arr)))

