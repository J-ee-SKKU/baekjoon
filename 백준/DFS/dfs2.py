"""
22/06/13-14
백준 2447번 별찍기-10 실버1
"""
N = int(input())
def star(n):
    if n == 3:
        arr = ['***','* *','***']
        return arr
    stars = star(n//3) 
    result = []
    for i in stars: #여기서 재귀실행
        result.append(i*3)
    for i in stars:
        result.append(i+' '*(n//3)+i) # n=3일때 공백한칸 n=9일때 공백 세칸이므로
    for i in stars:
        result.append(i*3)
    return result

print(*star(N),sep='\n')
        
   
    
