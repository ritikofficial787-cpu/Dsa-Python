#Check if number is present in the array or not

import numpy as np
my_array=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
def missingnumber(array,number):
    for i in range(len(array)):
        if array[i] == number:
            print(i)
        
missingnumber(my_array, 1)
    