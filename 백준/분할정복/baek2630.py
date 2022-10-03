"""
22/07/26
2630번 실버2 색종이 만들기
"""
N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
w = 0
b = 0
def dps(x,y,n): #검사를 시작하는 좌표와 몇칸짜리 정사각형을 검사할지
    global w,b
    color = paper[x][y] #처음 좌표의 색 0 or 1
    for i in range(x,x+n): #x좌표
        for j in range(y,y+n): #y좌표
            if paper[i][j] != color:
                nn = n//2
                dps(x,y,nn)
                dps(x,y+nn,nn)
                dps(x+nn,y,nn)
                dps(x+nn,y+nn,nn)
                return
    #for문 빠져나오는 경우는 범위내에 숫자가 모두 같을 경우
    if color == 0:
        w += 1
        return
    elif color == 1:
        b += 1
        return
dps(0,0,N)
print(w)
print(b)
