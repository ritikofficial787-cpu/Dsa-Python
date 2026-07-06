"""
Minimum cost to reach the last cell

Problem Statement:
- 2D Matrix is given
- Each cell has a cost associated with it for accessing
- We need to start from (0,0) cell and go till (n-1,n-1) cell
- We can go only to right or down cell from current cell
- Find the way in which the cost is minimum
"""
"""
Example:

Matrix:
4  7  8  6  4
6  7  3  9  2
3  8  1  2  4
7  1  7  3  7
2  9  8  9  3

Start at (0,0) -> End at (4,4)
Path with minimum cost (right/down moves only):
4 -> 6 -> 3 -> 1 -> 2 -> 3 -> 7 -> 3
(row 0 -> down, down, right, right, down, down, right)

Min Cost : 36 

 -Subproblem:-
      Option1 = y + 9+3   
      Option2 = y+ 7+3
        Min(option1, option2)

----Algorithm:-
     findMinCost(twoDArray, row, col):
      If row == -1 or col == -1
        return inf
      If row == 0 and col ==0:
         return twoDArray [row][col]
      
      Else
         op1 = findMinCost(twoDArray, row-1, col)
         op2 = findMinCost(twoDArray, row , col-1)
           return cost[row] [col] + min(op1, op2)
"""   

def findMinCost(twoDArray ,row, col):
    if row == -1 or col == -1:
        return float('inf')
    elif row==0 and col==0:
        return twoDArray[row][col]
    else:
        op1 = findMinCost(twoDArray, row-1,  col)
        op2 = findMinCost(twoDArray, row, col-1)
        return twoDArray[row][col] + min(op1,op2)
    
TwoDList = [[4,7,8,6,4],
            [6,7,3,9,2],
            [3,8,1,2,4],
            [7,1,7,3,7],
            [2,9,8,9,3]
            ]

print(findMinCost(TwoDList, 4, 4))