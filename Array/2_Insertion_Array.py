#Insertion

# myArray = |"a"|"b"|"c"|   |   |   |
#            [0] [1] [2] [3] [4] [5]
#myArray[3]="d"
#myArray[5]="r"
# To replace a data in array  means if we add f at index at 0 then all elmets move in right-side.
# myArray= |"f"|"a"|"b"|"c"|"d"|"e"|-->This is time consuming becasue we have a millions of number then problem happens
#if arrray is full and we want to add a elemnts so we increase the size of array-----It's also time consuming 


from array import *
arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d',[4.5,5.6,6.5])

#arr1.insert(6,7)
#arr2.insert(1,3.9)


arr1.insert(6,-4)


print(arr1)
print(arr2)

#Time complexity of array insertion in beggoning O(N)
#Time complexity of array insertion if array is full then o(n)

#Time complexity of array insertion in the end O(1)