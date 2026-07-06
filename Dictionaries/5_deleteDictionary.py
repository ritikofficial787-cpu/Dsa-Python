# Delete an element from a dictionary
#1. pop(key) — Remove a Specific Item
#Use pop() when you know the exact key of the item you want to get rid of. It deletes that item and gives you back its value.

mydict={'name':'ritik', 'age':20, 'address':'rajkot'}
print(mydict)

print(mydict.pop('name'))
print(mydict)

#2. popitem() — Remove the Last Item
#You don't pass any keys into popitem(). It automatically removes the very last item that was added to the dictionary and gives you back both the key and the value as a pair (a tuple)

print(mydict.popitem)
print(mydict)

#3. Clear(): It delete all pairs of dictionary
mydict.clear()
print(mydict)


#4. del(): we can delete any pairs of dictinary and it can delete entire dictionary
#del mydict['age']
#print(mydict)

del mydict
