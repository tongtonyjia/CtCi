###############################################################################
#
# 8.3 Magic Index
#
# A magic index in an array A[0...n-1] is defined to be an index such that
# A[i] = i. given a sorted array of distinct integers, write a method to find a
# magic index, if one exists, in array A.
#
# FOLLOW UP
# What if the values are not distinct?
#
###############################################################################


a = [-12, -5, -1, 0, 4, 5, 6, 9, 12, 46, 66, 78, 90]


def magic_index(a):
    if len(a) == 0:
        return None
    return _magic_index(a, 0, len(a)-1)


def _magic_index(a, start, finish):
    if start > finish:
        return None
    mid = (start + finish)/2
    if mid == a[mid]:
        return mid
    elif mid < a[mid]:
        return _magic_index(a, start, mid-1)
    else:
        return _magic_index(a, mid+1, finish)

found = magic_index(a)
print '{}: {}'.format(found, a[found])


a = [-12, -1, -1, -1, 0, 4, 4, 4, 4, 9, 12, 46, 66, 78, 90]


def magic_index_d(a):
    if len(a) == 0:
        return None
    return _magic_index_d(a, 0, len(a)-1)


def _magic_index_d(a, start, finish):
    if start > finish:
        return None
    mid = (start + finish)/2
    if mid == a[mid]:
        return mid
    left = min(mid-1, a[mid-1])
    found = _magic_index_d(a, start, left)
    if found is not None:
        return found
    right = max(mid+1, a[mid+1])
    return _magic_index_d(a, right, finish)

found = magic_index_d(a)
print '{}: {}'.format(found, a[found])
