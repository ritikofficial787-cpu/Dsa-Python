# Number of paths to reach the last cell with given cost
#
# Problem Statement:
# - 2D Matrix is given
# - Each cell has a cost associated with it for accessing
# - We need to start from (0,0) cell and go till (n-1,n-1) cell
# - We can go only to right or down cell from current cell
# - We are given total cost to reach the last cell
# - Find the number of ways to reach end of matrix with given "total cost"
#
# Example:
# Total cost : 25
#
# Matrix:
# 4  7  1  6
# 5  7  3  9
# 3  2  1  2
# 7  1  6  3
#
# Answer 1 (path sum = 25):
# 4 -> 7 -> 1 -> 3 -> 1 -> 6 -> 3
# (right, right, down, down, down, right)
#
# Answer 2 (path sum = 25):
# 4 -> 5 -> 7 -> 3 -> 2 -> 1 -> 3
# (down, right, right, down, down, right)
#
# Number of ways to reach end with total cost 25 : 2

#subproblem::
# Option1 = y+2 =22  f(3,4,22)  3rd row and 4th column
# option2 = y+6 = 22  f(4,3,22)  4th row and 3rd column
# sum(option1, option2)

#Algorithm:-
# findNumOfPaths(twoDArray, row, col, totalCost):
#    If cost <0:
#     return 0
#    elif row == 0 and col == 0:
#        if twoDArray[0][0] - cost == 0:
#           return 1
#        else:
#              return 1
#     elif row == 0:
#            return findNumofPaths(twoDArray, 0, col-1, cost- twoDArray[row][col])
#     elif col == 0:
#             return findNumofPaths(twoDArray, row-1, col, twoDArray[row][col])
#     else:
#         op1=findNumofPaths(twoDArray, row-1, col, cost - twoDArray[row][col])
#         op2=findNumofPaths(twoDarray, row, col-1, cost - twoDArray[row][col])
#          return op1+op2


def findNumofPaths(twoDArray, row,col,cost):
    if cost < 0 :
        return 0
    elif row == 0 and col == 0:
        if twoDArray[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return findNumofPaths(twoDArray, 0, col-1, cost - twoDArray[row][col])
    elif col == 0:
        return findNumofPaths(twoDArray, row-1, 0, cost - twoDArray[row][col])
    else:
        op1= findNumofPaths(twoDArray, row-1, col, cost- twoDArray[row][col])
        op2= findNumofPaths(twoDArray, row, col-1, cost-twoDArray[row][col])
        return op1+op2
    
TwoDList = [[4,7,1,6],
            [5,7,3,9,],
            [3,2,1,2],
            [7,1,6,3]
            ]

print(findNumofPaths(TwoDList, 3, 3, 25))