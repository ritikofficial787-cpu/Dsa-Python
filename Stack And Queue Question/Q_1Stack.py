# Use a single list to implement three stacks

class Multistack:
    def __init__(self, numberstack, stacksize):
        self.numberstack = numberstack
        self.custList = [0] * (stacksize * numberstack)
        self.sizes = [0] * numberstack
        self.stacksize = stacksize

    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False

    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False

    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return "The stack is Full"
        else:
            self.sizes[stacknum] += 1
            self.custList[self.indexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            self.custList[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            return value


# 3 stacks, each of size 2
customStack = Multistack(3, 2)

print(customStack.isFull(0))    # False
print(customStack.isEmpty(0))   # True

customStack.push(1, 0)          # Push 1 to stack 0
customStack.push(2, 0)          # Push 2 to stack 0
customStack.push(3, 2)          # Push 3 to stack 2

print(customStack.peek(0))      # 2  (top of stack 0)
print(customStack.peek(2))      # 3  (top of stack 2)
print(customStack.pop(0))       # 2
print(customStack.isEmpty(0))  
print(customStack.peek(1)) 
# False (still has 1)