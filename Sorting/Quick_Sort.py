"""
/**
 * Quick Sort Algorithm
 * ---------------------
 * A divide-and-conquer sorting algorithm.
 * Find pivot number and make sure smaller b=numbers located at the left of pivot and bigger numbers are located at the riight of the pivot.
 * Unlike Merge Sort extra space is not required.
 *
 * How it works:
 * 1. PICK A PIVOT - Choose an element from the array (commonly
 *                    the last, first, or a random element).
 * 2. PARTITION    - Rearrange the array so that elements smaller
 *                    than the pivot go to its left, and elements
 *                    larger go to its right. The pivot is now in
 *                    its correct sorted position.
 * 3. RECURSE      - Apply the same process to the left and right
 *                    sub-arrays (excluding the pivot).
 * 4. BASE CASE    - Sub-arrays with 0 or 1 element are already sorted.

 * Example:
 * [38, 27, 43, 3, 9, 82, 10]   (pivot = 10, last elem)
 *   -> partition: [3, 9] + [10] + [38, 27, 43, 82]
 *   -> recurse on [3, 9] -> [3, 9]
 *   -> recurse on [38, 27, 43, 82] (pivot = 82)
 *      -> [38, 27, 43] + [82]
 *      -> recurse on [38, 27, 43] (pivot = 43)
 *         -> [38, 27] + [43]
 *         -> recurse on [38, 27] (pivot = 27)
 *            -> [27] + [38]
 *   -> result: [3, 9, 10, 27, 38, 43, 82]
 *
 * Time Complexity:  O(n log n) average case
 *
 * Time Complexity:  O(n log n) average case
 *                    O(n^2) worst case (e.g. already sorted array
 *                    with poor pivot choice)
 * Space Complexity: O(log n) - in-place, only recursion stack used
 *
 * Good for: large datasets, when low memory overhead matters
 * Not ideal for: data with many duplicates or already-sorted data
 *                (without randomized pivot selection)
 
 * When to use Quick Sort?
 *  -When average expected time iso(NlogN)

 *When to avoid Quick Sort?

 *  -When space is a concern
 *  -When you need stable sort
 
 
 */
"""


def Partiton(customlist, low, high)  : #Low(first index) High(Last Index)
    i=low-1
    pivot=customlist[high]
    for j in range(low,high):
        if customlist[j] <=pivot:
            i+=1
            customlist[i], customlist[j] =customlist[j], customlist[i]
    customlist[i+1], customlist[high] = customlist[high], customlist[i+1]
    return (i+1)


def quickSort(customlist, low,high):
    if low<high:
        pi=Partiton(customlist,low,high)   #pi is partition index
        quickSort(customlist, low, pi-1)
        quickSort(customlist, pi+1, high)

clist=[2,3,5,6,7,9,8,1,4]
quickSort(clist,0,8)
print(clist)