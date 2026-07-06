#Insertion Sort:-
 # - Divide the given array into two part
 # - Take first element from unsorted araay and find its correct position in sorted array.
 # - Repeat until unsorted array is empty
# Insertion Sort - Explanation
#
# 1. Start from the second element (index 1) - treat the first element
#    as a "sorted" portion of size 1.
# 2. Take the current element and call it the "key".
# 3. Compare the key with elements before it (to its left).
# 4. Shift any elements bigger than the key one position to the right.
# 5. Insert the key into the gap left behind, where it belongs.
# 6. Move to the next element and repeat steps 2-5.
# 7. Continue until you reach the end of the list - now it's fully sorted.
#
# Time Complexity: O(n^2) worst/average case, O(n) best case (already sorted)
# Space Complexity: O(1) - sorts in place, no extra memory needed
# Stable - does not change the relative order of equal elements
#
# Example walkthrough:
# List: [5, 2, 8, 1, 9]
#
# Start: [5 | 2, 8, 1, 9]   (5 is the sorted portion)
#
# Step 1: key = 2
#   Compare 2 with 5 -> 5 is bigger, shift 5 right
#   Insert 2 before 5
#   List: [2, 5 | 8, 1, 9]
#
# Step 2: key = 8
#   Compare 8 with 5 -> 5 is smaller, no shift needed
#   Insert 8 right where it is
#   List: [2, 5, 8 | 1, 9]
#
# Step 3: key = 1
#   Compare 1 with 8 -> shift 8 right
#   Compare 1 with 5 -> shift 5 right
#   Compare 1 with 2 -> shift 2 right
#   Insert 1 at the very front
#   List: [1, 2, 5, 8 | 9]
#
# Step 4: key = 9
#   Compare 9 with 8 -> 8 is smaller, no shift needed
#   Insert 9 right where it is
#   List: [1, 2, 5, 8, 9]
#
# Sorted!


def InsertionSort(customlist):
    for i in range(1, len(customlist)):
        key = customlist[i]
        j = i-1
        while j>=0 and key <customlist[j]:
            customlist[j+1]=customlist[j]
            
        customlist[j+1] = key
        
    print(customlist)
cList=[2,1,4,5,3,9,8,7,6]
InsertionSort(cList)
