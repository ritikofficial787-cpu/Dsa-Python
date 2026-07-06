#Deletion in a 2-Dimensional Array
#After the deletion of a row or column the size of the array will be reduced by 1.
#  We can use numpy library to delete a row or column from a 2-D array.
#  We can use np.delete() function to delete a row or column from a 2-D array. 
# The syntax of np.delete() function is np.delete(array, index, axis) where array is the input array, index is the index of the row or column to be deleted and axis is the axis along which the deletion is to be performed. \
# If axis is 0 then we are deleting a row and if axis is 1 then we are deleting a column.

import numpy as np
twoDArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoDArray)
print("****************")
newTwoDArray = np.delete(twoDArray, 1, axis=1) #if axis is 0 then we are deleting a row and if axis is 1 then we are deleting a column
print(newTwoDArray)