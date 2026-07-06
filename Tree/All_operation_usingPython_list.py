# Insert a node in Binary Tree
#
# - The Binary Tree is full
# - We have to look for a first vacant place
#
# Tree structure:
#                  N1
#                /    \
#              N2      N3
#             /  \    /  \
#           N4   N5  N6  N7
#          / \    \
#        N8  N9   new (newNode)
#
# newNode insertion logic:
#   Left child = cell[2x]
#   x = 5, cell[2*5 = 10]
#   => N5's left child slot is empty (index 10), so newNode goes there
#
# Array representation (1-indexed, index 0 unused):
# Index:  0    1    2    3    4    5    6    7    8    9    10    11
#         X    N1   N2   N3   N4   N5   N6   N7   N8   N9   New
#
# Note: index 0 is marked invalid (X) since array-based binary trees
# typically start indexing from 1 for easier parent/child calculations:
#   left child  = 2*i
#   right child = 2*i + 1
#   parent      = i // 2

#Create Binary Tree Using Python List:-
class BinaryTree:
    def __init__(self,size):
        self.customList=size*[None]
        self.lastUsedIndex =0
        self.maxsize=size
   
    def insertNode(self,value):
        if self.lastUsedIndex+1==self.maxsize:
            return "The Binary Tree is Full"
        self.customList[self.lastUsedIndex+1]=value
        self.lastUsedIndex +=1
        return "The value Successfully Inserted"


#Search For a node in Binary Tree(Python List)
    def searchNode(self,nodevalue):
        for i in range(len(self.customList)):
            if self.customList[i]==nodevalue:
             return "Sucess"
        return "Not Found"
    

#Traversal (Usinf PreorderTraversal):-Uisng Python List
    def preOrderTraversal(self,index):
        if index> self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2+1)


#Inorder Traversal of Binary Tree (Python List)
    def InOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        self.preOrderTraversal(index*2)
        print(self.customList[index])
        self.preOrderTraversal(index*2+1)

#PostOrder Traversal of Binary Tree(python List)
    def PostOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        self.PostOrderTraversal(index*2)
        self.PostOrderTraversal(index*2+1)
        print(self.customList[index])

#Level Order Traversal of Binary Tree(Python List)
    def LevelOrderTraversal(self,index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

#Delete a node from a Binary Tree(python List)
 #Level order Traversal:
 # deepestNode = lasUsedIndex

    def deleteNode(self, value):
        if self.lastUsedIndex ==0:
            return"There is not any element to delete"
        for i in range(1,self.lastUsedIndex+1):
            if self.customList[i]==value:
                self.customList[i]= self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] =None
                self.lastUsedIndex-=1
                return"The node has been successfully deleted"
            
#Delete Entire Binary Tree(python List)
    def deleteEntireBT(self):
      self.customList=None
      return"The Binary Tree Successfully Delted"
      





newBT=BinaryTree(6)
print(newBT.insertNode("Food"))
print(newBT.insertNode("Veg"))
print(newBT.insertNode("Nonveg"))
newBT.insertNode("Veg Biryani")
newBT.insertNode("NonVeg Biryani")
print(newBT.searchNode("Ritik"))
print("*************************")
print(newBT.preOrderTraversal(1))
print("******************************")
print(newBT.InOrderTraversal(1))

print("*****************")
print(newBT.PostOrderTraversal(1))

print("*********************")
print(newBT.LevelOrderTraversal(1))
print("**********************")
print(newBT.deleteNode("Veg"))
print("*************")
print(newBT.deleteEntireBT())

newBT.LevelOrderTraversal(1)

