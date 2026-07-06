#The Longes Palindromic Subssequence (LPS)
# -Problem Statement:
#   - S is a given String
#   - Find the longest palindromic subsequence (LPS)
#   - Subsequence : a sequence that can ne driven from another sequence by deleting some elements without changing the order of them.
#   - Palindrome is a string that reads the same backward as well as forward.
#
#   EX: MADAM (Form both side we read MADAM )
# 
# ex:1
#  -s= "ELRMENMET"
#  -Output = 5
#  -LPS = "EMEME"
# ex:2
#    -s ="AMEEWMEA"
#    -oUTPUT = 6
#    - LPS: "AMEEMA"
#
# -Subproblem:-
#    option1 = 2 + f(2,8)     --Both elements are true 
#    option2 = 0 + f(1,8)
#    option3 = o +f(2,9) 
#  max(op1, op2, op3)
#
# Algorithms:-
#     findLPS(S, startIndex, endIndex):
#         If startIndex > endIndex
#             return 0
#         If s1[startIndex]  == s2[endIndex]
#           return 2 + findLPS(S, startindex+1, endIndex+1)
#     
#         Else:
#              op1 = findLPS(S, startIndex, endIndex+1)
#              op2 = findLPS(S, startIndex+1, endIndex)
#                return max(op1,op2)


def findLPS(S, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    elif startIndex == endIndex:
        return 1
    elif S[startIndex] == S[endIndex]:
        return 2+ findLPS(S, startIndex+1, endIndex-1)
    else:
        op1 = findLPS(S, startIndex, endIndex-1)
        op2 = findLPS(S, startIndex+1, endIndex)
        return max(op1,op2)
print(findLPS("ELRMENMET", 0,8))