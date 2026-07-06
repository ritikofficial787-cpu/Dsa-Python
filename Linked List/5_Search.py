#Linked List Search
# =========================================================================
# HOW SEARCHING WORKS IN A LINKED LIST (SIMPLE WORDS):
# =========================================================================
# 1. Start: Give the function a target value you want to find (nodeValue).
# 2. Check Head: Look at the start of the list. If it's empty, stop immediately!
# 3. Look & Compare: Walk through the list node by node.
#    - If matching value is FOUND (Yes) -> Stop and say "Found it!".
#    - If NOT found (No) -> Move to the next node and check again.
# 4. Terminate: Stop when you find the value or run out of nodes.
# =========================================================================

#                      ┌─────────┐
#                      │  Start  │
#                      └────┬────┘
#                           │
#                           ▼
#                    ┌─────────────┐
#                    │  nodeValue  │
#                    └──────┬──────┘
#                           │
#                           ▼
#                  /─────────────────\
#                 <    Check Head?    >
#                  \─────────────────/
#                    /             \
#                  No               Yes
#                  /                 \
#                 ▼                   ▼
#           ┌───────────┐     /───────────────────────\
#           │ Terminate │◄───<  nodeValue==currentNode >◄───┐
#           └───────────┘     \───────────────────────/     │
#                 ▲                       │                 │
#                 │                      Yes                No
#                 │                       │                 │
#                 └───────────────────────┴─────────────────┘

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

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)

singlyLinkedList.insertSLL(0, 0)
# This inserts at index 4 safely now because the list has enough nodes
singlyLinkedList.insertSLL(99, 4) 

print(singlyLinkedList.insertSLL)

#singlyLinkedList.traverseSLL()
print(singlyLinkedList.searchSLL(1))