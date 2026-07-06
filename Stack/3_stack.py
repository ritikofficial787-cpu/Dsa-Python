#Stack using Linked list
# Create a Stack
#  Create an object of a Linked List Class


class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head =None
    
    def __iter__(self):
        currNode=self.head
        while currNode:
            yield currNode
            currNode=currNode.next

class Stack:
    def __init__(self):
        self.LinkedList=Linkedlist()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
    
    def push(self, value):
        node=Node(value)
        node.next=self.LinkedList.head
        self.LinkedList.head=node

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue=self.LinkedList.head.value
            self.LinkedList.head=self.LinkedList.head.next
            return nodeValue
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue=self.LinkedList.head.value
            return nodeValue
        
    def delete(self):
        self.LinkedList.head =None


customstack=Stack()
customstack.push(1)
customstack.push(2)
customstack.push(3)
#print(customstack.isEmpty())
print(customstack)
print("---------------------")
print(customstack.pop())
print(customstack.peek())
