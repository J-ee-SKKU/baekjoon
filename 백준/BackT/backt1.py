n,m = map(int, input().split())
arr = [] 
def dfs():
    if len(arr) == m : 
        print(' '.join(map(str,arr)))#join 사용해서 리스트를 문자열로 출력
        return #출력했으니까 재귀탈출
    for i in range(1,n+1): #제일 앞에 출력되는 수
        if i in arr: #반복되는 경우는 넘어가기
            continue
        arr.append(i) #반복되지 않는 경우에 추가
        dfs() #다음 노드(자리) 내려가는 상황(재귀함수호출) 탈출시에도 여기로 와서 마저 실행
        arr.pop() #return한 후에 pop(제일 마지막 자리 없앰)해서 옆에 노드로 넘어갈 수 있게 함
        
dfs() #실행