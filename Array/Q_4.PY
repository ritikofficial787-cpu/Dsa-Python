# How to find maximum product of two intger where all elements are positive

import numpy as np

my_array=np.array([0,1,2,3,4,5,6,7,45,56,8,9,10,11,12,13,14,1516,17,18,19,20])

def minimumproduct(array):
  minproduct=float('inf')
  for i in range(len(array)):
    for j in range(i+1, len(array)):
      if array[i]*array[j] <minproduct:
        minproduct=array[i]*array[j]
        pairs=str(array[i]) +" ,"+ str(array[j])
        
    

  print(pairs)

  print(minproduct)
minimumproduct(my_array)



