#Deletion:-
#       To delete a element in array then we move elment c on place of c and d is at place of c....
#       Deletion is efficience while removing last element otherwise it's time consuming

# |"a"|"b"|"c"|"d"| ---we cannot remove b directly from array so we place c at place b

from array import *
arr1 = array('i',[1,2,3,4,5])

arr1.remove(2)
print(arr1)