#   Without size limit:

class Stack():
    def __init__(self):
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
            
    #push
    def push(self,value):
        self.list.append(value)
        return "The element has been successfully inserted"
    
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
customStack=Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print("Popped item:", customStack.pop())
print("Remaining Stack:")
print(customStack)
print(customStack.delete())
#print("Top element is:",customStack.peek())
#print(customStack.isempty())
