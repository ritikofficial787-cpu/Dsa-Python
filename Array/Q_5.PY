#Permutation 

#def permutation(list1, list2):
    #if sorted(list1) == sorted(list2):
     #   return True
    #    else:
#        return False
#list1 = ['a', 'b', 'c']
#list2 = ['c', 'b', 'a']
#print(permutation(list1, list2))




def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
list1 = ['a', 'b', 'c']
list2 = ['c', 'b', 'a']
print(permutation(list1, list2))