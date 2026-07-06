#List of depth:-

#Problem statement 
#    Given a  binary search tree, design an algorithm which creates a linked list of all the nodes at  each depth 

class LinkedList:
    def __init__(self, value):
        self.value=value
        self.next=None

    def add(self, value):
        if self.next==None:
            self.next == LinkedList(value)
        else:
            self.next.add(value)

    def __str__(self):
        return "({value})". format(value=self.value) + str(self.next)
    
class BinaryTree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def depth(tree):
    if tree == None:
        return 0
    if tree.left == None and tree.right == None:
        return 1
    else:
        depthleft = 1+ depth(tree.left)
        depthright=1+ depth(tree.right)
        if depthleft >depthright:
           return depthleft
        else:
            depthright

def treeToLinkedList(tree,custDict = { }, d=None):
    if d == None:
        d = depth(tree)
    if custDict.get(d) == None:
        custDict[d] = LinkedList(tree.value)
    else:
        custDict[d].add(tree.value)
        if d == 1:
            return custDict
    if tree.left !=None:
        custDict = treeToLinkedList(tree.left, custDict, d-1)
    if tree.right !=None:
        custDict = treeToLinkedList(tree.right, custDict, d-1)
    return custDict

mainTree = BinaryTree(1)
mainTree = BinaryTree(1)
two = BinaryTree(2)
three = BinaryTree(3)
four = BinaryTree(4)
five = BinaryTree(5)
six = BinaryTree(6)
seven = BinaryTree(7)
mainTree.left = two
mainTree.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

custDict = treeToLinkedList(mainTree)
for depthLevel, LinkedList in custDict.items():
    print("{0} {1}".format(depthLevel, LinkedList))
    
