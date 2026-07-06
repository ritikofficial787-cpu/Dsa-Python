# Operations and built in functions

my_dict= {'one':'uno', 'two':'dos', 'three': 'tres', 'four':'cuarto'}
print(my_dict)

# in operator: tells that is keys in dictioanry is exist or not

print('one' in my_dict)
print('uno' in my_dict)
print('uno' in my_dict.values()) # TC------------------------------>o(1)

# for operator: we can visit all key
for key in my_dict:
    print(key,dict[key])

# all method :return through when all elment in  the given iterables are true if not it return false
# syntax: dict.all()
# ==============================================================================
# TRUTH TABLE REFERENCE: all() FUNCTION BEHAVIOR
# ==============================================================================
# This table shows how Python's built-in all() function evaluates different
# lists, tuples, or sets (iterables) containing True/False values.
#
# Concept Rule: returns True ONLY if EVERY single element is True. 
# ------------------------------------------------------------------------------
#  Cases                                         | Return Value
# ------------------------------------------------------------------------------
#  All values are true                           | TRUE  (e.g., [True, True])
#                                                |
#  All values are false                          | FALSE (e.g., [False, False])
#                                                |
#  One value is true (others are false)          | FALSE (e.g., [True, False])
#                                                |
#  One value is false (others are true)          | FALSE (e.g., [False, True])
#                                                |
#  Empty Iterable                                | TRUE  (e.g., []) *Vacuous truth
# -----------------------------------------------------------------------------

new_dict={1:True, 2:True}
#new_dict={0:False, 1:False} #give output false
print(all(new_dict))
# if all values false return true else for true also and if one of them flase return false and empty variables return true.

#any(): any method return true if any element of collection is true
# ==============================================================================
# TRUTH TABLE REFERENCE: any() FUNCTION BEHAVIOR
# ==============================================================================
# This table shows how Python's built-in any() function evaluates different
# lists, tuples, or sets (iterables) containing True/False values.
#
# Concept Rule: returns True if AT LEAST ONE element is True. Otherwise False.
# ------------------------------------------------------------------------------
#  Cases                                         | Return Value
# ------------------------------------------------------------------------------
#  All values are true                           | TRUE  (e.g., [True, True])
#                                                |
#  All values are false                          | FALSE (e.g., [False, False])
#                                                |
#  One value is true (others are false)          | TRUE  (e.g., [True, False])
#                                                |
#  One value is false (others are true)          | TRUE  (e.g., [False, True])
#                                                |
#  Empty Iterable                                | FALSE (e.g., [])
# ------------------------------------------------------------------------------
Dict={0: True, 1:False, 2:False}
print(any(Dict))

#len method return the number of item in collection
print(len(my_dict))  #it rturn number of pairs

#sorted() metod return soretd fucntion from a iterables
#syntax: sorted(iterable,reverse,key)

ritik_dict={'e':1, 'a':2, 'u':3, 'o':4, 'i':5} #it sort the key not value
print(sorted(ritik_dict))
print(sorted(ritik_dict, reverse=False))