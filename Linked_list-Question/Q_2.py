#Return Nth to last

#Implement and algorithm to find the nth last element of sibgly linked list:
#
#+------+------+
#       | Head | 001  |---------+
#       +------+------+         |
#                               v
#                       +---------------+
#                  001  |   1   |  111  | [node1]
#                       +---------------+
#                               |
#                               v
#                       +---------------+
#                  111  |   2   |  222  | [node2]
#                       +---------------+
#                               |
#                               v
#                       +---------------+
#                  222  |   0   |  333  | [node3]
#                       +---------------+
#                               |
#                               v
#                       +---------------+
#                  333  |   3   |  444  | [node4]
#                       +---------------+
#                               |
#                               v
#                       +---------------+
#                  444  |   5   |  null | [Node5]
#                       +---------------+
#                               ^
#       +------+------+         |
#       | Tail | 444  |---------+
#      +------+------+
#
#       N = 2 --------->Node 4


from LinkedList import LinkedList
def nthToLast(ll, n):
    pointer1=ll.head
    pointer2=ll.head

    for i in range(n):
        if pointer1 is None:
            return None
        pointer2=pointer2.next
    while pointer2:
        pointer1=pointer1.next
        pointer2=pointer2.next
    return pointer1

coustomLL=LinkedList()
coustomLL.generated(10,0,99)
print(coustomLL)
print(nthToLast(coustomLL,2))
