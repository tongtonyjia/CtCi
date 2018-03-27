###############################################################################
#
# You have a ladder n-steps in height.
# You can either take one step or two steps up the ladder at a time.
# How can you find out all the different combinations up the ladder?
# Then figure out an algorithm that will actually print out all the different
# ways up the ladder.
# i.e.: 1,1,2,1,2,2... etc...
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


def ladder(n, steps):
    if n == 0:
        print(steps)
        return
    elif n < 0:
        return

    ladder(n-1, steps + [1])
    ladder(n-2, steps + [2])

    return


ladder(7, [])
