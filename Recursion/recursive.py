#import sys
#sys.setrecursionlimit(100) #This is used to increase the recursion limit. By default, Python has a recursion limit of 1000. If you try to exceed this limit, you will get a RecursionError.

def factorial(n):
    assert n>=0 and int(n) ==n, 'The number must be positive integer only!'
    if n in [0,1]:  #Base case(without base case the computer runs out of allocated memory for this pile. This is known as a Stack Overflow. Python prevents your entire computer from crashing by throwing the RecursionError)
        return 1 
    print(n)
    return n* factorial(n-1)

print(f"Factorial of 15 is: {factorial(5.6)}")


