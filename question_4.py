# 4. Write a program to print the first non-repeated character from a string?

str1 = input("Enter a word :")
str2 = str1.upper()
index = -1
result = ""
for i in str2:
    if str2.count(i) == 1:
        result += i
        break
    else:
        index += 1
if index != 1:
    print("First non-repeating character is", result)