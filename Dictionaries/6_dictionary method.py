mydict={'name':'Ritik', 'age':20, 'address': 'Rajkot', 'education':'Higher Schooling'}
#mydict.clear()
print(mydict)

# Copy(): copy method is used to create another dictionary with same key value and pairs reference to copied method.
new_dict=mydict.copy()
print(new_dict)

#fromkeys(): The fromkeys() method is a quick way to create a brand-new dictionary from scratch when you already know what keys you want, and you want all of them to start with the same initial value.

neo_dict={}.fromkeys([1,2,3],0)
print(neo_dict)

#get(): get() method is used to retrive a specific key if key exist in dictionary
#syntax: dictionary.get(key,value)
print(mydict.get('age',21))


#items(): In simple terms, items() gives you a list-like view of everything inside your dictionary, where each key-value pair is bundled together into a neat little package called a tuple.

print(mydict.items())

#keys(): gives a list of all keys in dictionary
print(mydict.keys())

#popitem(): The "Remove the Last Item"

print(mydict.popitem())
print(mydict)

#setdefault(): setdefault() is a defensive tool. It lets you add a key with a starting value, but only if that key doesn't already exist.
#syntax: dictionary.setdefault(key,default_value)
print(mydict.setdefault('name1','added'))
print(mydict)

#update():The update() method is used to merge or add multiple items into a dictionary all at once.
# this method update a element from a another dictionary element, update method  add s element if key is not in dictioanry if key in dictioanry thn update it .
#Syntax: dictionar().update(other_dicitonary)

dict= {'a':1, 'b':2, 'c':3}
mydict.update(dict)
print(mydict)