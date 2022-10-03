T = int(input())

def lcm(x, y):
    a = max(x,y)
    b = min(x,y)
    c = 0
    z = a*b #숫자바뀌기전에 미리 곱해놓은 값
    while True:
        if a%b == 0:
            break
        else:
            c = a
            a = b
            b = c%a # 원래의 a%b
    print(round(z/b))
    return
    
for i in range(T):
    a,b = list(map(int,input().split()))
    lcm(a,b)


