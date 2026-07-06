# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. 
# Avoid storing additional nodes in a data structure. Note: This is not necessarily a binary search tree.

def findNodeInTree(node, rootNode):
    if rootNode is None:
        return False
    
    if node == rootNode:
        return True
    
    # FIX: Properly search both left AND right subtrees independently
    return findNodeInTree(node, rootNode.left) or findNodeInTree(node, rootNode.right)


def findFirstCommonAncestor(firstNode, secondNode, root):
    # FIX: Base case to prevent 'NoneType' AttributeError
    if root is None:
        return None
        
    # If either target node is the current root, the root itself is the lowest common ancestor
    if root == firstNode or root == secondNode:
        return root

    firstNodeOnLeft = findNodeInTree(firstNode, root.left)
    secondNodeOnLeft = findNodeInTree(secondNode, root.right) # Checking if second node is on the right branch instead

    # If one is on the left side and the other is on the right side
    if firstNodeOnLeft != secondNodeOnLeft: 
        return root
    else:
        # If both are on the left side, go left
        if firstNodeOnLeft:
            return findFirstCommonAncestor(firstNode, secondNode, root.left)
        # If both are on the right side, go right
        else:
            return findFirstCommonAncestor(firstNode, secondNode, root.right)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Tree setup
node54 = Node(54)
node88 = Node(88, node54)
node35 = Node(35)
node22 = Node(22, node35, node88)
node33 = Node(33)
node90 = Node(90, None, node33)
node95 = Node(95)
node99 = Node(99, node90, node95)
node44 = Node(44, node22, node99)
node77 = Node(77)
rootNode = Node(55, node44, node77)

commonAncestor = findFirstCommonAncestor(node88, node33, rootNode)
print(commonAncestor.value) # Expected Output: 44