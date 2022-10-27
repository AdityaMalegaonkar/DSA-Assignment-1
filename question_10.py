# 10. Write a program to find the smallest number using a stack.

from collections import deque
 
 
class MinStack:
    def __init__(self):
        self.stk = deque()
        self.min = None
 
    def push(self, value):
        if not self.stk:
            self.stk.append(value)
            self.min = value
        elif value > self.min:
            self.stk.append(value)
        else:
            self.stk.append(2*value - self.min)
            self.min = value
 
    def pop(self):
        if not self.stk:
            self.print('Stack underflow!!')
            exit(-1)
        top = self.stk[-1]
        if top < self.min:
            self.min = 2*self.min - top
        self.stk.pop()
 
    def getMin(self):
        return self.min
 
 
if __name__ == '__main__':
 
    stk = MinStack()
 
    stk.push(6)
    print(stk.getMin())
 
    stk.push(7)
    print(stk.getMin())
 
    stk.push(5)
    print(stk.getMin())
 
    stk.push(3)
    print(stk.getMin())
 
    stk.pop()
    print(stk.getMin())
 
    stk.pop()
    print(stk.getMin())