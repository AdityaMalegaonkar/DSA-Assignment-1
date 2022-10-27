# 7. Write a program to convert prefix expression to infix expression.

def prefixtoinfix(prefix):
    stack = []
     
    i = len(prefix) - 1
    while i >= 0:
        if not operator(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def operator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
 
if __name__=="__main__":
    str = input("Enter a prefix expression :")
    print(prefixtoinfix(str))