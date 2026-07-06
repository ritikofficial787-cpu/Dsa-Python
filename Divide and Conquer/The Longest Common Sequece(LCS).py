# The longest Common Subssequenece(LCS):
#  Problem Statement:
#     - S1 and S2 are given stringd
#     - Find the longest common subsequence between BOTH strings
#     -Subsequence: A sequence that can be driven from another sequence by deleting some elements without changing the order of them.

#  ABCDE --- ACE   ADE  ACB
# EX:-
#     -S1= "elephant"
#     -S2= "erepat"
#     -Output = 5
#     -Longest String : "eepat"
#  -Subproblem:
#   Matching- option1 = 1 + f(2,8: 2,7)   (8 and 7 is len of string)
#   NotMatching- option2= 0 + f(3,8: 2,7)
#    option 3 = 0 +f(2,8:3,7)
# Maximum(option1, option2, option3)

#Algorithm:-
#  findCLS(s1, s2, index1, index2):
#     If index1 == len(s1)  or index2 == len(s2)
#            return o
#     If s1[index] ==s2[index]
#          return 1+ findCLS(s1,s2, index1+1, inde2+1)
#   
#     Else:
#      op1= findCLS(s1,s2,index1, index2+1)
#      op2= findCLS(s1,s2, index+1, index2)
#      return max(op1,op2)
#

def findLCS(s1,s2,index1,index2):
    if index1== len(s1) or index2 == len(s2):
        return 0 
    if s1[index1] == s2[index2]:
        return 1 + findLCS(s1,s2,index1+1, index2+1)
    else:
        op1=findLCS(s1,s2, index1, index2+1)
        op2 =findLCS(s1,s2, index1+1, index2)
        return max(op1, op2)
    
print(findLCS("elephant", "eretpat", 0,0))