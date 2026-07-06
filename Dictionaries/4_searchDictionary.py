#Searching in dictionary

my_dict={'name':'eddy', 'age':26, 'address':'London'}

def searchdict(dict,value):
    for key in dict:
     if dict[key]==value:
        return key,value
    return 'Value does not exist'

print(searchdict(my_dict,26))
