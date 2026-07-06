def fibonaaci(n):
    assert n>=0 and int(n) ==n, 'Fibonacci number must be positive integer only!'    
    if n in[0,1]:
        return n
    else:
     return fibonaaci(n-1) + fibonaaci(n-2)

print(fibonaaci(7.7))