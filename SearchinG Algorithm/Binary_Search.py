#   Binary Search Pseudocode

# -Create function with two parameters which are a sorted array and a value.
# -Create two pointers: a left pointers at the start of the array and a right pointer at the end of the array.
# -Based on left and right pointers calculate middle pointer
# -While  middle is not equal to the value and start<=end loop:
    #  -if the middle is grater than the value move the right pointer down 
    #  -if the middle is less than the value move the left pointer up.
# -If the value is not found return -1

import math
def binarySearch(array, value):
    start=0
    end= len(array)-1
    middle=math.floor((start + end)/2)
    while not(array[middle] == value) and start <=end:
        if value < array[middle]:
            end=middle-1
        else:
            start=middle+1
        middle = math.floor((start + end)/2)
        #print(start, middle, end)

    if array[middle]==value:
        return middle
    else:
        return -1





custArray=([2,3,4,5,6,7,8,9,11])
print(binarySearch(custArray, 7))
#[2, 3, 4, 5, 6, 7, 8, 9, 11]
# S           M            E
