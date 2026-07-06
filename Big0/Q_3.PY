"""
   def printUnorderPairs(arrray):
   for i in range(0,len(array)):
      for j in range(i+1, len(array)):
        print(array[i]+ "," + array[j]) 
"""
#Time Complexity:
#1. Counting iterations
#1st------>n-1
#2nd------>n-2
#
#(n-1)(n-2)+(n-3)+...+2+1
# = 1+2+...+(n-3)+(n-2)+(n-1)
#=n(n-1)/2
#n^2/2+n
#n^2
#Time complexity: O(N^2)