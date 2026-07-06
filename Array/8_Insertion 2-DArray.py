# If we add a column then the other columns will be shifted to the right and 
# if we add a row then the other rows will be shifted downwards.
#Time complexity will be o(mn) where m is number of rows and n is number of columns

import numpy as np
twoDArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoDArray)

print("****************")

newTwoDArray = np.insert(twoDArray, 1, [[10,11,12]], axis=0) #if axis is 0 then we are adding a row and if axis is 1 then we are adding a column
print(newTwoDArray)

newTwoDArray = np.append(twoDArray, [[10,11,12]], axis=0) #if axis is 0 then we are adding a row and if axis is 1 then we are adding a column
print(newTwoDArray)