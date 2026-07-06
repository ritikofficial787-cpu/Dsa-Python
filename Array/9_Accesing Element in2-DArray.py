#Access an element of two dimensional Array

import numpy as np
my_array=np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])
print(my_array)

def accessElement(array,  coloumnindex, rowindex):
    if rowindex>=len(array) or coloumnindex>=len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowindex][coloumnindex])
accessElement(my_array,1,2)