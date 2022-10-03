"""
22/06/05 ~ 22/06/06
백준 9663번 N-Queen 골드4
시간 너무 오래 걸림 >> 줄일 방법 생각하기
"""
n = int(input())
arr = list(0 for i in range(n))
cnt = 0
def test(hang): #행을 받아서 그자리에 넣어도 되는 지 검사하는 함수
    if hang == 0: # 첫행은 무조건 true
        return True
    for i in range(hang): #이미 들어가있는 수들과 대각선자리에 있는 지 검사
        if abs(hang-i) == abs(arr[hang]-arr[i]):
            return False
        elif arr[i] == arr[hang]: # 같은 행에 있지 않은지 검사
            return False
    return True

def N_queen(hang):
    global cnt
    if hang == n: # ex) n=5라면 hang은 4이므로 마지막행을 넘었다는 건 다 채웠다는 의미
        cnt += 1
        return
    else:
        for i in range(n):
            arr[hang] = i
            if test(hang): #test 통과했다면 다음행으로 이동
                N_queen(hang+1)  # 다음행

N_queen(0) #0행부터 시작
print(cnt)
