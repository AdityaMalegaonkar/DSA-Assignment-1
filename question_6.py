# 6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def operator(opt):
 
    if opt == "+":
        return True
 
    if opt == "-":
        return True
 
    if opt == "/":
        return True
 
    if opt == "*":
        return True
 
    return False
 
 
def posttopre(postfix):
 
    lst = []
 
    length = len(postfix)
 
    for i in range(length):
 
        if (operator(postfix[i])):
 
            opt1 = lst[-1]
            lst.pop()
            opt2 = lst[-1]
            lst.pop()
 
            temp = postfix[i] + opt2 + opt1
 
            lst.append(temp)
 
        else:
            lst.append(postfix[i])
 
    
    ans = ""
    for i in lst:
        ans += i
    return ans

if __name__ == "__main__":
 
    postfix = input("Enter a postfix expression :")
     
    print("Prefix : ", posttopre(postfix))