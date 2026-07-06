# Create Linked list class
from random import randint

class Node:
    def __init__(self, value=None):
        # Initializes a new node with a value and empty pointers to next/prev nodes.
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        # Converts the node's value into a string representation for easy printing.
        return str(self.value) # Making node to printable

class LinkedList:
    def __init__(self, values=None):
        # Initializes an empty linked list with head and tail set to None.
        self.head = None
        self.tail = None

    def __iter__(self):
        # Allows looping through the list elements using a 'for node in linked_list' structure.
        currentnode = self.head
        while currentnode:
            yield currentnode
            currentnode = currentnode.next

    def __str__(self):
        # Generates a string representation of the entire list with '----->' separating elements.
        values = [str(x.value) for x in self]
        return "----->".join(values)

    def __len__(self):
        # Counts and returns the total number of nodes currently in the linked list.
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        # Appends a new node with the given value to the very end (tail) of the list.
        if self.head is None:
            newnode = Node(value)
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generated(self, n, min_value, max_value):
        # Resets the list and populates it with 'n' random integers within a specific range.
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self

customLL = LinkedList()
customLL.generated(10, 0, 99)
print(customLL)