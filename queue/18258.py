class myQueue():

    def __init__(self):
        self.arr = []
        self.cnt = 0
    
    def push(self,n):
        self.arr.append(n)
        return 0
    
    def pop(self):
        if len(self.arr)==0:
            return -1
        if len(self.arr) <= self.cnt:
            return -1
        res = self.arr[self.cnt]
        self.cnt +=1
        return res
    
    def size(self):
        return len(self.arr) - self.cnt
    
    def empty(self):
        if (len(self.arr) - self.cnt)==0:
            self.cnt = 0
            self.arr = []
            return 1
        else:
            return 0
        
    def front(self):
        if (len(self.arr) - self.cnt)==0:
            return -1
        if len(self.arr) > self.cnt:
            return self.arr[self.cnt]
    
    def back(self):
        if (len(self.arr) - self.cnt)==0:
            return -1
        if len(self.arr) > self.cnt:
            return self.arr[-1]

import sys

N = int(sys.stdin.readline())

queue = myQueue()
for _ in range(N):
    input = sys.stdin.readline().strip().split()
    command = input[0]
    if len(input)==2:
        value = int(input[1])

    if command == 'push':
        queue.push(value)
    elif command == 'pop':
        print (queue.pop())
    elif command == 'size':
        print (queue.size())
    elif command == 'empty':
        print (queue.empty())
    elif command == 'front':
        print (queue.front())
    elif command == 'back':
        print (queue.back())
    

