# 8. Write a program to check if all the brackets are closed in a given code snippet.

def brackets_closed(exp):
    stack = []
 
    for char in exp:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            bracket = stack.pop()
            if bracket == '(':
                if char != ")":
                    return False
            if bracket == '{':
                if char != "}":
                    return False
            if bracket == '[':
                if char != "]":
                    return False
 
    if stack:
        return False
    return True

if __name__ == "__main__":
    exp = input("Enter your code :")

    if brackets_closed(exp):
        print("All brackets are closed")
    else:
        print("Brackets are not closed")