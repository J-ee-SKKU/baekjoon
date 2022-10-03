"""
22/06/04
백준 9375번 실버3"""
n = int(input()) # 테스트케이스 개수
for i in range(n):
    closet = {}
    m = int(input()) # 옷 개수
    for j in range(m):
        name, type = input().split()
        if type in closet: #closet key에는 옷 종류를 넣어놓는다
            closet[type] += 1 
        else:
            closet[type] = 1
    ans = 1
    for key in closet.keys():
        ans = (closet[key] + 1) * ans
    print(ans-1)
