"""
22/08/01 분할정복
1780번 실버2 종이의 개수
"""
import sys
input = sys.stdin.readline
N = int(input())
square = [list(map(int,input().split())) for _ in range(N)]
arr0 = 0
arr1 = 0
arrm1 = 0
def dps(x, y, n):  # 검사를 시작하는 좌표와 몇칸짜리 정사각형을 검사할지
    global arr0, arr1, arrm1
    start = square[x][y]  # 처음 좌표의 숫자 -1,0,1
    for i in range(x, x+n):  # x좌표
        for j in range(y, y+n):  # y좌표
            if square[i][j] != start:
                nn = n//3
                dps(x, y, nn)
                dps(x, y+nn, nn)
                dps(x,y+(nn*2),nn)
                dps(x+nn, y, nn)
                dps(x+nn, y+nn, nn)
                dps(x+nn, y+(nn*2),nn)
                dps(x+(nn*2), y, nn)
                dps(x+(nn*2), y+nn, nn)
                dps(x+(nn*2), y+(nn*2), nn)
                return
    #for문 빠져나오면 범위내의 숫자가 모두 같다는 의미
    if start == 0:
        arr0 += 1
    elif start == 1:
        arr1 += 1
    elif start == -1:
        arrm1 += 1
dps(0, 0, N)
print(arrm1)
print(arr0)
print(arr1)
