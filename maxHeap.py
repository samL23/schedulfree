import sys
import maxHeap

class MaxHeap: 
    
    def __init__(self, maxsize) -> None:
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    def parent(self, pos): 
        return pos //2
    
    def leftChild(self, pos): 
        return pos*2
    
    def rightChild(self, pos): 
        return (pos*2)+1
    
    def isLeaf(self, pos): 
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False
    
    def swap(self, apos, bpos):
        self.Heap[apos], self.Heap[bpos] = (self.Heap[bpos], self.Heap[apos])

    def maxHeapify(self, pos): 
        #if node is a parent and smaller than child
        if not self.isLeaf(pos): 
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or self.Heap[pos] < self.Heap[self.rightChild(pos)]):
                 #swap w left child and heapify
