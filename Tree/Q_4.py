#Validate BST
#Implement a function to check if a binary tree is a Binary Search Tree.

#The Binary Tree is Binary Search Tree if:
# - The left subtree of a node contains only nodes with keys less than the node's key
# -The right subtree of a node contains only nodes with keys grater than the node's key.
# -These conditions are applicable for both left and right subtree.

class TreeNode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right= None

def helper(node, minValue=float('-inf'), maxValue=float('inf')):
    if not node:
        return True
    val = node.val
    if val <=minValue or val>=maxValue:
        return False
    
    if not helper(node.right, val, maxValue):
        return False
    
    if not helper(node.left, minValue, val):
        return False
    
    return True

def isValidBST(root):
    return helper(root)


root1= TreeNode(2)
root1.left=TreeNode(1)
root1.right=TreeNode(4)

print(isValidBST(root1))


root2= TreeNode(4)
root2.left=TreeNode(1)
root2.right=TreeNode(3)

print(isValidBST(root2))
