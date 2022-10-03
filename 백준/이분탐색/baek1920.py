"""
22/08/30 이분탐색
1920번 실버4 수찾기
"""
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
M = int(input())
test=list(map(int,input().split()))
A = sorted(A)
"""
먼저 오름차순으로 정렬한 다음
가장 가운데 숫자랑 비교한다
가운데 숫자보다 작다면 앞부분으로 넘어가서
가장 가운데 숫자를 찾고 반복
만약 짝수개라면 가운데 숫자가 없기 때문에 절반나누고 +1 번째 숫자와 비교
"""
def bs(arr, low, high, key):
    while(low <= high):
        mid = (low+high)//2
        if arr[mid] == key:
            return 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return 0

for i in test:
    print(bs(A,0,len(A)-1,i))

