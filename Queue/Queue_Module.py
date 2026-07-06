"""
#How to use collction.dequeue as a FIFO queue

from collection import deque

cutomQueue=dequeu(maxlen=4)
print(customQueue)\



customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
customQueue.append(4)
print(customQueue)
print(cutomQueue.popleft())
print(customQueue.clear())
#If add one more element then it remove first element(overwrite) and currnode"""

import queue as q

cutomQueue= q.Queue(maxsize=4)
print(cutomQueue.qsize())
cutomQueue.put(1)
cutomQueue.put(2)
cutomQueue.put(3)
cutomQueue.put(4)
print(cutomQueue.qsize())
print(cutomQueue.full())
print(cutomQueue.get())

from multiprocessing import Queue

cutomQueue = Queue(maxsize=3)
cutomQueue.put(1)
cutomQueue(cutomQueue.get())


