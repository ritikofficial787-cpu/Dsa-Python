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


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)




print([node.value for node in singlyLinkedList])
# 