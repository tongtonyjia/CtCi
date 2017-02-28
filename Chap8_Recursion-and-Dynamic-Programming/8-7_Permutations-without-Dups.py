###############################################################################
#
# 8.7 Permutations without Dups
#
# Write a method to compute all permutations of a string of unique characters.
#
###############################################################################

from copy import deepcopy


s = 'asdf'


def permu(s):
    perms = list()
    for c in s:
        perms.append(c)

    idx = 0
    while len(perms[idx]) != len(s):
        perm = perms[idx]
        for c in s:
            if c not in perm:
                new = deepcopy(perm)
                new += c
                perms.append(new)
        idx += 1

    return perms[idx:]

perms = permu(s)
for p in perms:
    print p
    pass
