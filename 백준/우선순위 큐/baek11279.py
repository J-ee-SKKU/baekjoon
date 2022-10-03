"""
22/09/14 우선순위 큐
11279번 실버2 최대 힙
"""
#우선순위 큐
#들어간 순서에 상관없이 우선순위가 높은 데이터가 먼저 나오는 것
#힙 
#완전 이진 트리 (최대 힙은 부모가 더 크거나 같은 것, 최소 힙은 부모가 작거나 같은 것)
import sys
input = sys.stdin.readline
N = int(input())
class Maxheap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize #왜?
        self.FRONT = 1 #왜?
    
    def parent(self, pos):
        #부모노드의 인덱스는 2로 나눈 몫이기 때문
        return pos//2
    def leftChild(self,pos):

        return pos*2
    def RightChild(self, pos):

        return (pos*2) + 1

    def isLeaf(self, pos):
    # 자녀노드를 갖고있으면서 전체길이보다는 짧아야한다
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
    #두 노드를 교환하는 작업
        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
                                            self.Heap[fpos])

    
