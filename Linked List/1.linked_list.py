#Creation of singly Linked list:-

# Create Head and Tail, intialize with null
#Create a blank node and assign a value to it and refernece to null.
#Link Head and Tail with these Node
class Node:
    def __init__(self, value=None):
        self.value= value
        self.next=None
    


class SinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

singlyLinkedList=SinkedList()
node1 =Node(1)
node2=Node(2)
singlyLinkedList.head=node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2

#Time complexity to create a singly linked list is O(1)
#Space Complexity is O(1)

