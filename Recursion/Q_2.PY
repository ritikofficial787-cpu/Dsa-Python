#How to calculate power of a number using recursion?
#Step 1: Recursive case -the flow
#X^n=x*x*X**X...(n times)..*x
#2^4 = 2*2*2*2*
#x^a * x^b =x^a+b
#x^3 + x^4 = x^3+4
#x^n =x*x^n-1

#step2: Base case-the stopping criterion
#0 and 1

#.step3: Unintentional case - the constraint
#-power(-2) ??
#-power(1.5) ??

def power(base,exp):
    assert exp>=0  and int(exp)== exp, 'The exponent must be positve integer '
    if exp==0:
        return 1
    if exp ==1:
       return base
    else:
     return base * power(base, exp-1)
print(power(2,-1))
