#Check balanced
#Implements a function to check if a binary tree is balanced.For the purposes of this question, a balanced tree is
# defined to be a tree such that the heights of the two subtrees of any node never differ by more than one,

# The Binary Tree is Balnced if:
# -The right subtree is balanced
# -The left subtree is balanced.
# -The diffrence between the heights of the left subtree and the right subtree is atmost 1

#Balanced Tree
def isBalancedHelper(rootnode):
    if rootnode is None:
        return 0
    leftHeight = isBalancedHelper(rootnode.left)
    if leftHeight == -1:
        return -1
    rightHeight = isBalancedHelper(rootnode.right)
    if rightHeight ==-1:
        return -1
    if abs(leftHeight-rightHeight)> 1:
        return -1
    return max(leftHeight, rightHeight) +1

def isBalnced(rootnode):
    return isBalancedHelper(rootnode) >-1

class Node():
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

N1 =Node("N1")
N2 =Node("N2")
N3 =Node("N3")
N4 =Node("N4")
N5 =Node("N5")
N6 =Node("N6")
N1.left=N2
N1.right=N3
N2.left=N4
N2.right=N5
N3.right=N6

print(isBalnced(N1))