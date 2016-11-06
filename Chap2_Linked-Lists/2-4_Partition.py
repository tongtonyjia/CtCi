###############################################################################
#
# 2.4 Partition
#
# Write code to partition a linked list around a value x, such that all nodes
# less than x come before all nodes greater than or equal to x. If x is
# contained within the list, the values of x only need to be after the elements
# less than x (see below). The partition element x an appear anywhere in the
# "right partition"; it does not need to appear between the left and right
# partitions.
#
# EXAMPLE
# Input:    3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output:   3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
#
###############################################################################

import LibraryPath
from lib.LinkedList import LinkedList


ll = LinkedList()
ll.add_node(3)
ll.add_node(5)
ll.add_node(8)
ll.add_node(5)
ll.add_node(10)
ll.add_node(2)
ll.add_node(1)


# Time: O(n), Space: O(1)
def partition(ll, partition):
    node = ll.head
    length = 1
    while node.next is not None:
        length += 1
        node = node.next
    tail = node

    node = ll.head
    prev = ll.head
    count = 0
    while count <= length:
        if node.data >= partition:
            if node == ll.head:
                ll.head = node.next
                prev = ll.head
            else:
                prev.next = node.next
            ll.add_node(node.data)
            tail = tail.next
        else:
            prev = node

        node = node.next
        count += 1

    return ll


partition(ll, 5).print_list()
