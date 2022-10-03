a = [list(map(int, input().split())) for _ in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        if a[i][j] == 0:
            zero.append((i,j))
def test(i,j):
    pro = [1,2,3,4,5,6,7,8,9] # 될 수 있는 숫자 후보군에서 제거할거임

    for k in range(9): #행열검사
        if a[i][k] in pro: #같은 행 검사 
            pro.remove(a[i][k]) # 이미 있는 숫자는 제거
        if a[k][j] in pro: #같은 열 검사
            pro.remove(a[k][j])
    #3x3검사
    i //= 3 #3으로 나눈 몫으로 위치를 찾는다
    j //= 3 #0(0,1,2),1(3,4,5),2(6,7,8)로 나누어진다
    for m in range(i*3,i*3+3): # 3x3 범위를 지정한다.
        for n in range(j*3,j*3+3):
            if a[m][n] in pro:
                pro.remove(a[m][n])
    return pro #안되는 것들은 다 제거후 남은 숫자리스트만 출력 한개가 아닐수도 있

flag = False #중복출력막기위한 플래그
def dfs(x): #백트래킹, 매개변수는 검사한 0의 개수를 의미 
    global flag
    if flag: #flag == True 면 바로 return
        return
    if x == len(zero): #두 수가 같아지면 모든 빈칸을 검사했다는 의미
        for i in a: #[0][~], [1][~] 이런 식으로 출력
            print(*i) # *를 붙이면 리스트를 []없이 한 줄에 출력해줌
        flag = True # flag True로 바꿔줌
        return
    else:
        (one,two) = zero[x] # 빈칸의 좌표를 변수에 담음
        res = test(one,two) #테스트결과 리스트를 만듦

        for i in res:
            a[one][two] = i #원래 빈칸이었던 좌표에 골라낸 숫자를 집어넣음
            dfs(x+1) #다음 0으로 넘어감
            a[one][two] = 0 # 아닐 경우 다시 돌아와서 0으로 초기화
dfs(0)

    




