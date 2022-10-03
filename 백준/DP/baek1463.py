"""
22/06/25 동적 프로그래밍
1463번 실버3 1로 만들기
"""
X = int(input())
ans = [0] * (X+1)
ans[0] = -1
for i in range(1,X+1): #범위 설정할때 런타임에러 조심하기 
    ans[i] = ans[i-1] + 1 #1작은 수보다 한 번의 연산을 더하면 되므로
    if i%3 == 0:
        ans[i] = min(ans[i//3]+1,ans[i])
    if i%2 == 0:
        ans[i] = min(ans[i//2]+1,ans[i])
print(ans[X])
    
