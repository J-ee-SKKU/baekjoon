"""
22/07/13 그리디
1931 실버1 회의실 배정
"""
#처음 제출할 때 중복값제거 안해서 틀린다고 어떤 미친새끼가 써놓음 아니었음 이걸로 30분은 잡아먹은듯
#  ex) [2,2], [2,2] 이럴 경우 하나만 들어가야함
#이차원 배열은 바로 set 불가능, 튜플로 변환한 후 바꿔줘야한다
N = int(input())
sch = []
for i in range(N):
    sch.append(list(map(int,input().split())))
#sch = list(set(map(tuple,sch)))
sch.sort(key=lambda x:(x[1],x[0])) #끝나는 순서대로 오름차순 정렬 같으면 시작순서
cnt = 0 
last = 0 #테이블에 제일 늦게 들어간 값의 끝나는 시간
for i,j in sch: #i는 시작시간 , j는 끝나는 시간
    if i >= last:
        cnt += 1
        last = j
print(cnt)