N = int(input())
arr = [] # 주어진 수들
up = [] # dic 업데이트용 배열
ans= {} # 나누는 수와 나머지 저장하는 dic
for i in range(N):
    arr.append(int(input()))

for i in range(1,arr[1]+1): # 첫번째와 두번째 수의 공통 해 찾는 과정
    if (arr[0] % i) == (arr[1] % i):
        ans[i] = arr[0]%i
    else:
        continue
out = list(ans.keys()) #첫번째랑 두번째 겹치는 숫자들만 따로 모음

for k in range(2,len(arr)): #주어진 배열 모두 검사
    for i in ans: #{}에 있는 숫자들로 검사
        if arr[k] % i != ans[i]: #첫 두 수의 결과랑 다르면 제외
            if i in out:
                out.remove(i) 
                up.append(i)
    for j in up:
        del ans[j]
    up = []
            
strout = list(map(str,out))
print(' '.join(strout))