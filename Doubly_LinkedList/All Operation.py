class Node:
    def __init__(self, value=None):
        self.value = value
        self.next= None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
       self.head = None
       self.tail =None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node = node.next

#Creation of Doubly Linked List

    def createDLL(self, nodeValue):
        node=Node(nodeValue)
        node.prev=None
        node.next=None
        self.head=node
        self.tail=node
        return "The DLL is created Successfully"
    
    # Insertion Method in Doubly Linked List
    def insertNode(self,nodevalue,location):
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newNode = Node(nodevalue)
            if location == 0:
                newNode.prev=None
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
            elif location == 1:
                newNode.next=None
                newNode.prev=self.tail
                self.tail.next=newNode
                self.tail=newNode
            else: 
                tempNode= self.head
                index = 0
                while index< location-1:
                    tempNode=tempNode.next
                    index+=1
                newNode.next=tempNode.next
                newNode.prev=tempNode
                newNode.next=newNode
                tempNode.next=newNode



#Traversal Method in Doubly Linked List:
    def traversallDoublyll(self):
        if self.head is None:
            print("Traversall of this DLL Not Possible")
        else:
            tempnode=self.head
            while tempnode:
                print(tempnode)
                tempnode = tempnode.next

    def reversetraversallDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
         tempnode=self.tail
        while tempnode:
            print(tempnode)
            tempnode=tempnode.prev


#Search Method in Doubly Linked List
    def searchDLL(self, nodevalue):
        if self.head is None:
            print("There is not any element in the list")
        else:
            tempnode=self.head
            while tempnode:
                if tempnode.value==nodevalue:
                    return tempnode.value
                tempnode =tempnode.next
            return "The node does not exist in this list"
        
# Delete A Node In SinglyLinked list
    def deleteNode(self,location):
        if self.head is None:
            print("There is no element in DLL")
        else:
            if location == 0:
                if self.head==self.Tail:
                 self.head=None
                 self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=None
            elif location ==1:
                if self.head==self.tail:
                 self.head=None
                 self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=None
            else:
                currentnode=self.head
                index=0
                while index<location-1:
                    currentnode=currentnode.next
                    index+=1
                currentnode.next=currentnode.next.next
                currentnode.next.prev=currentnode
            print("The node has been sucessfully deleted")



doubyll=DoublyLinkedList()
doubyll.createDLL(5)
print([node.value for node in doubyll])
doubyll.insertNode(0,0) #beggining
doubyll.insertNode(2,1) #End
#print([node.value for node in doubyll])
#doubyll.searchDLL(1)
#doubyll.traversallDoublyll()
doubyll.deleteNode(1)
#doubyll.reversetraversallDLL()
print([node.value for node in doubyll])