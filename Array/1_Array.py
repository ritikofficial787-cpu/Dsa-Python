# Creating an array in :

# When we create an array, we:
# .Assign it to variable.
# .Define the type of elements that it will store
# .Define its size(the maximum number of elements)
# ex:- my_arr=|1|2|3|4|5|
# * If we define array of size 10 then add only 5 elemnets then im memeory asssign the reserved for array.


# ARRAY In Python (Array Module)
#for array import*
#arrayName = array(typecode,[initialize])

# ex:-

from array import *
arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d',[4.5,5.6,6.0,7,8,9])


print(arr1)
print(arr2)