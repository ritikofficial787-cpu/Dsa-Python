#Number Factor:-

def numberFactor(n):
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        subproblem1 =numberFactor(n-1)
        subproblem2=numberFactor(n-3)
        subproblem3= numberFactor(n-4)
        return subproblem1+subproblem2+subproblem3
    
print(numberFactor(3))