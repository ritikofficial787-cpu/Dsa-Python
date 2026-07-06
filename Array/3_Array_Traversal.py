#Array Traversal:- Traversal meanss visiting or accessing every element in the array sequentially (one by one), 
#                  from the start to the end.


from array import *
arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d',[4.5,5.6,6.0,7,8,9])

#arr1.insert(6,-4)
#print(arr1)

def traversearray(array):
    for i in array:
        print(i)
traversearray(arr1)
traversearray(arr2)