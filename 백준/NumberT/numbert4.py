"""
왜 틀린지 모르겠다 ㅅㅂㅅㅂㅅㅂㅅㅂㅅ
"""


import math
N = int(input())
s = []
ans = []
gcd = 0
for i in range(N):
    s.append(int(input()))
    s.sort()
for i in range(len(s)): # 최대공약수 구하기
    if i==0:
        continue
    if i==1:
        gcd = s[1]-s[0]
    gcd = math.gcd(s[i]-s[i-1],gcd)
gcd_A =int(gcd ** 0.5) # 최대공약수의 제곱근 최대공약수 전부를 for문 돌리면 시간초과나므로
for i in range(2,gcd_A+1): #최대공약수의 약수 구하기
    if gcd%i == 0:
        ans.append(i)
        ans.append(gcd//i)
ans.append(gcd) # 위의 식에서 1로 나누지 않기 때문에 약수리스트에 자기 자신이 안들어간다
#그래서 따로 추가해준다.
ans = list(set(ans)) # 제곱수인경우 수가 중복해서 들어가므로 set로 없애줘야함
ans.sort()
for i in ans:
    print(i, end = '')

