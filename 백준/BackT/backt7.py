"""
22/06/12
백준 14888번 연산자 끼워넣기 실버1
"""
N = int(input())
num = list(map(int,input().split()))
op = list(map(int, input().split()))
opzip = ['+','-','*','//']
ans = num[0] #첫번째 숫자부터 시작
maxr = -1000000001
minr = 1000000001
def dfs(n): #n은 1부터 시작 어차피 숫자 시작은 num[0]로 같음 
    global ans
    global maxr
    global minr
    if n == N:
        maxr = max(maxr,ans)
        minr = min(minr,ans)
        return
    for i in range(4):
        tmp = ans #tmp에 ans 저장해두고 다시 돌아올 수 있도록 함
        if op[i] > 0: #연산자가 있는지
            if i == 0: # +일때
                ans += num[n]
            elif i == 1: # -일때
                ans -= num[n]
            elif i == 2: # *일때
                ans *= num[n]
            else: # //일때
                if ans >= 0:
                    ans //= num[n]
                else:
                    ans = (abs(ans)//num[n])*(-1)
            #한번계산했으면 다음 노드로 넘어가는 재귀함수 호출
            op[i] -= 1 # 한번계산한 연산자 제거해주기
            dfs(n+1) #다음재귀함수호출
            #return 받고 해야할일
            ans = tmp #바로 전 계산결과로 돌리기
            op[i] += 1 #바로 전으로 돌아왔으니 제거해준 연산자도 돌려주기
dfs(1)
print(maxr)
print(minr)



    