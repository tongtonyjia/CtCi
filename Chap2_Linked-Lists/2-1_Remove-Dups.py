###############################################################################
#
# 2.1 Remove Dups
#
# Write code to remove duplicates from an unsorted linked list.
#
# Follow up:
# How would you solve this problem is a temporary buffer is not
# allowed.
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


def remove_dups(ll):
    prev = ll.head
    node = prev.next

    counts = set()
    counts.add(prev.data)

    while node is not None:
        if node.data not in counts:
            counts.add(node.data)
            prev = node
        else:
            prev.next = node.next

        node = node.next

    return ll

remove_dups(ll).PrintList()


def remove_dups_no_buffer(ll):
    current = ll.head

    while current is not None:
        data = current.data
        runner_prev = current
        runner = current.next
        while runner is not None:
            if runner.data == data:
                runner_prev.next = runner.next
            runner = runner.next
        current = current.next

    return ll

remove_dups_no_buffer(ll).PrintList()
