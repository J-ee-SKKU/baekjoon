"""
22/06/20 집합과 맵
11478번 실버3 서로 다른 부분 문자열의 수
"""
S = input()
ans = set()
# ls = tuple(S) 이것때문에 메모리 초과남
for i in range(len(S)):  # 시작위치정하기
    for j in range(i, len(S)):
        ans.add(S[i:j+1])
print(len(ans))
