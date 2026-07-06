#How to find GCD (Greatest common Divisior) of two numbers using recursion?
#Step -1 Recursive case- the flow
# Gcd is the largest positive integer  that divides the numbers without a remainder
# gcd(8,12)=4
# 8=2*2*2  common number in between is(2)
# 12=2*2*3
# Euclidean algorithm(to find gcd):
#gcd(48,18)
#step-1 48/18 = 2 remainder 12
#step-2 18/12=1 remainder 5
#step-3 12/6=2 remainder=0 gcd is 6
#gcd(a,0)=a
#gcd(a,b)=gcd(b,a mod b)
#gcd not be to -ve so convert into +ve number because gcd of +e number is equal to -ve number


def gcd(a,b):
    assert int(a)== a and int(b)==b, 'The number must be intger only!'
    if a <0:
       a=-1*a
    if b<0:
       b = -1*b
    if b==0:
        return a
    else:
     return gcd(b, a%b)
print(gcd(48,18))