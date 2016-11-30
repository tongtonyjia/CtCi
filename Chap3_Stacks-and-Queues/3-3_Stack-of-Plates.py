###############################################################################
#
# 3.3 Stack of Plates
#
# Imagine a (literal) stack of plates. If the stack gets too high, it might
# topple. Therefore, in real life, we would likely start a new stack when the
# previous stack exceeds some threshold. Implement a data structure SetOfStacks
# that mimics this. SetOfStacks should be composed of several stacks and should
# create a new stack once the previous one exceeds capacity. SetOfStacks.push()
# and SetOfStacks.pop() should behave identically to a single stack (that is,
# pop() should return the same values as it would if there were just a single
# stack).
#
# FOLLOWUP
# Implement a function popAt(int index) which performs a pop operation on a
# specific sub-stack.
#
###############################################################################

import LibraryPath
from lib.Stack import StackNode, Stack


class SetOfStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.stack_set = -1
        self.stack_pos = stack_size - 1
        self.set = []
        self.holes = []

    def push(self, data):
        if self.holes != []:
            hole = self.holes.pop()
            self.set[hole].push(data)
            print 'Filled hole at: {}.'.format(hole)
        else:
            if self.stack_pos == self.stack_size - 1:
                new_stack = Stack()
                new_stack.push(data)
                self.set.append(new_stack)
                self.stack_set += 1
                self.stack_pos = 0
                print 'Create stack: {}, pos: {}.'.format(
                    self.stack_set, self.stack_pos
                )
            else:
                self.set[self.stack_set].push(data)
                self.stack_pos += 1
                print 'Pushed stack: {}, pos: {}.'.format(
                    self.stack_set, self.stack_pos
                )

    def pop(self):
        if self.stack_set == -1:
            print 'Completely empty.'
            return None
        to_pop = self.set[self.stack_set].pop()
        print 'Popped stack: {}, pos: {}.'.format(
            self.stack_set, self.stack_pos
        )

        self.stack_pos -= 1
        if self.set[self.stack_set].isEmpty():
            self.set.pop()
            self.stack_set -= 1
            self.stack_pos = self.stack_size - 1

        print to_pop.data

    def popAt(self, stack_set):
        if stack_set <= self.stack_set:
            if not self.set[stack_set].isEmpty():
                to_pop = self.set[stack_set].pop()
                self.holes.append(stack_set)
                print self.holes
                print 'Popped stack and created hole: {}.'.format(
                    stack_set
                )
                print to_pop.data
            else:
                print 'Empty set: {}.'.format(stack_set)
        else:
            print 'No such set: {}.'.format(stack_set)


ss = SetOfStacks(3)
ss.push(2)
ss.push(3)
ss.push(4)
ss.push(2)
ss.push(1)
ss.pop()
ss.pop()
ss.pop()
ss.pop()
ss.pop()
ss.pop()
ss.pop()
ss.push(2)
ss.push(3)
ss.push(4)
ss.push(2)
ss.push(1)
ss.popAt(3)
ss.popAt(0)
ss.popAt(0)
ss.push(2)
ss.push(1)
ss.push(1)
