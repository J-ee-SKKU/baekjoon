 = int(input())
t = 0
for i in range(1,n+1):
    while True:
        if i%5==0:
            i = i/5
            t += 1
        else:
            break
print(t)