# Given the root node to a singly linked list, reverse the last n nodes in the
# list.

import LibraryPath
from lib.LinkedList import LinkedList


def rev_n(head, n):
    if head is None:
        return

    cur1 = head
    cur2 = head
    count = 0
    while cur1.next is not None:
        cur1 = cur1.next
        if count >= n:
            cur2 = cur2.next
        count += 1
    if count < n:
        return

    hook = cur2
    cur2 = cur2.next
    prev = None
    while cur2 is not None:
        nextt = cur2.next
        cur2.next = prev
        prev = cur2
        cur2 = nextt
    hook.next = prev


ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.add_node(5)
ll.add_node(6)
ll.add_node(7)
ll.add_node(8)

rev_n(ll.head, 2)
ll.print_list()
