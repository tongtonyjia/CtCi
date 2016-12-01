###############################################################################
#
# 3.4 Queue via Stacks
#
# Implement a MyQueue class which implements a queue using two stacks.
#
###############################################################################

import LibraryPath
from lib.Stack import StackNode, Stack


class MyQueue:
    def __init__(self):
        self.stack_head = Stack()
        self.stack_tail = Stack()

    def shift(self):
        if self.stack_head.isEmpty():
            while not self.stack_tail.isEmpty():
                self.stack_head.push(self.stack_tail.pop().data)
        else:
            while not self.stack_head.isEmpty():
                self.stack_tail.push(self.stack_head.pop().data)

    def add(self, data):
        if self.stack_tail.isEmpty():
            self.shift()
        self.stack_tail.push(data)

    def remove(self):
        if self.stack_head.isEmpty():
            self.shift()
        return self.stack_head.pop().data

qq = MyQueue()
qq.add(5)
qq.add(3)
qq.add(1)
print qq.remove()
print qq.remove()
