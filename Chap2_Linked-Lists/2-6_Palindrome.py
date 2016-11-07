###############################################################################
#
# 2.6 Palindrome
#
# Implement a function to check if a linked list is a palindrome.
#
###############################################################################

import LibraryPath
from lib.LinkedList import LinkedList


ll1 = LinkedList()
ll1.add_node(3)
ll1.add_node(5)
ll1.add_node(8)
ll1.add_node(5)
ll1.add_node(10)
ll1.add_node(2)
ll1.add_node(1)

ll2 = LinkedList()
ll2.add_node(1)
ll2.add_node(2)
ll2.add_node(10)
ll2.add_node(5)
ll2.add_node(10)
ll2.add_node(2)
ll2.add_node(1)

ll3 = LinkedList()
ll3.add_node(12)
ll3.add_node(2)
ll3.add_node(101)
ll3.add_node(101)
ll3.add_node(2)
ll3.add_node(12)


"""
def if_palindrome(ll):
    num_list = list()
    i = 0

    node = ll.head
    while node is not None:
        num_list.append(node.data)
        node = node.next

    length = len(num_list)
    for i in range(length/2+1):
        if i == length - i - 1:
            return True

        if num_list[i] != num_list[length - i - 1]:
            return False
"""


# Time: O(N)  Space: O(N)
def if_palindrome(ll):
    num_list = list()

    node_f = ll.head
    node_s = ll.head
    while node_s is not None:
        if node_f is None:
            if node_s.data != num_list.pop():
                return False
        else:
            node_f = node_f.next
            if node_f is not None:
                node_f = node_f.next
                num_list.append(node_s.data)
        node_s = node_s.next

    return True

print if_palindrome(ll1)
print if_palindrome(ll2)
print if_palindrome(ll3)
