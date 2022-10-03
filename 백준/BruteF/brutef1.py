"""
22/06/05
백준 1436번 실버5
"""
a = int(input())
cnt = 0
start = 666
while True:
    if '666' in str(start):
        cnt += 1
    if cnt == a:
        print(start)
        break
    start += 1