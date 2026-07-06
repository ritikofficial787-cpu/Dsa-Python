#.Two Dimensional Array = An array with a bunch of values having been declared with double index
#. a[i][j] --> i and j betw 0 and N
#      0  1  2  3  4 5  6  7  8
#.    |0|1|33|55|91|20|51|62|74|13|
#.    |5|4|10|11|8| 11 |68|87| 12|
#.    |2|24|50|37|40|48|30|59|81|93|

# 2-D Array in python

import numpy as np

twoDarray = np.array([[11, 15, 10, 6],
                     [10, 14, 11, 5],
                     [15, 18, 14, 9]])
print(twoDarray)
print(twoDarray[2][2]) 
print(twoDarray[1][3]) 