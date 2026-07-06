#Deltetion / Slice

my_list=[1,2,3,4,5,6,7,8]
print(my_list[2:5]) #3,4,5 because the index starts from 0 and the last index is 7
print(my_list[2:8]) #3,4,5,6,7,8

print(my_list[0:8:2]) #1,3,5,7 because the index starts from 0 and the last index is 7

my_list[0:2]=['x','y'] #it updates the list from index 0 to 1 with the new values 'x' and 'y'
print(my_list) #['x','y',3,4,5,6,7,8] because the index starts from 0 and the last index is 7

#deletion
#List method fot deletion
#- del list[index] : it deletes the element at the specified index
#pop() : it deletes the last element of the list and returns it
#remove() : it deletes the first occurrence of the specified value
#delete(): it deletes the entire list

my_list.pop(1)  # Use parentheses instead of square brackets
print(my_list)  #['x', 3, 4, 5, 6, 7, 8] because the index starts from 0 and the last index is 6
my_list.remove(5)  # Remove the value 5 from the list
print(my_list)  #['x', 3, 4, 6,

#my_list.clear()  # Clear all elements from the list
#print(my_list)  #[] because the list is now empty

del my_list[2:4]  # Delete the elements at indices 2 and 3
print(my_list)  # This will raise a NameError because the list has been deleted

#my_list.delete()  # Delete the entire list
print(my_list)  # This will raise a NameError because the list has been deleted