# 3. Write a program to check if two strings are a rotation of each other?

def checkRotation(str1, str2): 
    str_sum = ""
  
    if len(str1) != len(str2): 
        return False
   
    str_sum = str1 + str1 
  
    
    if str2 in str_sum:
        return True
    else: 
        return False
 
string1 = input("Enter first word :")
string2 = input("Enter second word :")
  
if checkRotation(string1, string2): 
    print("Given Strings are rotations of each other")
else: 
    print("Given Strings are not rotations of each other")