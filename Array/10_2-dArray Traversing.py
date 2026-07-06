#Traversing a 2-Dimensional Array

import numpy as np
twoDArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoDArray)
def traverse2DArray(array):
    for r in range(len(array)):
        for c in range(len(array[0])): #in len(array[0]) we are getting the number of columns in the array
            print(array[r][c])

traverse2DArray(twoDArray)