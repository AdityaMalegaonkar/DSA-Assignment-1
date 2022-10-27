# 2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverseList(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
 
arr = []
size = int(input("Enter size of array :"))
for i in range(size):
    element = int(input("Enter a number :"))
    arr.append(element)
print(arr)
reverseList(arr, 0, size-1)
print("Reversed list is")
print(arr)