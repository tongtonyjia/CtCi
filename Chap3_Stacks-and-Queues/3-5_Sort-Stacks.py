###############################################################################
#
# 3.5 Sort Stacks
#
# Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements
# into any other data structure (such as an array). The stack supports the
# following operations: push, pop, peek, and isEmpty.
#
###############################################################################

# Note:
#  - If more pushes than pops, implement fake sort
#  - If more pops than pushes, implement real sort


import LibraryPath
from lib.Stack import StackNode, Stack


# this is a fake sort, which is faster, but not ideal for consecutive pops
#
class SortedStack():
    def __init__(self):
        self.stack = Stack()

    def _min_top_stack(self):
        tmp = Stack()
        min_data = float('Inf')
        while not self.stack.isEmpty():
            node = self.stack.pop()
            node_data = node.data
            if node_data < min_data:
                if min_data != float('Inf'):
                    tmp.push(min_data)
                min_data = node_data
            else:
                tmp.push(node_data)
        tmp.push(min_data)
        self.stack = tmp

    def push(self, data):
        self.stack.push(data)

    def pop(self):
        self._min_top_stack()
        return self.stack.pop()

    def peek(self):
        self._min_top_stack()
        return self.stack.peek()

    def isEmpty(self):
        return self.stack.isEmpty()

ss = SortedStack()
ss.push(2)
ss.push(3)
ss.push(0)
ss.push(4)
ss.push(2)
ss.push(1)
ss.push(7)
print ss.pop().data
print ss.pop().data
