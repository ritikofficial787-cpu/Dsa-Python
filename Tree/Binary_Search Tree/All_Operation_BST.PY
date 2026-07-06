#Creation of Binary Search Tree(Linked list):

class BSTNode:
    def __init__(self, data):
        self.data=data
        self.leftchild=None
        self.rightchild=None



#Insert a Node to Bianry Search Tree:-
def isnserNodeBST(rootNode,nodevalue):
    if rootNode.data is None:
        rootNode.data=nodevalue
    elif  nodevalue<=rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild=BSTNode(nodevalue)
        else:
            isnserNodeBST(rootNode.leftchild, nodevalue)


    else:
        if rootNode.rightchild is None:
            rootNode.rightchild=BSTNode(nodevalue)
        else: 
            isnserNodeBST(rootNode.rightchild, nodevalue)
    return "The Node has been Successfully inserted"


#Traversal of Binary Search Tree:-
#1. Depth first search
#   -Preorder traversal  :- Left Subtree → Right Subtree
#   -Inorder traversal :- Left → Root → Right
#   -Post order traversal :-  Left → Right → Root
#2. Breadth first Search
#  -Level order traversal

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)

def InOrderTraversal(rootNode):
    if not rootNode:
        return
    InOrderTraversal(rootNode.leftchild)
    print(rootNode.data)
    InOrderTraversal(rootNode.rightchild)

def PostOrderTraversal(rootNode):
    if not rootNode:
        return
    PostOrderTraversal(rootNode.leftchild)
    PostOrderTraversal(rootNode.rightchild)
    print(rootNode.data)


#LevelOrder Trvaersal
def LevelOrderTraversal(rootNode):
    if not rootNode:
        return
        customQueue=qe.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customQueue.enquue(root.value.leftchild)

#Search  for a node in Binary Search Tree:-
def SearchNode(rootnode,nodeValue):
    if rootnode.data==nodeValue:
         print("The Vlaue is Found")
    elif nodeValue <rootnode.data:
        if rootnode.leftchild.data==nodeValue:
            print("The Vlaue is Found")
        else:
            SearchNode(rootnode.leftchild, nodeValue)
    else:
        nodeValue>rootnode.data
        if rootnode.rightchild.data==nodeValue:
            print("The Value is Found")
        else:
            SearchNode(rootnode.rightchild, nodeValue)



#Delete a Node From Binary Search Tree:-
 #case1:The node to be deleetd is a leaf node
 #case2:The Node has one child
   #Then Assign child node has parent node
 #case3:The Node has two Children
   #

def minValueNode(bstNode):
    current = bstNode
    while (current.leftchild is not None):
        current=current.leftchild
    return current

def deleteNode(rootnode, nodevalue):
    if rootnode is None:
        return rootnode
    if nodevalue < rootnode.data:
        rootnode.leftchild=deleteNode(rootnode.leftchild, nodevalue)
    elif nodevalue >rootnode.data:
        rootnode.rightchild=deleteNode(rootnode.rightchild, nodevalue)
    else:
        if rootnode.leftchild is None:
            temp = rootnode.rightchild
            rootnode=None
            return temp
        if rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode=None
            return temp
        
        temp = minValueNode(rootnode.rightchild)
        rootnode.data=temp.data
        rootnode.rightchild=deleteNode(rootnode.rightchild, temp.data)
    return rootnode

#Delete Entire BST
#roootnode=None
#rootnode=leftchild=None
#rootnode.rightchild=None

def DeleteEntireBst(rootnode):
    rootnode.data=None
    rootnode.leftchild=None
    rootnode.rightchild=None
    return "Rhe BST Has successfully Deleted"

    
    

       
      



customBST=BSTNode(None)
isnserNodeBST(customBST, 70)
isnserNodeBST(customBST, 50)
isnserNodeBST(customBST, 90)
isnserNodeBST(customBST, 30)
isnserNodeBST(customBST, 60)
isnserNodeBST(customBST, 80)
isnserNodeBST(customBST, 100) 
isnserNodeBST(customBST,20)
isnserNodeBST(customBST, 40)
isnserNodeBST(customBST,60)
deleteNode(customBST,100)
LevelOrderTraversal(customBST)
print("******************")
preOrderTraversal(customBST)

print("**************")
InOrderTraversal(customBST)

print("****************")
PostOrderTraversal(customBST)

print("***************")
SearchNode(customBST,60)

print(DeleteEntireBst(customBST))







#print(customBST.data)
#print(customBST.leftchild.data)
#print(customBST.rightchild.data)
   