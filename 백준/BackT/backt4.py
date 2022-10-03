"""
22/06/05
백준 15652번 실버3
"""
#비내림차순 + 중복O
n, m = map(int, input().split())
arr = []
def dfs(s):
    if len(arr) == m:
        print(' '.join(map(str, arr)))  # join 사용해서 리스트를 문자열로 출력
        return  # 출력했으니까 재귀탈출
    for i in range(s, n+1):  # 범위가 s부터면 i가 2로 바뀌면 뒤로 2이상의 수만 올 수 있다
        arr.append(i)   # 추가
        dfs(i)  # 다음 노드(자리) 내려가는 상황(재귀함수호출) 탈출시에도 여기로 와서 마저 실행
        arr.pop()  # return한 후에 pop(제일 마지막 자리 없앰)해서 옆에 노드로 넘어갈 수 있게 함

dfs(1)  # 실행
