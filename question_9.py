# 9. Write a program to reverse a stack.

class Stack:
 
    def __init__(self):
        self.elements = []
         
    def push(self, value):
        self.elements.append(value)
       
    def pop(self):
        return self.elements.pop()
     
    def empty(self):
        return self.elements == []
     
    def show(self):
        for value in reversed(self.elements):
            print(value)

def bottominsert(stck , value):
   
    if stck.empty():
         
        stck.push(value)
         
    else:
        popped = stck.pop()
        bottominsert(stck , value)
        stck.push(popped)
 
def reverse(stck):
    if stck.empty():
        pass
    else:
        popped = stck.pop()
        reverse(stck)
        bottominsert(stck , popped)

stk = Stack()
 
size = int(input("Enter size of stack :"))
for i in range(size):
    value = int(input("Enter a number :"))
    stk.push(value)
 
print("Original Stack")
stk.show()
 
print("\nStack after Reversing")
reverse(stk)
stk.show()