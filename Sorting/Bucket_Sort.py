#Bucket Sort:-
#   -Create buckets and distribute elements of array into buckets.
#   -Sort buckets individually.
#   -Merge buckets after sortion
#Number of buckets = round(sqrt(number of elemets))
#round(sqrt(9))=3
#Apppropriate bucket = cell(Value* number of buckets/ max value)
#cell(2*3/9)=1 means it store in bucket 1
#Then sort all buckets (using any sorting algorithm)

# Bucket Sort - Quick Overview
#
# [5,3,4,7,2,8,6,9,1] -> distribute into buckets -> sort each bucket -> combine
#
# Bucket 1: [3,2,1] -> sorted -> [1,2,3]
# Bucket 2: [5,4,6] -> sorted -> [4,5,6]
# Bucket 3: [7,8,9] -> sorted -> [7,8,9]
#
# Combine: [1,2,3] + [4,5,6] + [7,8,9] = [1,2,3,4,5,6,7,8,9]
#
# Time: O(n+k) avg, O(n^2) worst | Space: O(n+k)

import math
def InsertionSort(customlist):
    for i in range(1, len(customlist)):
        key = customlist[i]
        j = i-1
        while j>=0 and key <customlist[j]:
            customlist[j+1]=customlist[j]
            j-=1
        customlist[j+1] = key
        
    return customlist


def BucketSort(customlist):
    numberofBuckets= round(math.sqrt(len(customlist)))
    maxValue = max(customlist)
    arr = []

    for i in range(numberofBuckets):
        arr.append([])
    for j in customlist:
        index_b=math.ceil(j*numberofBuckets/maxValue)
        arr[index_b-1].append(j)
    for i in range(numberofBuckets):
        arr[i]=InsertionSort(arr[i])

    k=0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customlist[k]=arr[i][j]
            k+=1
    return customlist    





cList=[1,4,5,6,2,3,9,7,8]
print(BucketSort(cList))