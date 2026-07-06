 #Convert String
 # Problem Statement :-
#-S1 and S2 are given Strings
#-Convert S2 to S1 using delete, insert or replace operations
#-Find the minimum count of edit operations
#  ex:
#       -S1 = "catch"
#       -S2 = "carch"
#       -Output = 1
#       -Explanation: Replace "r" with "t"
#  ex:
#         -S1 = "table"
#         -S2 = "tbres"
#         -Output = 3
#         -Explanation : Insert "a" to second position, replace "r" with "l" and delete "s"

#Divide and conquer appraoch:-
#    -S1 = "table"
#    -S2 = "tgable"   (Delete)  -----> f(2,3)
#      
#    -S1="table"
#    -S2="tble"     (Insert) ---------> f(3,2)
#
#    -S1="table"
#    -S2="tcble"   (Replace)  ---------->f()

#Algorithm
#   FindMinOperation(s1, s2, index1, index2):
#     If index1 == len(s1)
#         return len(s2)- index2
#
#     If index2 == len(s2)
#          return len(s1)-index1
#      If s1[index1] == s2[index2]
#          return findMinOperation(s1,s2, index+1, index2+1)
#     Else
#        deleteOp= 1 + findMinOperation(s1, s2, index1, index2+1)
#        insertOp= 1+ findMinOperation(s1,s2, index1+1,  index2)
#        replaceOp=1+ findMinOperation(s1, s2, index1+1, index2+1)
#       return min(deleteOp, insertOp, replaceOp)


def findMinOperation(s1, s2, index1, index2):
    if index1 == len(s1):
        return len(s2)-index2
    if index2==len(s2):
        return len(s1)- index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1+1, index2+1)
    else:
        deleteOp= 1 + findMinOperation(s1, s2, index1, index2+1)
        insertOp= 1+ findMinOperation(s1, s2, index1+1, index2)
        replaceOp= 1+ findMinOperation(s1,s2, index1+1, index2+1)
        return min(deleteOp, insertOp, replaceOp)

print(findMinOperation("table", "tbrles", 0, 0))          