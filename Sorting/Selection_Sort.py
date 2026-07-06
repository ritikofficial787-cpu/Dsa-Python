#Selection Sort:-
 #-In case of Selection sort we repeatedly find the minimum element and
 #  move it to the sorted part of array to make unsorted part sorted.
# Selection Sort - Explanation
#
# 1. Start with the first element of the list, assume it's the minimum.
# 2. Loop through the rest of the unsorted part to find the actual smallest value.
# 3. Once found, swap it with the first element.
# 4. Move the boundary of the "sorted" section one step forward.
# 5. Repeat steps 1-4 for the remaining unsorted part of the list.
# 6. Continue until the entire list is sorted.
#
# Time Complexity: O(n^2) - best, average, and worst case
# Space Complexity: O(1) - sorts in place, no extra memory needed
# Not stable - can change the relative order of equal elements
#
# Example walkthrough:
# List: [5, 2, 8, 1, 9]
# Pass 1: min in [5,2,8,1,9] is 1 -> swap with index 0 -> [1, 2, 8, 5, 9]
# Pass 2: min in [2,8,5,9]   is 2 -> already in place   -> [1, 2, 8, 5, 9]
# Pass 3: min in [8,5,9]     is 5 -> swap with index 2  -> [1, 2, 5, 8, 9]
# Pass 4: min in [8,9]       is 8 -> already in place   -> [1, 2, 5, 8, 9]
# Sorted!

def SelectionSort(customList):
    for i in range(len(customList)):
        min_index=i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
              min_index=j
        customList[i], customList[min_index]=customList[min_index], customList[i]
    print(customList)
Clist=[2,1,4,5,3,8,7,9,6]
SelectionSort(Clist)