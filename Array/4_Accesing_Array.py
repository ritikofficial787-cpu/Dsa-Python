#Access array
# How can we tell computer which particular value we would like to access?
#  With help of index we can access any element in array
# for ex:  arr= |"a"|"b"|"c"|
#    arr[0]="a", arr[1]="b"

from array import *
array1=["i", [1,2,3,4,5,6]]
def accessElement(array,index):
    if index >= len(array1):
        print("Their is not any element in this index")
    else:
        print(array[index])
accessElement(array, 6)