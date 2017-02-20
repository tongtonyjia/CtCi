###############################################################################
#
# 8.6 Towers of Hanoi
#
# In the classic problem of the Towers of Hanoi, you have 3 towers and N disks
# of different sizes which can slide onto any tower. The puzzle starts with
# disks sorted in ascending order of size from top to bottom (i.e., each disk
# sites on top of an even larger one).
#
# You have the following contraints:
# (1) Only one disk can be move at a time.
# (2) A disk is slid off the top of one tower onto another tower.
# (3) A disk cannot be placed on top of a smaller disk.
#
# Write a program to move the disks from the first tower to the last using
# stacks.
#
###############################################################################

hanoi = {
    1: [7, 6, 5, 4, 3, 2, 1],
    2: [],
    3: []
}


def hanoi_swap(n=None):
    if n is None:
        n = len(hanoi[1])
    return _hanoi_swap(n, 1, 2, 3)


def _hanoi_swap(n, origin, buff, dest):
    if n <= 0:
        return

    _hanoi_swap(n-1, origin, dest, buff)

    hanoi[dest].append(hanoi[origin].pop())

    _hanoi_swap(n-1, buff, origin, dest)


print hanoi
hanoi_swap(n=3)
print hanoi
