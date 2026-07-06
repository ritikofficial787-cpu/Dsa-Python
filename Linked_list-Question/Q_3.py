#Partition

#Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equla to x

#[Head: 001]---> [node1: 001]       [node2: 111]       [node3: 222]       [node4: 333]       [Node5: 444]
#               +----+-----+       +----+-----+       +----+-----+       +----+-----+       +----+------+
#                | 11 | 111 |------>|  3 | 222 |------>|  9 | 333 |------>| 10 | 444 |------>| 15 | null |
#                +----+-----+       +----+-----+       +----+-----+       +----+-----+       +----+------+
#                                                                                                 ^
#[Tail: 444]--------------------------------------------------------------------------------------+
#x = 10
#currentnode=node1
#Tail=node1
#currentnode.next=null

from LinkedList import LinkedList

def partition(ll, x):
    currentnode = ll.head
    
    # Track the real end of the list using a local variable
    local_tail = ll.tail  
    
    while currentnode:
        nextnode = currentnode.next
        
        if currentnode.value < x:
            # Case 1: Nodes smaller than x move to the head
            if currentnode == ll.head:
                # If it's already the head, just move on
                pass 
            else:
                currentnode.next = ll.head
                ll.head = currentnode
        else:
            # Case 2: Nodes greater/equal to x move after our tracked tail
            if currentnode == local_tail:
                # If it's already the tracked tail, update our marker
                local_tail = currentnode
            else:
                local_tail.next = currentnode
                local_tail = currentnode
                local_tail.next = None # Prevent circular loops!
                
        currentnode = nextnode
        
    # Update the actual class tail property once at the end
    ll.tail = local_tail
    return ll

customLL = LinkedList()
customLL.generated(10, 0, 99)
print(customLL)
partition(customLL, 20)
print(customLL)