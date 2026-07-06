#Common Operations On AVL Tree:
#Creating of AVL Trees
#Search for a nodes in AVL trees
#Traverse all nodes in AVL tree
#Insert a node in AVL tree
#Delete a node from AVL tree
#Delete the entire AVL trees

#Create AVL tree
#newAVL=AVL()
#rootnode=None
#leftchild=None
#rightchild=None

class AVLNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
        self.height=1


def preorderTraversal(rootNode):
    if not rootNode:
        return 
    else:
        print(rootNode.data)
        preorderTraversal(rootNode.leftchild)
        preorderTraversal(rootNode.rightchild)

def inOrderTraversal(rootnode):
    if not rootnode:
        return
    inOrderTraversal(rootnode.leftchild)
    print(rootnode.data)
    inOrderTraversal(rootnode.rightchild)


def postorderTraversal(rootnode):
    if not rootnode:
        return
    postorderTraversal(rootnode.leftchild)
    postorderTraversal(rootnode.rightchild)
    print(rootnode.data)

"""def levelOrderTraversal(rootnode):
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
               customQueue.enqueue(root.value.rightchild)"""

def SearchNode(rootNode, nodevalue):
    if rootNode.data ==nodevalue:
        print("Thw Value is Found")
    elif nodevalue < rootNode.data:
        if rootNode.leftchild.data == nodevalue:
            print("The Value is Found")
        else:
            SearchNode(rootNode.leftchild, nodevalue)
    else:
        if rootNode.rightchild.data==nodevalue:
            print("The value is found")
        else:
            SearchNode(rootNode.rightchild, nodevalue)



#Insert Node:

def getHeight(rootNode):
    if not rootNode:

        return 0
    return rootNode.height

def rightRotate(disbalanceNode):
    newRoot=disbalanceNode.leftchild
    disbalanceNode.leftchild= disbalanceNode.leftchild.rightchild
    newRoot.rightchild=disbalanceNode
    disbalanceNode.height=1+max(getHeight(disbalanceNode.leftchild), getHeight(disbalanceNode.rightchild))
    newRoot.height=1+max(getHeight(newRoot.leftchild), getHeight(newRoot.rightchild))
    return newRoot

def  leftRotate(disbalance):
    newRoot=disbalance.rightchild
    disbalance.rightchild=disbalance.rightchild.leftchild
    newRoot.leftchild=disbalance
    disbalance.height=1+max(getHeight(disbalance.leftchild), getHeight(disbalance.rightchild))
    newRoot.height=1+max(getHeight(newRoot.leftchild), getHeight(newRoot.rightchild))
    return newRoot

def getBalanced(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftchild)- getHeight(rootNode.rightchild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftchild=insertNode(rootNode.leftchild, nodeValue)
    else:
        rootNode.rightchild=insertNode(rootNode.rightchild, nodeValue)
    
    rootNode.height=1+max(getHeight(rootNode.leftchild), getHeight(rootNode.rightchild))
    balance=getBalanced(rootNode)

    # Case 1: Left-Left -> single right rotation
    if balance > 1 and nodeValue < rootNode.leftchild.data:
        return rightRotate(rootNode)

    # Case 2: Left-Right -> left rotate child, then right rotate root
    if balance > 1 and nodeValue > rootNode.leftchild.data:
        rootNode.leftchild=leftRotate(rootNode.leftchild)
        return rightRotate(rootNode)

    if balance < -1 and nodeValue > rootNode.rightchild.data:
        return leftRotate(rootNode)

    if balance < -1 and nodeValue < rootNode.rightchild.data:
        rootNode.rightchild = rightRotate(rootNode.rightchild)
        return leftRotate(rootNode)

    return rootNode


#Delete
def getMinValueNode(rootNode):
    if not rootNode:
        return rootNode
    return getMinValueNode(rootNode.leftchild)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftchild = deleteNode(rootNode.leftchild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightchild=deleteNode(rootNode.rightchild, nodeValue)
    else:
        if rootNode.leftchild is None:
            temp = rootNode.rightchild
            rootNode = None
            return temp
        elif rootNode.rightchild is None:
            temp = rootNode.leftchild
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.rightchild)
        rootNode.data=temp.data
        rootNode.rightchild=deleteNode(rootNode.rightchild, temp.data)

#Rotation is Required
    balance=getBalanced(rootNode)
    if balance > 1 and getBalanced(rootNode.leftchild)   >=  0:
        return rightRotate(rootNode)
    if balance > -1 and getBalanced(rootNode.rightchild)  <= 0:
        return leftRotate(rootNode)
    if balance > 1 and getBalanced(rootNode.leftchild)  < 0:
        rootNode.leftchild=leftRotate(rootNode.leftchild)
        return rightRotate(rootNode)
    if balance > -1 and getBalanced(rootNode.rightchild) > 0:
        rootNode.rightchild = rightRotate(rootNode.rightchild)
        return leftRotate(rootNode)
    return rootNode

def deleteEntireAVL(rootNode):
    rootNode.data=None
    rootNode.leftchild=None
    rootNode.rightchild=None
    return "The AVL has been successfullly delted"
        


newAVL=AVLNode(5)
newAVL=insertNode(newAVL, 10)
newAVL=insertNode(newAVL,15)
newAVL=insertNode(newAVL,20)
newAVL=deleteNode(newAVL,15)
deleteEntireAVL(newAVL)

inOrderTraversal(newAVL)