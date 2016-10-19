###############################################################################
#
# 2.3 Delete Middle Node
#
# Implement an algorithm to delte a node in the middle (i.e., any node but the
# first and last node, not necessarily the exact middle) of a singly linked
# list, given only access to that node.
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
def del_mid(mid):
    mid.data = mid.next.data
    mid.next = mid.next.next

ll.print_list()

node = ll.head
del_mid(node.next.next.next)

ll.print_list()
