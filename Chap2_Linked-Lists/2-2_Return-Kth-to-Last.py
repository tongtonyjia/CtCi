###############################################################################
#
# 2.2 Return Kth to Last
#
# Implement an algorithm to find the kth to last element of a singly linked
# list.
#
###############################################################################

import LibraryPath
from lib.LinkedList import LinkedList


ll = LinkedList()
ll.add_node(1)
ll.add_node(3)
ll.add_node(1)
ll.add_node(2)
ll.add_node(6)
ll.add_node(2)
ll.add_node(4)


# Time: O(n), Space: O(n)
def kth_to_last(ll, k):
    node = ll.head

    node_map = dict()
    counter = 0

    while node is not None:
        node_map[counter] = node
        node = node.next
        counter += 1

    if k > counter:
        return 'k larger than length of linked list.'
    else:
        return node_map[counter-k].data


# Time: O(n), Space: O(1)
def kth_to_last_better(ll, k):
    node = ll.head
    runner = ll.head
    distance = 0
    while node is not None:
        if distance < k:
            node = node.next
            distance += 1
        else:
            node = node.next
            runner = runner.next

    if distance != k:
        return 'k larger than length of linked list.'
    else:
        return runner.data

print kth_to_last(ll, 3)
print kth_to_last_better(ll, 3)
