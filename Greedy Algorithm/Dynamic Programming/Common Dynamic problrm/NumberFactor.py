def numberFactorTD(n, tempDict):
    """
    Top Down (Memoization) approach to find the number of ways
    to express N as a sum of 1, 3 and 4.

    Parameters:
        n        -> the number for which we want NF(n)
        tempDict -> dictionary used as memo/cache to store
                    already computed results (avoids recomputation)
    """

    # Base cases: directly return known results
    # NF(0) = 1, NF(1) = 1, NF(2) = 1  (treated as base hits here)
    if n in (0, 1, 2):
        return 1

    # NF(3) = 2 (another base case)
    elif n == 3:
        return 2

    else:
        # Recursive case: only compute if not already memoized
        if n not in tempDict:

            # Recurrence relation: NF(n) = NF(n-1) + NF(n-3) + NF(n-4)
            subP1 = numberFactorTD(n-1, tempDict)   # ways using last step = 1
            subP2 = numberFactorTD(n-3, tempDict)   # ways using last step = 3
            subP3 = numberFactorTD(n-4, tempDict)   # ways using last step = 4

            # Store the computed result in the dictionary (memoize)
            tempDict[n] = subP1 + subP2 + subP3

        # Return the cached/memoized value for n
        return tempDict[n]
    
# Bottom Up

def numberFactorBU(n):
    # Base cases: NF(0)=1, NF(1)=1, NF(2)=1, NF(3)=2
    tempArr = [1, 1, 1, 2]

    # Build up the table iteratively using the recurrence:
    # NF(i) = NF(i-1) + NF(i-3) + NF(i-4)
    for i in range(4, n+1):
        tempArr.append(tempArr[i-1] + tempArr[i-3] + tempArr[i-4])

    return tempArr[n]  # (missing return in original — add if needed)


print(numberFactorTD(5, {}))


# Driver code
# Calling with an empty dictionary {} as the initial memo storage
print(numberFactorTD(5, {}))