#Searching in a 2-Dimensional Array
#Linear seaarch is used to search an element in a 2-D array. We will traverse the whole array and check if the element is present or not. If we find the element we will return true otherwise we will return false.
import numpy as np
twoDArray = np.array([[1,2,3],[4,5,6],[
7,8,9]])
print(twoDArray)
def search2DArray(array, value):
    for r in range(len(array)):
        for c in range(len(array[0])):
            if array[r][c] == value:
                return f'The value is located at index '+str(r)+','+str(c)
            
    return 'The value is not present in the array'
print(search2DArray(twoDArray, 5))
print(search2DArray(twoDArray, 1111))