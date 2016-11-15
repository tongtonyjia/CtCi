###############################################################################
#
# 2.7 Intersection
#
# Given two (singly) linked lists, determine if the two lists intersect. Return
# the intersecting node. Note that the intersection is defined based on
# reference, not value. That is, if the kth node fo the first linked list is
# the exact same node (by reference) as the jth node of the second linked list,
# then they are intersecting.
#
###############################################################################

import LibraryPath
from lib.LinkedList import LinkedList


ll1 = LinkedList()
ll1.add_node(3)
ll1.add_node(5)
ll1.add_node(8)


ll2 = LinkedList()
ll2.add_node(5)
ll2.add_node(10)
ll2.add_node(2)
ll2.add_node(6)


ll3 = LinkedList()
ll3.add_node(1)
ll3.add_node(5)
ll3.add_node(4)


node = ll1.head
while node.next is not None:
    node = node.next

node.next = ll3.head

node = ll2.head
while node.next is not None:
    node = node.next

node.next = ll3.head

ll1.print_list()
ll2.print_list()


def find_intersect(ll1, ll2):
    node = ll1.head
    ll1_length = 0
    while node.next is not None:
        ll1_length += 1
        node = node.next
    tail1 = node

    node = ll2.head
    ll2_length = 0
    while node.next is not None:
        ll2_length += 1
        node = node.next
    tail2 = node

    if tail1 != tail2:
        return False

    delta = min(ll1_length, ll2_length)
    ll1_head_start = ll1_length - delta
    ll2_head_start = ll2_length - delta

    ll1_pointer = ll1.head
    ll2_pointer = ll2.head
    while ll1_pointer.next is not None and ll2_pointer.next is not None:
        if ll1_pointer == ll2_pointer:
            return ll1_pointer
        if ll1_head_start == ll2_head_start:
            ll1_pointer = ll1_pointer.next
            ll2_pointer = ll2_pointer.next
        else:
            if ll1_head_start != 0:
                ll1_pointer = ll1_pointer.next
                ll1_head_start -= 1
            elif ll2_head_start != 0:
                ll2_pointer = ll2_pointer.next
                ll2_head_start -= 1

    return False

result = find_intersect(ll1, ll2)
if result:
    print result.data
else:
    print "False"
