my_list=[1,2,3,4,5,6,7,8,9,10]
#print(my_list)
print(len(my_list)) #10 because the list has 10 elements

#print(my_list[1]) #IndexError: list index out of range because the index starts from 0 and the last index is 9
#print('2' in my_list) #True because 2 is present in the list
#print('11' in my_list) #False because 11 is not present in the list


#print("*******Accessing Element using Index**********")
#def accessingelement(list,index):
#    if index < len(list):
#        return list[index]
#    else:
#        return "Index out of range"
#print(accessingelement(my_list,5))

#print("******* Traversal  using for loop**********")

def traverseList(list):
    for i in my_list: 
        print(i)
traverseList(my_list)