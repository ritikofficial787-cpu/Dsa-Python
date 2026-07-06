#Queue Operation
#-Create Queue
#Enqueue
#Dequeue
#Peek
#isEmpty
#isFull
#deleteQueue

#Queue can be created using Python List or a linked list
#1-Python List: -Queue without capacity, -Queue with capacity (circular Queue)
#2>Linked List

#Enqueue() method -means insert element= And in memeory it located random place and another elemet is added is located at adjacet side.


#Queue Without size limit:-

class Queue():
    def __init__(self):
        self.items=[]

    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items is None:
            return True
        else:
            return False
        
    def Enqueue(self, value):
        self.items.append(value)
        return "The elemet is inserted at the end of Queue"
    
    def Dequeue(self):
        if self.isEmpty():
            return "This is not any element in the queue"
        else :
            return self.items.pop(0)
        
    def Peek(self):
        if self.isEmpty():
            return "This is not any element in the queue"
        else :
            return self.items[0]
        
    def Delete(self):
        self.items=None
        
    
    
customQueue=Queue()
customQueue.Enqueue(1)
customQueue.Enqueue(2)
customQueue.Enqueue(3)
customQueue.Enqueue(4)
#print(customQueue.Dequeue())
#print(customQueue.Peek())
customQueue.Delete()
print(customQueue)

        
