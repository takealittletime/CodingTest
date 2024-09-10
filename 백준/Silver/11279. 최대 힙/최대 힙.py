import sys

class maxHeap:
    def __init__(self):
        self.heap = []

    def push(self,val):
        self.heap.append(val)
        self._heapify_up(len(self.heap)-1)
    
    def pop(self):
        
        if len(self.heap) == 0:
            return 0
        
        max = self.heap[0]

        if len(self.heap) > 1: #힙의 크기가 1보다 큰 경우
            self.heap[0] = self.heap.pop()
            self._heapify_down(0)
        else: #힙의 크기가 1인 경우
            self.heap.pop()

        return max


    def _heapify_up (self,index):
        parent_index = (index-1)//2
        while (index >0 and self.heap[parent_index] < self.heap[index]):
            self.heap[parent_index],self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
            parent_index = (index-1)//2
    
    def _heapify_down (self, index):
        largest = index
        size = len(self.heap)

        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2

            if (left_child_index < size and self.heap[left_child_index] > self.heap[largest]):
                largest = left_child_index
            if (right_child_index < size and self.heap[right_child_index] > self.heap[largest]):
                largest = right_child_index
            if (largest != index):
                self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
                index = largest
            else:
                break

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])

heap = maxHeap()

for command in data[1:]:
    command = int(command)
    
    if command == 0:
        print(heap.pop())
    else:
        heap.push(command)