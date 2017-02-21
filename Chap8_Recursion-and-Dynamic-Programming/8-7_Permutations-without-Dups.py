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
    perms = []
    for c in s:
        perms.append([c])

    while len(perms[0]) != len(s):
        perm = perms.pop(0)
        for c in s:
            if c not in perm:
                new = deepcopy(perm)
                new.append(c)
                perms.append(new)

    return perms

perms = permu(s)
for p in perms:
    print p
