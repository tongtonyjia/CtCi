###############################################################################
#
# 8.5 Recursive Multiply
#
# Write a recursive function to multiply two positive integers without using
# the * operator. You an use addition, subtraction, and bit shifting, but you
# should minimize the number of those operations.
#
###############################################################################


def min_prod(a, b):
    s = min(a, b)
    b = max(a, b)
    return _min_prod(s, b)


def _min_prod(s, b):
    if s == 0:
        return 0
    if s == 1:
        return b

    ss = s >> 1
    half = _min_prod(ss, b)

    if s % 2 == 0:
        return half + half
    else:
        return half + half + b


print min_prod(7, 9)
