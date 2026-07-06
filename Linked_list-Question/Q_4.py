#Sum Lists

#You have two numbers represnted by a linked list, where each node contains a single digit.
#The digits are stored in reverse oreder, such that the 1's digit is at the head of the list.Write a
#function that adds two numbrs and returns the sum as a likned list.

 # list1 = 7 -> 1 -> 6        617
# list2 = 5 -> 9 -> 2   -->  295  -->  617 + 295 = 912  -->  sumList = 2 -> 1 -> 9
#
#   617       7 + 5 = 12
# + 295       1 + 9 + 1 = 11
# -----       6 + 2 + 1 = 9
#   912
#
# [7] -> [1] -> [6]
#                         [2] -> [1] -> [9]
# [5] -> [9] -> [2]
 

from LinkedList import LinkedList

def sumList(llA, llB):
    n1=llA.head
    n2=llB.head
    carry=0
    ll=LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result+=n1.value
            n1=n1.next
        if n2:
            result+=n2.value
            n2=n2.next
        ll.add(int(result%10))
        carry=result/10
    return ll

llA=LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)


llB =LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)
print(llA)
print(llB)
print(sumList(llA, llB))
 