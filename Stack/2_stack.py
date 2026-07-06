#With limited size

class Stack():
    def __init__(self, maxsize):
        self.maxsize=maxsize
        self.list=[]
        
    def __str__(self):
        values = [str(x) for x in self.list]
        values.reverse()
        return "\n".join(values)  # <-- Must be a backslash (\) followed by n
    
    #isEmpty

    def isempty(self):
        if self.list == []:
            return True
        else:
            return False
        
    #isfull
    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False
        
    #push
    def push(self, value):
     if self.isFull():
         return "The stack is full"
     else:
         return self.list.append(value)
         print("The element successfully added")
    

    #pop
    def pop(self):
        if self.isempty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
        

    #peek
    def peek(self):
        if self.isempty():
            return "There is no element in stack"
        else:
            return self.list[len(self.list)-1]
        
    #delete entire stack
    def delete(self):
        self.list=None
        



customstack=Stack(4 )
print(customstack.isempty())
customstack.push(1)
customstack.push(2)
customstack.push(3)
print(customstack)