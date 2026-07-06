# How to search for an element in Tuple?


newtuple=('a','b','c','d')
#print('a' in newtuple) 

def searchelement(tuple,value):
    for i in tuple:
        if i == value:
            return tuple.index(i)
    return 'Value does not exist'
print(searchelement(newtuple,'2'))