###############################################################################
#
# 3.2 Stack Min
#
# How would you design a stack which, in addition to push and pop, has function
# min which returns the minimum element? Push, pop and min should all operate
# in O(1) time.
#
###############################################################################

import LibraryPath
from lib.Stack import StackNode


class Stack:
    def __init__(self):
        self.top = None
        self.min_stack = list()

    def push(self, data):
        node = StackNode(data)
        if self.top is None:
            self.min_stack.append(node)
        else:
            self.min_stack.append(
                node if data <= self.min_stack[-1].data else self.min_stack[-1]
            )
            node.next = self.top

        self.top = node

    def pop(self):
        top = self.top
        if self.top.next is not None:
            self.top = self.top.next
            self.min_stack.pop()

        return top

    def peek(self):
        return self.top

    def min(self):
        if len(self.min_stack) != 0:
            return self.min_stack[-1]
        else:
            return None


ss = Stack()
ss.push(2)
ss.push(3)
ss.push(4)
ss.push(2)
ss.push(1)
print ss.min().data  # should be 1
ss.pop()
print ss.min().data  # should be 2
ss.pop()
print ss.min().data  # should be 2
