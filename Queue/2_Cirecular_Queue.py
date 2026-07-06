#Queue with fixed Capacity(Circular Queue)

# Create  queue
#size=6
#start=-1
#Top=-1

# ==============================================================================
# QUEUE OPERATIONS: Step-by-Step Enqueue Process
# ==============================================================================

# ------------------------------------------------------------------------------
# STEP 1: enqueue(5)
# ------------------------------------------------------------------------------
# Description: First element is added. Both pointers point to index 0.
# Pointers   : Start (S) = 0, Top (T) = 0
#
# Array Layout:
#   Index:    [  0  ] [  1  ] [  2  ] [  3  ] [  4  ] [  5  ]
#   Data:    |   5   |       |       |       |       |       |
#             ------- ------- ------- ------- ------- -------
#               ▲ ▲
#               │ │
#               S T  (Both at index 0)

# ------------------------------------------------------------------------------
# STEP 2: enqueue(6)
# ------------------------------------------------------------------------------
# Description: Second element is added. 'Start' stays fixed, 'Top' shifts right.
# Pointers   : Start (S) = 0, Top (T) = 1
#
# Array Layout:
#   Index:    [  0  ] [  1  ] [  2  ] [  3  ] [  4  ] [  5  ]
#   Data:    |   5   |   6   |       |       |       |       |
#             ------- ------- ------- ------- ------- -------
#               ▲       ▲
#               │       │
#               S       T  (Top moves to index 1)

# ==============================================================================

#IF we use dequeue mthod return first element means it returen 5
#Peek method return element on the basis of start (S) 


class Queue():
    def __init__(self, maxsize):
        self.items= maxsize *[None]
        self.maxsize=maxsize
        self.start=-1
        self.top=-1

    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)
    

    def isFull(self):
        if self.top +1==self.start:
            return True
        elif self.start == 0 and self.top +1==self.maxsize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return True
        
    def Enqueue(self,value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top+1==self.maxsize:
                self.top=0
            else:
                self.top +=1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] =value
            return "The elemenet is inseted at the end of the queue"
        

    def Dequeue(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            firstElement=self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start=-1
                self.top=-1
            elif self.start +1== self.maxsize:
                self.start=0
            else:
                self.start+=1
            self.items[start]=None
            return firstElement
        

    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[self.start]
        

    def delete(self):
        self.items=self.maxsize*None
        self.start=-1
        self.top=-1

customQueue=Queue(5)
#print(customQueue.isEmpty())
#print(customQueue.isFull())
customQueue.Enqueue(1)
customQueue.Enqueue(2)
customQueue.Enqueue(3)
customQueue.Enqueue(4)
customQueue.Enqueue(5)
print(customQueue)
