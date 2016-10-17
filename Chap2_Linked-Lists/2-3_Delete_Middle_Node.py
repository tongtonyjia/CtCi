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
ll.AddNode(1)
ll.AddNode(3)
ll.AddNode(1)
ll.AddNode(2)
ll.AddNode(6)
ll.AddNode(2)
ll.AddNode(4)


# Time: O(n), Space: O(n)
def del_mid(mid):
    mid.data = mid.next.data
    mid.next = mid.next.next

ll.PrintList()

node = ll.head
del_mid(node.next.next.next)

ll.PrintList()
