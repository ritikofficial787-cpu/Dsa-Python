"""
* Merge Sort:-
  /**
 * Merge Sort Algorithm
 * ---------------------
 * A divide-and-conquer sorting algorithm.
 *
 * How it works:
 * 1. DIVIDE  - Split the array into two halves recursively
 *              until each sub-array has only one element.
 * 2. CONQUER - Each single-element array is trivially "sorted".
 * 3. MERGE   - Combine pairs of sorted sub-arrays back together
 *              by comparing front elements and picking the
 *              smaller one first, until everything is merged
 *              into one fully sorted array.
 *
 * Example:
 * [38, 27, 43, 3] 
 *   -> split into [38, 27] and [43, 3]
 *   -> split further into [38], [27], [43], [3]
 *   -> merge: [27, 38] and [3, 43]
 *   -> merge: [3, 27, 38, 43]
 *
 * Time Complexity:  O(n log n) - always, regardless of input order
 * Space Complexity: O(n)       - needs extra space for merging
 *
 * Good for: large datasets, stable sorting needs, linked lists
 * Not ideal for: small arrays (overhead) or limited memory
 */



"""

def merge(customlist, l, m, r):
    n1 = m -l +1  #Divide into two subarray(n1,n2)
    n2 = r -m

    L =[0] * (n1)
    R =[0] * (n2)

    for i in range(0, n1):
        L[i]=customlist[l+i]

    for j in range(0, n2):
        L[j]=customlist[m+1+j]

    i=0  #Initial indx of first subarray
    j=0  #Intial index of second subarray
    k=1  #Initail index of Merge subarray

    while i<n1 and j<n2:
        if L[i] <= R[j]:
            customlist(k) =L[i]
            i+=1
        else:
            customlist[k] = R[j]
            j+=1
        k+=1
    while i <n1:
        customlist[k] =L[i]
        i+=1
        k+=1
    while j<n2:
        customlist[k]=L[i]
        j+=1
        k+=1 


def mergeSort(customlist, l, r):
    if l<r:
        m=(l+(r-1))//2
        mergeSort(customlist, l, m)
        mergeSort(customlist, m+1, r)

        merge(customlist, l, m, r)

Clist=[2,1,7,3,6,4,5,9,8]
print(mergeSort(Clist,0, 8))