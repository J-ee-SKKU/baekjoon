"""
22/07/05 동적 프로그래밍
2565번 골드5 전깃줄
"""
"""
겹치지 않으려면 A의 숫자 크기대로 정렬했을때 B도 계속 커져야한다. 
그러므로 A를 정렬했을 때 B의 가장 긴 증가하는 수열을 찾고 이 수열을 제외한 만큼 삭제하면 된다.
"""
#전깃줄은 100개이하, 숫자는 1~500
N = int(input())
line = [list(map(int,input().split())) for _ in range(N)]
cnt = [1]*N
line = sorted(line)
for i in range(N): #0~ N-1
    for j in range(i): #0~ i-1
        if line[j][1] < line[i][1]:
            cnt[i] = max(cnt[i],cnt[j]+1)
print(N-max(cnt))

