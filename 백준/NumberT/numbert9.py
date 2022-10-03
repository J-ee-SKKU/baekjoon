"""
22/06/04 - 22/06/05
백준 2004번 실버2
끝자리 0개수 출력하기
"""
n,m = map(int,input().split())
def count_num(n,k): #1~n 사이의 k가 곱해진 개수 구하기
    count = 0
    while n: # n==0이면 False가 되어 탈출
        n //= k # n에 k로 나눈 몫을 넣는다
        count += n #몫을 누적시킨다
    return count
five_count = count_num(n,5) - count_num(m,5) - count_num(n-m,5) #nCm
two_count = count_num(n,2) - count_num(m,2) - count_num(n-m,2)
#2와 5중에 더 적은 개수만큼 10이 만들어지므로 더 적은 개수가 0의 개수가 된다
ans = min(five_count,two_count)
print(ans) 




