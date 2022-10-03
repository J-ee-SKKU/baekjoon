"""
22/07/14 그리디
1541번 실버2 잃어버린 괄호
"""
# 작은 값을 만들기 위해서는 최대한 큰 값을 빼주어야 하기 때문에 - 만나면 
# 괄호치고 다시 -나오면 괄호 닫아줌 처음거에서 뒤에꺼 다 빼주면 댐
arr = input().split('-')
plus = 0
minus = 0
for i in arr[0].split('+'):
    plus += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        minus += int(j)
print(plus - minus)