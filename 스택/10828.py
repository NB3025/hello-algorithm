a = int(input())

class NB_Stack:
    def __init__(self):
        self.arr = []
    
    def push(self, n):
        self.arr.append(n)
    
    def top(self):
        if len(self.arr) == 0:
            return -1
        else:
            return self.arr[-1]
    
    def size(self):
        return len(self.arr)
    
    def empty(self):
        if len(self.arr)==0:
            return 1
        else:
            return 0
    
    def pop(self):
        if len(self.arr)==0:
            return -1
        
        res = self.arr[-1]
        self.arr.remove(res)
        return res
        
stack = NB_Stack()
for i in range(a):
    num = int(input())
    