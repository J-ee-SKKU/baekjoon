"""
22/06/14
백준 11729번 하노이탑 실버1
tlqkf 진짜 아이디어 미쳤다 어케 생각하지
"""
N = int(input())
def hanoi(n,start,end): #n개를 s에서 e로
    if n == 1:
        print(start,end)
        return
    hanoi(n-1,start,6-start-end) #n-1개를 지금있는위치와 목적지를 제외한 곳으로 옮겨둠
    print(start,end) #남아있는지금위치의 한개를 목적지로 옮김
    hanoi(n-1,6-start-end,end) #아까 옮긴 n-1개를 다시 목적지로 옮김
print(2**N-1)
hanoi(N,1,3)
    

   
     