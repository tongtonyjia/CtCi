###############################################################################
#
# 2.8 Loop Detection
#
# Given a circular linked list, implement an algorithm that returns the node at
# the beginning of the loop.
#
# DEFINITION
# Circular linked list: A (currupt) linked list in which a node's next pointer
# point to an earlier node, so as to make a loop in the linked list.
#
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C [the same C as earlier]
# Output: C
#
###############################################################################

import LibraryPath
from lib.LinkedList import LinkedList


ll0 = LinkedList()
ll0.add_node(1)
ll0.add_node(2)
ll0.add_node(3)
ll0.add_node(4)
ll0.add_node(5)
ll0.add_node(6)

node = ll0.head
while node.next is not None:
    if node.data == 3:
        loop_node = node
    node = node.next
node.next = loop_node


ll1 = LinkedList()
ll1.add_node(1)
ll1.add_node(2)
ll1.add_node(3)
ll1.add_node(4)
ll1.add_node(5)
ll1.add_node(6)
ll1.add_node(7)
ll1.add_node(8)
ll1.add_node(9)

node = ll1.head
while node.next is not None:
    if node.data == 2:
        loop_node = node
    node = node.next
node.next = loop_node


ll2 = LinkedList()
ll2.add_node(5)
ll2.add_node(10)
ll2.add_node(2)
ll2.add_node(6)
ll2.add_node(3)
ll2.add_node(5)
ll2.add_node(8)
ll2.add_node(5)
ll2.add_node(10)
ll2.add_node(2)
ll2.add_node(6)


def find_circular(ll):
    fast = ll.head
    slow = ll.head

    while slow is not None and fast is not None:
        if fast.next is None:
            return False

        slow = slow.next
        fast = fast.next

        if fast.next is None:
            return False

        fast = fast.next

        if slow == fast:
            break

    slow = ll.head
    while slow is not None:
        slow = slow.next
        fast = fast.next

        if slow == fast:
            return slow.data

print find_circular(ll0)
print find_circular(ll1)
print find_circular(ll2)
