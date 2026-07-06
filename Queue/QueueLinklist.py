#Queue using Linked list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempnode = self.head
        while tempnode:
            yield tempnode
            tempnode = tempnode.next


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]  # Fixed: LinkedList → linkedList
        return ' '.join(values)

    def enqueue(self, value):
        newnode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newnode
            self.linkedList.tail = newnode
        else:
            self.linkedList.tail.next = newnode
            self.linkedList.tail = newnode

    

    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        else:
            return False
        
    def Dequeue(self):
        if self.isEmpty():
            print("There is not any element any node in the Queue")
        else:
            tempnode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head=None
                self.linkedList.tail=None

            else:
                self.linkedList.head=self.linkedList.head.next
            return tempnode
    def peek(self):
        if self.isEmpty():
            print("There is not any element any node in the Queue")
        else:
            return self.linkedList.head
        
    def delete(self):
        self.linkedList.head=None
        self.linkedList.tail=None



customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.Dequeue())
print(customQueue)
print(customQueue.peek())
customQueue.delete()
print(customQueue())
