#Cration

class Heap:
    def __init__(self, size):
        self.customlist=(size+1) * [None]
        self.heapSize=0
        self.maxsize = size+1

def peekofHeap(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.customlist[1]
    
def sizeOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

    
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
         for i in range(1, rootNode.heapSize+1):
             print(rootNode.customlist[i])

def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <=1:
        return
    if heapType =="Min":
        if rootNode.customlist[index]< rootNode.customlist[parentIndex]:
            temp= rootNode.customlist[index]= rootNode.customlist[parentIndex]
            rootNode.customlist[parentIndex]=temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType=="Max":
        if rootNode.customlist[index]> rootNode.customlist[parentIndex]:
            temp=rootNode.customlist[index]
            rootNode.customlist[index] = rootNode.customlist[parentIndex]
            rootNode.customlist[parentIndex] =temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

def insertNode(rootNode, nodevalue, heapType):
    if rootNode.heapSize+1==rootNode.maxsize:
        return "The Binary Heap is Full"
    rootNode.customlist[rootNode.heapSize+1] = nodevalue
    rootNode.heapSize+=1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has benn successfully inserted"


def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex= index *2
    rightIndex= index *2+1
    swapchild=0

    if rootNode.heapSize < leftIndex:
      return
    elif rootNode.heapSize == leftIndex:
       if heapType=="Min":
           if rootNode.customlist[index]> rootNode.customlist[leftIndex]:
               temp=rootNode.customlist[index]
               rootNode.customlist[index] = rootNode.customlist[leftIndex]
               rootNode.customlist[leftIndex] =temp
           return
       else:
           if rootNode.customlist[index] < rootNode.customlist[rightIndex]:
               temp=rootNode.customlist[index]
               rootNode.customlist[index] = rootNode.customlist[rightIndex]
               rootNode.customlist[rightIndex]=temp
           return
    else:
        if heapType == "Min":
            if rootNode.customlist[leftIndex] < rootNode.customlist[rightIndex]:
               swapchild=leftIndex
            else:
                swapchild=rightIndex
            if rootNode.customlist[index] > rootNode.customlist[swapchild]:
                temp=rootNode.customlist[index]
                rootNode.customlist[index] = rootNode.customlist[swapchild]
                rootNode.customlist[swapchild] =temp

        else: 
            if rootNode.customlist[leftIndex] > rootNode.customlist[rightIndex]:
                swapchild=leftIndex
            else:
                swapchild=rightIndex
            if rootNode.customlist[index]< rootNode.customlist[swapchild]:
                temp=rootNode.customlist[index]
                rootNode.customlist[index]= rootNode.customlist[swapchild]
                rootNode.customlist[swapchild] =temp

    heapifyTreeExtract(rootNode, swapchild, heapType)

def extractNode(rootNode, heapType):
    if rootNode.heapSize==0:
        return
    else:
        extractNode=rootNode.customlist[1]
        rootNode.customlist[1]=rootNode.customlist[rootNode.heapSize]
        rootNode.customlist[rootNode.heapSize] = None
        rootNode.heapSize -=1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractNode

#Delete Entire Binary Heap
# customList=None

def deleteEntireBH(rootNode):
    rootNode.customlist=None
                
            
           



newBinaryHeap=Heap(5)
insertNode(newBinaryHeap, 4, "Max")
insertNode(newBinaryHeap, 5, "Max")
insertNode(newBinaryHeap, 2, "Max")
insertNode(newBinaryHeap, 1, "Max")
extractNode(newBinaryHeap, "Max")

levelOrderTraversal(newBinaryHeap)
#print(sizeOfHeap(newBinaryHeap))