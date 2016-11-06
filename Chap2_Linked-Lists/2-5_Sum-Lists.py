###############################################################################
#
# 2.5 Sum Lists
#
# You have two numbers represented by a linked list, where each node contains a
# single digit. The digits are stored in reverse order, such that the 1's digit
# is at the head of the list. Write a function that adds the two numbers and
# returns the sum as a linked list.
#
# EXAMPLE
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
#
# FOLLOW UP
# Suppose the digits are stored in foward order. Repeat the above problem.
#
# EXAMPLE:
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.
#
###############################################################################

import LibraryPath
from lib.LinkedList import LinkedList


num1_rev = LinkedList()
num1_rev.add_node(7)
num1_rev.add_node(1)
num1_rev.add_node(6)

num2_rev = LinkedList()
num2_rev.add_node(5)
num2_rev.add_node(9)
num2_rev.add_node(2)


num1_for = LinkedList()
num1_for.add_node(6)
num1_for.add_node(1)
num1_for.add_node(7)

num2_for = LinkedList()
num2_for.add_node(2)
num2_for.add_node(9)
num2_for.add_node(5)


def sum_lists_rev(num1_list, num2_list):
    node1 = num1_list.head
    node2 = num2_list.head

    result = 0

    pos = 0
    while node1 is not None:
        result += node1.data * 10**pos
        pos += 1
        node1 = node1.next

    pos = 0
    while node2 is not None:
        result += node2.data * 10**pos
        pos += 1
        node2 = node2.next

    result_list = LinkedList()
    for digit in str(result)[::-1]:
        result_list.add_node(int(digit))

    return result_list

sum_lists_rev(num1_rev, num2_rev).print_list()


def sum_lists_for(num1_list, num2_list):
    node1_num = ''
    node = num1_list.head
    while node is not None:
        node1_num += str(node.data)
        node = node.next

    node2_num = ''
    node = num2_list.head
    while node is not None:
        node2_num += str(node.data)
        node = node.next

    result = int(node1_num) + int(node2_num)

    result_list = LinkedList()
    for digit in str(result):
        result_list.add_node(int(digit))

    return result_list

sum_lists_for(num1_for, num2_for).print_list()
