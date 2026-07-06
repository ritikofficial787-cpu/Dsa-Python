"""
# Heap Sort:-
  -Step1 : Insert data to Binary Heap Tree
  -Step2 : Extract data from Binary Heap
  -It is best suited with array, it does not work with Linked list

  -Step1: Insert data to Binary Heap Tree
  -Step2: Extract data from Binary Heap 

  /**
 * Heap Sort Algorithm
 * ---------------------
 * A comparison-based sorting algorithm that uses a
 * "binary heap" data structure (a tree-like structure
 * stored in an array).
 *
 * How it works:
 * 1. BUILD MAX HEAP - Rearrange the array into a "max heap",
 *                      where every parent node is greater
 *                      than or equal to its children. This
 *                      means the largest element is always
 *                      at the root (index 0).
 * 2. SWAP & SHRINK   - Swap the root (largest element) with
 *                      the last element in the heap. This
 *                      puts the largest value in its correct
 *                      final position at the end of the array.
 * 3. RE-HEAPIFY      - Reduce the heap size by 1 (ignoring the
 *                      sorted element) and "heapify" again so
 *                      the next largest element rises to the root.
 * 4. REPEAT          - Keep swapping the root with the last
 *                      unsorted element and re-heapifying until
 *                      only one element remains.
 *
 * Example:
 * [38, 27, 43, 3, 9, 82, 10]
 *   -> build max heap: [82, 38, 43, 3, 9, 27, 10]
 *   -> swap root(82) with last(10): [10, 38, 43, 3, 9, 27, 82]
 *      -> heapify remaining [10, 38, 43, 3, 9, 27]: [43, 38, 27, 3, 9, 10]
 *   -> swap root(43) with last(10): [10, 38, 27, 3, 9, 43, 82]
 *      -> heapify remaining [10, 38, 27, 3, 9]: [38, 10, 27, 3, 9]
 *   -> ... continues until fully sorted
 *   -> result: [3, 9, 10, 27, 38, 43, 82]
 *
 * Time Complexity:  O(n log n) - in all cases (best, average, worst)
 * Space Complexity: O(1)       - sorts in-place, no extra arrays needed
 *
 * Good for: situations needing guaranteed O(n log n) with O(1) space
 * Not ideal for: when stability is required (heap sort is NOT stable)
 */
"""

def heapify(customlist, n,i):
    smallest = i
    l =2*i+1
    r=2*1+2
    if l<n and customlist[l]<customlist(smallest):
        smallest=l
    
    if r<n and customlist[r] < customlist[smallest]:
        smallest=r
    
    if smallest !=i:
        customlist[i], customlist[smallest] = customlist[smallest], customlist[i]
        heapify(customlist, n, smallest)

def heapSort(customlist):
    n = len(customlist)
    for i in range(int(n/2)-1, -1, -1):
        heapify(customlist,n,i)

    for i in range(n-1,0,-1):
        customlist[i], customlist[0] = customlist[0], customlist[i]

    customlist.reversed()


clist=[2,1,7,6,5,3,4,9,8]
heapSort(clist)