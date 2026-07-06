#Bubble Sort:-
 #-Bubblee Sort is also referred as Sinking Sort.
 #-We repeadetly compare each pair of adjacent items and swap them if they are in the wrong order
# ============================================
# BUBBLE SORT - Explanation (no code logic)
# ============================================
#
# Example list: 5, 1, 4, 2, 8
#
# Bubble sort compares two neighboring numbers
# at a time, and swaps them if they are in the
# wrong order. We keep sweeping left to right
# until nothing needs swapping anymore.
#
# PASS 1:
#   Compare 5 and 1 -> 5 > 1, swap   -> 1, 5, 4, 2, 8
#   Compare 5 and 4 -> 5 > 4, swap   -> 1, 4, 5, 2, 8
#   Compare 5 and 2 -> 5 > 2, swap   -> 1, 4, 2, 5, 8
#   Compare 5 and 8 -> in order      -> 1, 4, 2, 5, 8
#   (Biggest number, 8, has now "bubbled" to the end)
#
# PASS 2:
#   Compare 1 and 4 -> in order
#   Compare 4 and 2 -> swap          -> 1, 2, 4, 5, 8
#   Compare 4 and 5 -> in order
#   (8 is already placed, skip it)
#
# PASS 3:
#   Compare 1 and 2 -> in order
#   Compare 2 and 4 -> in order
#   No swaps this pass -> list is sorted!
#
# FINAL RESULT: 1, 2, 4, 5, 8
#
# Idea: each pass pushes the next-largest value
# into its correct spot, like bubbles rising up.
# ============================================

def bubbleSort(customlist):
    for i in range(len(customlist)-1):
        for j in range(len(customlist)-i-1):
            if customlist[j] > customlist[j+1]:
                customlist[j], customlist[j+1] = customlist[j+1], customlist[j]
        print(customlist)

cList = [2,1,7,6,5,3,4,9,8]
bubbleSort(cList)