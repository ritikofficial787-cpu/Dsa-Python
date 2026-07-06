#Create Binary Tree Using Python List:-
class BinaryTree:
    def __init__(self,size):
        self.customList=size*[None]
        self.lastUsedIndex =0
        self.maxsize=size

newBT=BinaryTree(8)