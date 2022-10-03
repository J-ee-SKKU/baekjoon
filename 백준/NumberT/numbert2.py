a,b = list(map(int,input().split()))
c = 0
d = a*b
while True:
    if a%b == 0:
        break
    else:
        c = a
        a = b
        b = c%b
print(b)
print(round(d/b))