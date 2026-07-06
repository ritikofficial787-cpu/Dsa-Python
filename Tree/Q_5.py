# Successor:-
# Write an algorithm to find the next node (i.e in- order successor) of given node in a binary search tree. You may
# assume that each node has a link to its parent.
#  -If right subtree of node is Not None, then successor lies in right subtree.
# -If right subtree of node is None, then successor is one of the ancestors.

class Node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None

def minValue(node):
    current = node
    while (current is not None):
        if current.left is None:
            break
        current= current.left
    return current

def inOrderSuccessor(root, n): #n is current node
    if n.right is not None:
        return minValue(n.right)
    
    p =n.parent  #p=Parent node
    while p is not None:
        if  n !=p.right:
            break
        n = p 
        p=p.parent
    return p


#Insert value

def insert(node, data):
    if node is None:
        return Node(data)
    
    else:
        if data <= node.data:
            temp = insert(node.left, data)
            node.left=temp
            temp.parent=node

        else:
            temp = insert(node.right,  data)
            node.right = temp
            temp.parent=node
        return node
    
root = None
root = insert(root, 4)
root = insert(root, 2)
root= insert(root, 8)
root= insert(root, 1)
root= insert(root, 3)
root= insert(root, 5)
root = insert(root, 9)

temp = root.left.right #3

successor = inOrderSuccessor(root, temp)

if successor is not None:
    print("Inorder Successor of %d is %d" %(temp.data, successor.data))
else:
    print("Inorder successor does not exist")