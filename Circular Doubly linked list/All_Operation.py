#Creation of Circular Doubly Linked
#1. Start  
#2. Get nodeValue  
#3. Create a new blank node and assign `node.value = nodeValue`  
#4. Set `head = node` and `tail = node`  
#5. Set `node.next = node` and `node.prev = node`  
#6. End


class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node == self.tail.next:
                break

#Creation
    def createCDLL(self,nodeValue):  #Only one node
        newNode=Node(nodeValue)
        self.head=newNode
        self.tail=newNode
        newNode.prev=newNode
        newNode.next=newNode
        return "The CDLL is created Successfully"
    

#Insertion
    def insertCDLL(self, value, location):
        if self.head is None:
            print("The CDLL does not exist")
        else:
            newnode=Node(value)
            if location == 0: #Starting
                newnode.next=self.head
                newnode.prev=self.tail
                self.head.prev=newnode
                self.head=newnode
                self.tail.next=newnode
            elif location ==1:
                newnode.next=self.head
                newnode.prev=self.tail
                self.head.prev=newnode
                self.tail.next=newnode
                self.tail=newnode
            else:
                tempnode=self.head
                index = 0
                while index<location-1:
                    tempnode=tempnode.next
                    index +=1
                newnode.next=tempnode.next
                newnode.prev=tempnode
                newnode.next.prev=newnode
                tempnode.next=newnode
            return "The node has benn inserted"
        

#Traverse
    def traversalCDLL(self):
        if self.head is None:
            print("The traversall not possible.")
        else:
            tempnode=self.head
            while tempnode:
                print(tempnode.value)
                if tempnode == self.tail:
                    break
                tempnode=tempnode.next


#Reverse Traversall 
    def reverseTraversal(self):
        if self.head is None:
            print("The reversetraversall not posiible")
        else:
            tempnode = self.tail
            while True:
                print(tempnode.value)
                if tempnode == self.head:
                    break
                tempnode = tempnode.prev

 #Search               

    def searchCDLL(self,nodevalue):
        if self.head is None:
            print("There is not any node in CDLL")
        else:
            tempnode=self.head
            while tempnode:
                if tempnode.value==nodevalue:
                    return tempnode.value
                if tempnode==self.tail:
                    return "The value does not exist in CDLL"
                tempnode=tempnode.next

#Delete
    def deleteCDLL(self,location):
        if self.head is None:
            print("There is not any node to delete")
        else:
            if location == 0:
                if self.head ==self.tail:
                    self.head.prev=None
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=self.tail
                    self.tail.next= self.head
            elif location==1:
                if self.head ==self.tail:
                    self.head.prev=None
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=self.head
                    self.head.prev=self.tail
            else:
                tempnode=self.head  #Tempnode==Current node
                index=0
                while index<location-1:
                 tempnode =tempnode.next
                 index+=1
                tempnode.next=tempnode.next.next
                tempnode.next.prev=tempnode
            print("The node has benn successfully deleted")

#Deleting Entire CDLL
    def deleteEntireCDLL(self):
        if self.head is None:
            print("There is no element to be deleted")
        else:
            self.tail.next=None
            tempnode=self.head
            while tempnode:
             tempnode.prev=None
             tempnode = tempnode.next
            self.head=None
            self.tail=None
        print("The CDLL has been successfully deleted")




                
                    
                


CircularDLL=CircularDoublyLinkedList()
print(CircularDLL.createCDLL(5))
CircularDLL.insertCDLL(0,0)
CircularDLL.insertCDLL(1,1)
CircularDLL.insertCDLL(2,2)

print([node.value for node in CircularDLL])
#CircularDLL.traversalCDLL()
#CircularDLL.reverseTraversal()
#print(CircularDLL.searchCDLL(2))
#CircularDLL.deleteCDLL(1)   #1 reperesent its delete the last node
CircularDLL.deleteEntireCDLL()
print([node.value for node in CircularDLL])

