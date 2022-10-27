# 1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def printPairs(arr, length, sum):

    for i in range(0, length ):
        for j in range(i + 1, length ):
            if (arr[i] + arr[j] == sum):
                print("(", arr[i],
                      ", ", arr[j],
                      ")", sep = "")

arr = []
size = int(input("Enter size of array :"))
for k in range(size):
    element = int(input("Enter a number :"))
    arr.append(element)
print(arr)
sum = int(input("Enter a number whose pairs of sum you want from array :"))
length = len(arr)
printPairs(arr, length, sum)