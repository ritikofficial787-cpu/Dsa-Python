class Node:
    def __init__(self, value=None):
        self.value = value
        self.next= None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node= self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

            
    #Creation Circular singly linked list
    def createSCLL(self, nodeValue):
        node = Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
        return"The CSLL has been created"
    
    #Insertion
    # Insertion
    def insertionCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            
            if location == 0:  # Beginning
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
                
            elif location == 1:  # End
                newNode.next = self.tail.next  # Points back to head
                self.tail.next = newNode
                self.tail = newNode
                
            else:  # Specific location
                tempnode = self.head
                index = 0
                # Traverse to the node just before the insertion point
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                
                # Get the node that comes after our insertion point
                nextNode = tempnode.next
                # Link current node to new node
                tempnode.next = newNode
                # Link new node to the next node
                newNode.next = nextNode
                
            return "The node has been successfully inserted"
        


    #Traversal  of a node in circular singly linked list
    # ==========================================
# FLOWCHART LOGIC: TRAVERSAL OPERATION
# ==========================================

# [START] -> Begin the traversal process

# CHECK HEAD? (Is the list empty?)
# ├── NO  -> [TERMINATE] (Exit immediately, nothing to print)
# └── YES -> Proceed to the loop

# LOOP WHILE Node is valid:
# ├── PRINT(currentNode.value)
# ├── MOVE to the next node (currentNode = currentNode.next)
# └── IF Node has circled back to Head:
#     └── [TERMINATE] (Break loop to prevent an infinite cycle)
    def traversalSCLL(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            tempnode =self.head
            while tempnode:
                print(tempnode.value)
                tempnode=tempnode.next
                if tempnode == self.tail.next:
                    break

# Searchin - Circular Singly Linked List
# ==========================================
# FLOWCHART LOGIC: SEARCH OPERATION
# ==========================================

# [INPUT]: nodeValue -> The target value we want to find

# CHECK HEAD? (Is the list empty?)
# ├── NO  -> [TERMINATE] (Exit immediately, value cannot exist)
# └── YES -> Proceed to look for the value

# LOOP WHILE checking each node:
# ├── IF currentNode.value == nodeValue:
# │   └── YES -> [TERMINATE] (Value found! Success)
# │
# └── NO -> Move to next node (currentNode = currentNode.next)
#     └── IF circled back to Head:
#         └── [TERMINATE] (Value not found in entire list)
    def searchCSLL(self, nodevalue):
            if self.head is None:
               print("There is not any node in this CSLL")
            else: 
                tempnode = self.head
                while tempnode:
                    if tempnode.value   == nodevalue:
                        return {tempnode.value}
                    tempnode= tempnode.next
                    if tempnode==self.tail.next:
                        return " The node does not exist in this CSLL"
                    

#Delete a node from circulR SINGLY LINKED LIST
    def DeleteSCLL(self,location):
        if self.head is None:
            print("There is no Element in SCLL TO DEleted")
        else:
            if location ==0: #Begginig
                if self.head == self.tail: #Means we have only one node
                    self.head.next=None
                    self.head=  None
                    self.tail=None
                else:             #More than one node
                    self.head=self.head.next
                    self.tail = self.head
            elif location==1:  #Means we have only one node
                  if self.head == self.tail: #Means we have only one node
                    self.head.next=None
                    self.head=  None
                    self.tail=None
                  else:
                      node = self.head
                      while node is not None:
                          if node.next == self.tail:
                              break
                          node = node.next
                      node.next=self.head
                      self.tail=node
            else:
                tempnode= self.head
                index = 0 
                while index< location -1:
                    tempnode = tempnode.next
                    index+=1
                nextnode= tempnode.next
                tempnode.next=nextnode.next

#Delete Entire Circualar Singly Linked list
    def deleteEntireSCLL(self):
        self.head =None
        self.tail.next = None
        self.tail = None


                
circularSLL=CircularSinglyLinkedList()
circularSLL.createSCLL(1)
circularSLL.insertionCSLL(0,0)
circularSLL.insertionCSLL(2,1)
circularSLL.insertionCSLL(3,1)
circularSLL.insertionCSLL(2,2)
circularSLL.insertionCSLL(3,3)
#circularSLL.traversalSCLL()
#print(circularSLL.searchCSLL(30))

print([node.value for node in circularSLL])
circularSLL.deleteEntireSCLL()
print([node.value for node in circularSLL])


#circularSLL.DeleteSCLL(1)
#circularSLL.DeleteSCLL(3)
#print([node.value for node in circularSLL ])
