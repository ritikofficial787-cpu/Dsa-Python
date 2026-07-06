#Searching for an element in a list

mylist=[1,2,3,4,5,6,7,8]
#if 2 in mylist:
 #   print(mylist.index(2))
#else:    print("Element is not present in the list")

def searchinlist(list,value):
    for i in list:
       if  i == value:
           return f' The value is exist at index of  {list.index(value)}'
    return 'The value not exist'

print(searchinlist(mylist,5))
