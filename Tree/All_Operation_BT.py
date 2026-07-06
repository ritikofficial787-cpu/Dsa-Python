#Create Binary Tree using Linked List
#Operation:-
 #Creation of Tree
 #Insertion of a node
 #Deletion of a node
 #Search for value
 #Trverse all nodes
 #Deletion of tree
#newtree=Tree(
from Queue.QueueLinklist import QueueLinklist as qe

class Tree:
    def __init__(self, data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
newBT=Tree("Drinks")
leftchild=Tree("Hot")
tea=Tree("Tea")
coffee=Tree("Coffee")
leftchild.leftchild=tea
leftchild.leftchild=coffee
newBT.leftchild=leftchild
rightchild=Tree("Cold")
cola=Tree("Cola")
mango=Tree("Mango")
fanta=Tree("Fanta")
rightchild.rightchild=cola
rightchild.rightchild=mango
rightchild.rightchild=fanta
newBT.rightchild=rightchild

newBT.leftchild=leftchild
newBT.rightchild=rightchild


#TraversL OF BINARY TREE:-
#1. Depth first search
#   -Preorder traversal
#   -Inorder traversal
#   -Post order traversal
#2. Breadth first Search
#  -Level order traversal

#Pre-order Traversal

#PreOrder Traversal of Binary Tree
#
#                  N1
#                 /  \
#               N2     N3
#              /  \   /  \
#            N4    N5 N6   N7
#           /  \
#         N9    N10

#PreOrder Traversal:  N1 → N2 → N4 → N9 → N10 → N5 → N3 → N6 → N7

#Note: Root → Left Subtree → Right Subtree


def preorderTraversal(rootNode):
    if not rootNode:
        return 
    else:
        print(rootNode.data)
        preorderTraversal(rootNode.leftchild)
        preorderTraversal(rootNode.rightchild)

preorderTraversal(newBT)


print("*********************************************")
# 
#2.Inorder Traversal of Binary Tree:-
# ================================================
# InOrder Traversal of Binary Tree
# ================================================
#
#                  N1
#                 /  \
#               N2     N3
#              /  \   /  \
#            N4    N5 N6   N7
#           /  \
#         N9    N10
#
# InOrder: N9 → N4 → N10 → N2 → N5 → N1 → N6 → N3 → N7
# Order: Left → Root → Right

def inOrderTraversal(rootnode):
    if not rootnode:
        return
    inOrderTraversal(rootnode.leftchild)
    print(rootnode.data)
    inOrderTraversal(rootnode.rightchild)
inOrderTraversal(newBT)

print("********************************************")

#3.Postorder traversal:-
# =============================================================================
#                  POST-ORDER TRAVERSAL OF BINARY TREE
# =============================================================================
#
#                     Left Subtree          Right Subtree          Root Node
#                          ↓                       ↓                   ↓
#
#                               N1
#                              /  \
#                            N2    N3
#                           /  \   /  \
#                         N4    N5 N6   N7
#                        /  \
#                      N9    N10
#
# Post-Order Traversal Order (Left → Right → Root):
# N9 → N10 → N4 → N5 → N2 → N6 → N7 → N3 → N1
#
# =============================================================================
def postorderTraversal(rootnode):
    if not rootnode:
        return
    postorderTraversal(rootnode.leftchild)
    postorderTraversal(rootnode.rightchild)
    print(rootnode.data)

postorderTraversal(newBT)

# =============================================================================
#                  LEVEL ORDER TRAVERSAL OF BINARY TREE
# =============================================================================
#
# What is Level Order Traversal? (Simple Explanation)
# ===================================================
# Level Order Traversal is also called Breadth-First Search (BFS).
# It visits the tree **level by level**, from top to bottom,
# and left to right on each level.
#
# Think of it like:
# → First visit the root
# → Then visit all its children (Level 1)
# → Then visit all grandchildren (Level 2)
# → And so on...
#
# Example Tree:
#
#                               N1                  ← Level 0 (Root)
#                              /  \
#                            N2    N3               ← Level 1
#                           /  \   /  \
#                         N4    N5 N6   N7          ← Level 2
#                        /  \
#                      N9    N10                     ← Level 3
#
# Level Order Traversal Result:
# N1 → N2 → N3 → N4 → N5 → N6 → N7 → N9 → N10
#
# Simple Steps:
# 1. Start at the root node (N1)
# 2. Visit all nodes at the current level before moving to the next level
# 3. Always process left child before right child
# 4. It uses a Queue (First In, First Out) to remember which nodes to visit next
#
# Key Point:
# Unlike Preorder, Inorder, or Postorder (which go deep first),
# Level Order goes wide first — level by level.
#
# =============================================================================

def levelOrderTraversal(rootnode):
   if not  rootnode:
       return
   else:
       customQueue = qe.Queue()
       customQueue.enqueue(rootnode)
       while not(customQueue.isEmpty()):
           root = customQueue.dequeue()
           print(root.value.data)
           if (root.value.leftchild is not None):
               customQueue.enqueue(root.value.leftchild)
           if (root.value.righttchild is not None):
               customQueue.enqueue(root.value.rightchild)
        
levelOrderTraversal(newBT)


# SEARCH NODE:
def searchBT(rootnode, nodevalue):
    if not rootnode:
        return "The Binary tree does not exist"
    else:
        customQueue = qe.Queue()
        customQueue.enqueue(rootnode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            

            if root.data == nodevalue:
                return "Success"
            if root.leftchild is not None:
                customQueue.enqueue(root.leftchild)
            if root.rightchild is not None:  # Fixed spelling typo here too
                customQueue.enqueue(root.rightchild)
        return "Not found"

print("--- Search Result ---")
print(searchBT(newBT, "Tea"))  


#Insert a  node in Binary Tree
# -A root node is blank.
# -The tree exist and we have to look for first vacant place
# -Use a Level order traversal to find vacant place.

def inserNodeBT(rootnode,newnode):
    if not rootnode:
        rootnode=newnode
    else:
        customQueue = qe.Queue()
        customQueue.enqueue(rootnode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.leftchild)
            else:
                root.value.leftchild=newnode
                return "Successfully Inserted"
            
            if root.value.rightchild is not None:
                customQueue.enqueue(root.value.rightchild)
            else:
                root.value.rightchild=newnode
                return "Successfully Inserted"
            
newnode=Tree("Fanta")
print(inserNodeBT(newBT,newnode))
levelOrderTraversal(newBT)          



