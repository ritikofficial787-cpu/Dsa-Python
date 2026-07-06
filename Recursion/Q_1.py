# How to find the sum of digits of a positive integer using recursion?
# step -1 : Recursive case- the flow
# imagine 10  --> 10/10 =1 and remainder =0
# 54  --->54/10 =5 and reamider = 4
# 112/10=11 and remainder=2
# 11/10 = 1 and remainder=1

#f(n)=n%10 + f(n/10)

#step-2 base case- the stoping criterion
n=0



def sumofnum(n):
    assert n>=0 and int(n)==n , 'The number has to be a positive integers only'
    if n==0:
        return 0
    else:
     return  (int(n%10)) + sumofnum(int(n/10))

x=sumofnum(10000)
print(x)