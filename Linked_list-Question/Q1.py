#Write code to remove duplicate from an unsorted linked list

# currentNode= node1
#   tempset={1}
#  while currentnode.next is not None:
#     if next nodes's value is in tempset
#     Delete next node
#  Otherwise add it to tempset

from LinkedList import LinkedList
def removedups(ll):
    if ll.head is None:
        return
    else:
        currentnode=ll.head
        visited=set([currentnode.value])
        while currentnode.next:
            if currentnode.next.value in visited:
                currentnode.next=currentnode.next.next
            else:
                visited.add(currentnode.next.value)
                currentnode=currentnode.next
            return ll


def removeDups1(ll):
    if ll.head is None:
        return
    
    currentnode=ll.head
    while currentnode:
        runner = currentnode
        while currentnode.next:
            if runner.next.value==currentnode.value:
                runner.next=runner.next.next
            else:
                runner = runner.next
            currentnode=currentnode.next
    return ll.head

cutomLL=LinkedList()
cutomLL.generated(10,0,99)
print(cutomLL)
removeDups1(cutomLL)