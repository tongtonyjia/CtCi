###############################################################################
#
# 3.1 Three in One
#
# Describe how you could use a single array to implement three stacks.
#
###############################################################################

import LibraryPath
from lib.Stack import StackNode


class Stack:
    def __init__(self, array, num_partitions):
        self.array = array
        self.tops = dict()
        self.ranges = dict()
        for num in range(num_partitions):
            self.tops[num] = (len(array)/num_partitions)*num
            self.ranges[num] = range(
                (len(array)/num_partitions)*num,
                (len(array)/num_partitions)*(num+1)
            )

    def push(self, partition_num, data):
        new_node = StackNode(data)

        if self.array[self.tops[partition_num]] is None:
            self.array[self.tops[partition_num]] = new_node
            print 'Pushed {} to Stack {}.'.format(data, partition_num)
        else:
            if self.tops[partition_num] + 1 in self.ranges[partition_num]:
                self.array[self.tops[partition_num] + 1] = new_node
                self.tops[partition_num] = self.tops[partition_num] + 1
                print 'Pushed {} to Stack {}.'.format(data, partition_num)
            else:
                print 'Can\'t push. Stack {} full.'.format(partition_num)

    def pop(self, partition_num):
        top = self.array[self.tops[partition_num]]
        if top is not None:
            if self.tops[partition_num] - 1 in self.ranges[partition_num]:
                self.tops[partition_num] = self.tops[partition_num] - 1
            else:
                self.array[self.tops[partition_num]] = None
            print 'Popped {} from Stack {}.'.format(top.data, partition_num)
        else:
            print 'Can\'t pop. Stack {} empty.'.format(partition_num)

        return top

    def peek(self, partition_num):
        return self.array[self.tops[partition_num]]

    def isEmpty(self, partition_num):
        return self.array[self.tops[partition_num]] is None


array = dict()
for num in range(9):
    array[num] = None
ss = Stack(array, 3)
ss.push(2, 5)
ss.push(2, 5)
ss.push(2, 5)
ss.pop(2)
ss.pop(2)
ss.pop(2)
ss.pop(2)
ss.push(2, 5)
ss.pop(2)
ss.peek(2)
ss.push(2, 5)
ss.peek(2)
ss.push(1, 5)
ss.push(1, 6)
ss.push(1, 3)
print ss.isEmpty(0)
ss.push(0, 3)
print ss.isEmpty(0)
ss.push(0, 3)
ss.push(0, 3)
ss.push(0, 3)
