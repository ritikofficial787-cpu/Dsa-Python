#How would you design a stack,which, in addition to push and pop, has a function mn which
#  returns the minimum element?Push,Pop and min should all operate o(1)

class Node():
    def __init__(self,value=None, next=None):
       self.value=value
       self.next=next

    def __str__(self):
        string=str(self.value)
        if self.next:
            string += ','+ str(self.value)   
        return string
    
class Stack():
    def __init__(self):
        self.top=None
        self.minnode= None

    def min(self):
        if not self.minnode:
            return None
        return self.minnode.value
    
    def push(self, item):
        if self.minnode and (self.minnode.value <item):
            self.minnode=Node(value=self.minnode.value, next=self.minnode)

        else:
            self.minnode =Node(value=item, next=self.minnode)
        self.top=Node(value=item, next=self.top)

    def pop(self):
        if not self.top:
            return None
        self.minnode=self.minnode.next
        item=self.top.value
        self.top=self.top.next
        return item
    
customStack=Stack()
customStack.push(5)
print(customStack.min())
customStack.push(6)
print(customStack.min)
customStack.push(3)
print(customStack)
print(customStack.pop())
print(customStack.min())
