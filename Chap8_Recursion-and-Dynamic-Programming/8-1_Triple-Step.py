###############################################################################
#
# 8.1 Triple Step
#
# A child is runing up a staircase with n steps and can hop either 1 step, 2
# steps, or 3 steps at a time. Implement a method to count how many possible
# ways the child can run up the stairs.
#
###############################################################################


def count_ways_r(n, s):
    if s == n:
        return 1
    if s > n:
        return 0
    return count_ways_r(n, s+1) + count_ways_r(n, s+2) + count_ways_r(n, s+3)


print count_ways_r(15, 0)


def count_ways_rr(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return count_ways_rr(n-1) + count_ways_rr(n-2) + count_ways_rr(n-3)

print count_ways_rr(15)


def count_ways_d(n, cache=None):
    if n <= 0:
        return 0
    cache = dict()
    cache[1] = 1
    cache[2] = 2
    cache[3] = 4
    if 0 <= n < 4:
        return cache[n]
    for i in range(4, n+1):
        cache[i] = cache[i-1] + cache[i-2] + cache[i-3]

    return cache[n]


print count_ways_d(15)
