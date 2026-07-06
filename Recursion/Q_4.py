#How to convert a number from decimal to binary using recursion
#-step:1 Recursive case-the flow
#. Divide the number by 2
#. Get the integer quotient for next iteration
#. Get the remainder for the binary digit
#. Repeat the steps until the quoteint is equal to to 0
#ex:
#13 to binary(1010)
# Division by   Quoteint  Remainder
# 13/2            6        0
# 6/2             3        1
# 3/2             1        0
# 1/2             0        1
# Main point is  if combine last number (1*10+0=10) then other ABOVE(10*10+1=101) then(101*10+0=1010)
#f(n)= n mod 2 +  10 *f(n/2)

def decimalToBinary(n):
    assert int(n) == n, 'The parameter must be intger only'
    if n==0:
       return 0
       
    else:

     return n%2 +10 * decimalToBinary(n//2)
print(decimalToBinary(54))