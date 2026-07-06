#Delete a node from singly Linked list
class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempnode = self.head
                index = 0 
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                # FIXED INDENTATION HERE
                nextNode = tempnode.next
                tempnode.next = newNode
                newNode.next = nextNode


    def traverseSLL(self):
        if self.head is None:
            print("The Single Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    def searchSLL(self, nodeValue):
        if self.head is None:
            return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node=node.next
            return "The value not exist in List"


    # Ensure this method is indented exactly like 'insertSLL' or 'traverseSLL'
    def deleteNode(self, location):
        if self.head is None:
            print("The SLL does not exist")
        else:
            # Case 1: Delete the first node
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            
            # Case 2: Delete the last node
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            
            # Case 3: Delete from a specific index (Middle)
            else:
                tempNode = self.head
                index = 0
                # Fixed: loop runs until it reaches the node right BEFORE the target
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                
                # Fixed: Properly link over the deleted node
                nextNode = tempNode.next
                tempNode.next = nextNode.next

#Entire list drlete
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head=None
            self.tail=None
    
        



        

singlyLinkedList = SLinkedList() 


singlyLinkedList.insertSLL(1, 0)   # ya 1
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 2)
singlyLinkedList.insertSLL(4, 3)
singlyLinkedList.insertSLL(5, 4)

print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteEntireSLL()
singlyLinkedList.traverseSLL()
#singlyLinkedList.deleteNode()
print([node.value for node in singlyLinkedList])



